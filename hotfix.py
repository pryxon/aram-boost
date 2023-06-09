# -*- coding: utf-8 -*-
import shutil
import os
import time
import colorama
import sys
import subprocess
import tkinter as tk
import tkinter.filedialog as tk_FileDialog

colorama.init()

__author__: str = "pryxon"
__version__: str = "1.0.4"

def getFileDialogTitle(msg: str, title: str) -> str:

    if msg and title:
        return "%s - %s" % (title, msg)

    if msg and not title:
        return str(msg)

    if title and not msg:
        return str(title)

    return None

def diropenbox(msg: str=None, title: str=None, default=None) -> str:
    title = getFileDialogTitle(msg, title)

    localRoot = tk.Tk()
    localRoot.withdraw()
    localRoot.lift()
    localRoot.attributes('-topmost', 1)
    localRoot.attributes('-topmost', 0)

    if not default:
        default = None

    localRoot.update()
    f = tk_FileDialog.askdirectory(parent=localRoot, title=title, initialdir=default, initialfile=None)
    localRoot.destroy()

    if not f:
        return None

    return os.path.normpath(f)

def copyFiles(path: str) -> None:

    try:
        print(colorama.Fore.BLUE + "[+] Copying Clients..." + colorama.Style.RESET_ALL)
        shutil.copy("folder/LeagueClient.exe", path)
        shutil.copy("folder/LeagueClientUX.exe", path)

        print(colorama.Fore.BLUE + "[+] Copying Plugin-Manifest..." + colorama.Style.RESET_ALL)
        shutil.copy("folder/plugin-manifest.json", path + "\Plugins")

        print(colorama.Fore.BLUE + "[+] Copying Assets.wad..." + colorama.Style.RESET_ALL)
        shutil.copy("folder/assets.wad", path + "\Plugins\\rcp-fe-lol-champ-select")

    except PermissionError:
        print(colorama.Fore.RED + "[-] Error: The game is already running in the background. Close the game" + colorama.Style.RESET_ALL)
        time.sleep(10)
        exit()

    except FileNotFoundError:
        print(colorama.Fore.RED + "[-] Error: The folder named 'folder' was not found please download the cheat again and don't touch the folder named 'folder'." + colorama.Style.RESET_ALL)
        time.sleep(10)
        exit()
    
    except Exception as err:
        print(colorama.Fore.RED + f"[-] Error: {err}" + colorama.Style.RESET_ALL)
        time.sleep(10)
        exit()

    try:
        print(colorama.Fore.GREEN + "[+] Starting League Of Legends..." + colorama.Style.RESET_ALL)
        subprocess.Popen([path + '/LeagueClient.exe', '--allow-multiple-clients', '--legacy-SSL', '--no-proxy'])
    
    except Exception:
        print(colorama.Fore.RED + "[-] Error: Can't find where league of legends is installed" + colorama.Style.RESET_ALL)
        time.sleep(10)
        exit()
    
def main() -> None:
    
    path_var: bool = False

    for i in path_list:
        try:
            with open(i + "/LeagueClient.exe", "r") as f:
                f.encoding
                path_var = True
                path = i
                break
        
        except Exception: continue
    
    if path_var is False:
        try:
            with open("folder/path.txt", "r", encoding="utf-8") as f:
                path = str(f.read())
                path_var = True
        
        except Exception: path_var = False
    
    if path_var is False:

        print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "[+] Select the folder where League of Legends is installed" + colorama.Style.RESET_ALL)
        path = diropenbox("Select LOL Path", "R3nzTheCodeGOD")
        
        with open("folder/path.txt", "w", encoding="utf-8") as f:
            f.write(path)

    copyFiles(path)

if __name__ == "__main__":

    os.system("@echo off")
    os.system("cls")

    start: float = time.perf_counter()
    path: str = ""

    path_list: list = [
        "C:/Riot Games/League of Legends", "C:/Program Files (x86)/Riot Games/League of Legends", "C:/Program Files/Riot Games/League of Legends",
        "D:/Riot Games/League of Legends", "D:/Program Files (x86)/Riot Games/League of Legends", "D:/Program Files/Riot Games/League of Legends",
        "E:/Riot Games/League of Legends", "E:/Program Files (x86)/Riot Games/League of Legends", "E:/Program Files/Riot Games/League of Legends",
        "F:/Riot Games/League of Legends", "F:/Program Files (x86)/Riot Games/League of Legends", "F:/Program Files/Riot Games/League of Legends"
    ]

    print(colorama.Style.BRIGHT + colorama.Fore.GREEN + f"""
     ____  _____           _____ _           ____          _       ____  ___  ____  
                                                            
                                                            
 $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |  $$ |\$$\ $$  |$$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  \__|$$ |  $$ | \$$$$  / $$ /  $$ |$$ |  $$ |
$$ |  $$ |$$ |      $$ |  $$ | $$  $$<  $$ |  $$ |$$ |  $$ |
$$$$$$$  |$$ |      \$$$$$$$ |$$  /\$$\ \$$$$$$  |$$ |  $$ |
$$  ____/ \__|       \____$$ |\__/  \__| \______/ \__|  \__|
$$ |                $$\   $$ |                              
$$ |                \$$$$$$  |                              
\__|                 \______/                             

                    {colorama.Fore.CYAN + "GitHub: https://github.com/pryxon/aram-boost"}
                    {colorama.Fore.CYAN + "Discord: " + colorama.Style.RESET_ALL}""")

    main()

    print(colorama.Fore.BLUE + f"[+] the process took {round(time.perf_counter() - start, 2)}s" + colorama.Style.RESET_ALL)
    
    time.sleep(5)