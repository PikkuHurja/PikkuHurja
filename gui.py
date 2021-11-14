import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import socket
import base64 as b64

from decodinsmth import pw
from decodinsmth import us
from decodinsmth import pr
from decodinsmth import hs


def clear_ter():
    for x in range(0, 10):
        print("\n" + "\n" + "\n")


import paramiko as pm
from colorama import *
import time as tm
init(convert=True)
init(autoreset=True)

windowBg = "#3e4756"
textCl = "#d3dbdc"
buttonCl = "#23272a"
fiedlCl = "#2c2f33"

#/button remotefile colors//

dirButtonCl = "#0b1c47"
audButtonCl = "#470b3d"
vidButtonCl = "#47450b"
picButtonCl = "#104a1b"
othButtonCl = "#393042"


root = tk.Tk()
root.title("AB File Transfer")
root.configure(bg=windowBg)
root.iconbitmap('resource/icon.ico')
img = PhotoImage(file="resource/bg.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)


buttonFont = font.Font(size=30)

hostFolder = "/home/pikku/copy"
chUpFi = 0
foldSelected = 0
foldSelected1 = 0

def logged_in():
    
    
    
    enterPass.destroy()
    enterUsr.destroy()
    enterPort.destroy()
    enterHost.destroy()
    passField.destroy()
    usrField.destroy()
    portField.destroy()
    hostField.destroy()
    MainButton.destroy()
    useDefButton.destroy()
    setDefButton.destroy()
    bufferGrid0.destroy()
    bufferGrid1.destroy()
    bufferGrid2.destroy()
    bufferGrid3.destroy()
    
    if type(onSend.inport) == str:
        onSend.inport = int(onSend.inport)

    
    
    
    loc_folder.foldSelected = 0
    selected_file.selected = 0
    print(Fore.RED + "Connecting...")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((onSend.inhost, onSend.inport))
    retry = 0
    while result != 0:
        print(Fore.RED + "Retrying...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((onSend.inhost, onSend.inport))
        tm.sleep(1)
        retry = retry + 1
        if retry > 10:
            print("Could Not Connect To Server @", onSend.inhost, onSend.inport)
            tm.sleep(3)
            exit()
            
    
    
    print(Fore.GREEN + Style.BRIGHT + "Connection Found")
    Sshc()
    selScr()

def onSend():
    onSend.inpass = passField.get()
    onSend.inusr = usrField.get()
    onSend.inport = portField.get()
    onSend.inhost = hostField.get()
    
    if onSend.inport.isdigit() == False:
        onSend.inport = 22
    
    logged_in()

def useDef():
    onSend.inpass = pw
    onSend.inusr = us
    onSend.inport = pr
    onSend.inhost = hs
    logged_in()

    
def setDef():
    onSend.inpass = passField.get()
    onSend.inusr = usrField.get()
    onSend.inport = portField.get()
    onSend.inhost = hostField.get()
        
    inpass = onSend.inpass.encode("ascii")
    inuser = onSend.inusr.encode("ascii")
    inport = onSend.inport.encode("ascii")
    inhost = onSend.inhost.encode("ascii")
    
    inpass = b64.b64encode(inpass)
    inuser = b64.b64encode(inuser)
    inport = b64.b64encode(inport)
    inhost = b64.b64encode(inhost)
    
    pww = inpass.decode("ascii")
    usw = inuser.decode("ascii")
    prw = inport.decode("ascii")
    hsw = inhost.decode("ascii")
    
    
    keys = open("keys.txt", "w+")
    keys.write(pww + "\n" + usw + "\n" + prw + "\n" + hsw + "\n")
    
    keys.close()

    
    
    
    
 
def selScr():
    selScr.DownloadButt = Button(root, text="Download", command=Download, bg=buttonCl, fg=textCl,)
    selScr.UpButt = Button(root, text="  Upload  ", command=Upload, bg=buttonCl, fg=textCl,)

    selScr.DownloadButt['font'] = buttonFont
    selScr.UpButt['font'] = buttonFont

    
    
    selScr.UpButt.grid(row=1, column=1)
    selScr.DownloadButt.grid(row=1, column=9)
    
    



    
def Download():
    selScr.DownloadButt.destroy()
    selScr.UpButt.destroy()
    
    
    Download.localbutt = Button(root, text="Select Download Folder", command=loc_folder, bg=buttonCl, fg=textCl)
    Download.hostbutt = Button(root, text="Select File To Download", command=command_ls, bg=buttonCl, fg=textCl)

    Download.hosttxt = Label(root, text="Selected Remote File: ", bg=windowBg, fg=textCl)
    Download.localtxt = Label(root, text="Selected Folder: ", bg=windowBg, fg=textCl)
    
    rem_popup.displayFiles = 1
    
    Download.localbutt.grid(row=1, column=0)
    Download.hostbutt.grid(row=1, column=1)
    Download.localtxt.grid(row=2, column=0)
    Download.hosttxt.grid(row=2, column=1)
    
def Upload():
    selScr.DownloadButt.destroy()
    selScr.UpButt.destroy()
    
    Upload.localbutt = Button(root, text="Select File To Upload", command=loc_file, bg=buttonCl, fg=textCl)
    Upload.hostbutt = Button(root, text="Select Remote Folder To Upload", command=command_ls, bg=buttonCl, fg=textCl)
    
    Upload.hosttxt = Label(root, text="Selected Remote Folder: " + hostFolder, bg=windowBg, fg=textCl)
    Upload.localtxt = Label(root, text="Selected File: ", bg=windowBg, fg=textCl)
    
    rem_popup.displayFiles = 0
    
    Upload.localbutt.grid(row=1, column=0)
    Upload.hostbutt.grid(row=1, column=1)
    Upload.localtxt.grid(row=2, column=0)
    Upload.hosttxt.grid(row=2, column=1)

def loc_file():
    loc_file.locFilePath = filedialog.askopenfilename()
    loc_file.locFile = os.path.basename(loc_file.locFilePath)
    

    Upload.localtxt.destroy()
    Upload.localtxt = Label(root, text="Selected File: " + loc_file.locFile, bg=windowBg, fg=textCl)
    Upload.localtxt.grid(row=2, column=0)

    Upload.Uploadbut = Button(root, text="Upload", command=exec_upload, bg=buttonCl, fg=textCl)
    Upload.Uploadbut.grid(row=9, column=9)
    
    chUpFi = 1

    
def loc_folder():
    loc_folder.locFolder = filedialog.askdirectory()
    
    Download.localtxt.destroy()
    Download.localtxt = Label(root, text="Selected Folder: " + loc_folder.locFolder,bg=windowBg, fg=textCl)
    Download.localtxt.grid(row=2, column=0)
    
    loc_folder.foldSelected = 1
    foldCheck()

    

def command_ls():
    stdin, stdout, stderr = Sshc.ssh.exec_command("cd copy" + add_rm_path.addPath + ";pwd;ls")
    list = stdout.readlines()
    
    #remove \newline//
    
    clist = []
    for element in list:
        clist.append(element.strip())
        
    #get out pwd#
    command_ls.pwd = clist.pop(0)
    ls = clist
    lenght = len(ls)
    
    
    flie = ""
    plis = ""
    lis = []
    command_ls.dir = []
    command_ls.aud = []
    command_ls.vid = []
    command_ls.pic = []
    command_ls.oth = []
    
    
    
    i = 0
    
    while lenght > i:
        path = ls[i]
        flie, plis = os.path.splitext(path)

        
        if plis == '':                                          #folder
            command_ls.dir.append(flie)
            
            
        elif plis == '.mp3' or plis == '.aac' or plis == '.flac' or plis == '.alac' or plis == '.waw' or plis == '.aiff' or plis == '.dsd' or plis == '.reapeaks' or plis == '.MP3':                                     #audio
            command_ls.aud.append(flie + plis)
            
        elif plis == '.mov' or plis == '.mp4' or plis == '.mkv' or plis == '.wmv' or plis == '.avi' or plis == '.flv' or plis == '.f4v' or plis == '.swf' or plis == '.MP4':   #video
            command_ls.vid.append(flie + plis)
            
        elif plis == '.jpg' or plis == '.png' or plis == '.raw' or plis == '.jpeg' or plis == '.gif' or plis == '.eps' or plis == '.ai' or plis == '.pdf' or plis == '.tiff' or plis == '.psd' or plis == '.eps' or plis == '.indd' : #picture
            command_ls.pic.append(flie + plis)
            
        else:                                                   #other
            command_ls.oth.append(flie + plis)
    
        lis.append(plis)
        i = i + 1
    rem_popup()
    
def rem_popup():
    rem_popup.remo = tk.Tk()
    rem_popup.remo.title("Select Remote File / Folder From: " + command_ls.pwd)
    rem_popup.remo.configure(bg=windowBg)
    rem_popup.remo.geometry("+500+500")
    
    wrapLen = 7
    
    rem_popup.remo.minsize(700, 100)
    
    rem_popup.i=0
    
    lenght = len(command_ls.dir)
    
    while lenght > rem_popup.i:
        
        
        if wrapLen > lenght:
            rem_popup.remBut0 = Button(rem_popup.remo, text=command_ls.dir[rem_popup.i], command=lambda idx = rem_popup.i: add_rm_path(idx), bg=dirButtonCl, fg=textCl, wraplength=190)
            rem_popup.remBut0.grid(row=1, column=rem_popup.i)
            rem_popup.i = rem_popup.i + 1
        else:
            print("much lenght")
            if wrapLen > lenght:
                rem_popup.remBut0 = Button(rem_popup.remo, text=command_ls.dir[rem_popup.i], command=lambda idx = rem_popup.i: add_rm_path(idx), bg=dirButtonCl, fg=textCl, wraplength=190)
                rem_popup.remBut0.grid(row=1, column=rem_popup.i)
                rem_popup.i = rem_popup.i + 1
                
            elif wrapLen * 2 > lenght:
                rem_popup.remBut0 = Button(rem_popup.remo, text=command_ls.dir[rem_popup.i], command=lambda idx = rem_popup.i: add_rm_path(idx), bg=dirButtonCl, fg=textCl, wraplength=190)
                rem_popup.remBut0.grid(row=1, column=rem_popup.i - wrapLen)
                rem_popup.i = rem_popup.i + 1
            
                
            
        
    if rem_popup.displayFiles == 1:
        
        rem_popup.i=0
        
        
        lenght = len(command_ls.aud)
        
        while lenght > rem_popup.i:
            if wrapLen > lenght:
                ft = "aud"
                remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                remBut1.grid(row=10, column=rem_popup.i)
                rem_popup.i = rem_popup.i + 1
                
            else:
                ft = "aud"
                print("much lenght")
                print("len", lenght)
                print("wrapLen",wrapLen)
                if wrapLen > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=10, column=rem_popup.i)
                    rem_popup.i = rem_popup.i + 1
                    
                elif wrapLen * 2 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=11, column=rem_popup.i - wrapLen)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 3 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=12, column=rem_popup.i - wrapLen * 2)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 4 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=13, column=rem_popup.i - wrapLen * 3)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 5 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=14, column=rem_popup.i - wrapLen * 4)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 6 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=15, column=rem_popup.i - wrapLen * 5)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 7 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=16, column=rem_popup.i - wrapLen * 6)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 8 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=17, column=rem_popup.i - wrapLen * 7)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=18, column=rem_popup.i - wrapLen * 8)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=19, column=rem_popup.i - wrapLen * 9)
                    rem_popup.i = rem_popup.i + 1
                    
                    
                    
                else:
                    print("wtf")
                    remBut1 = Button(rem_popup.remo, text=command_ls.aud[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=audButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=20, column=rem_popup.i - 2 * wrapLen * 10)
                    rem_popup.i = rem_popup.i + 1
            
        rem_popup.i=0
        
        
        lenght = len(command_ls.vid)

        
        while lenght > rem_popup.i:
            if wrapLen > lenght:
                ft = "vid"
                remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                remBut1.grid(row=23, column=rem_popup.i)
                rem_popup.i = rem_popup.i + 1
                
            else:
                ft = "vid"
                print("much lenght")
                print("len", lenght)
                print("wrapLen",wrapLen)
                if wrapLen > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=23, column=rem_popup.i)
                    rem_popup.i = rem_popup.i + 1
                    
                elif wrapLen * 2 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=24, column=rem_popup.i - wrapLen)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 3 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=25, column=rem_popup.i - wrapLen * 2)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 4 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=26, column=rem_popup.i - wrapLen * 3)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 5 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=27, column=rem_popup.i - wrapLen * 4)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 6 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=28, column=rem_popup.i - wrapLen * 5)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 7 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=29, column=rem_popup.i - wrapLen * 6)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 8 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=30, column=rem_popup.i - wrapLen * 7)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=31, column=rem_popup.i - wrapLen * 8)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=32, column=rem_popup.i - wrapLen * 9)
                    rem_popup.i = rem_popup.i + 1
                    
                    
                    
                else:
                    remBut1 = Button(rem_popup.remo, text=command_ls.vid[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=vidButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=33, column=rem_popup.i - 2 * wrapLen * 10)
                    rem_popup.i = rem_popup.i + 1
            
            
            
            
        rem_popup.i=0
        
        
        lenght = len(command_ls.pic)
        
        while lenght > rem_popup.i:
        
            if wrapLen > lenght:
                ft = "pic"
                remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                remBut1.grid(row=34, column=rem_popup.i)
                rem_popup.i = rem_popup.i + 1
                
            else:
                ft = "pic"
                print("much lenght")
                print("len", lenght)
                print("wrapLen",wrapLen)
                if wrapLen > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=35, column=rem_popup.i)
                    rem_popup.i = rem_popup.i + 1
                    
                elif wrapLen * 2 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=36, column=rem_popup.i - wrapLen)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 3 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=37, column=rem_popup.i - wrapLen * 2)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 4 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=38, column=rem_popup.i - wrapLen * 3)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 5 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=39, column=rem_popup.i - wrapLen * 4)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 6 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=40, column=rem_popup.i - wrapLen * 5)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 7 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=41, column=rem_popup.i - wrapLen * 6)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 8 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=42, column=rem_popup.i - wrapLen * 7)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=43, column=rem_popup.i - wrapLen * 8)
                    rem_popup.i = rem_popup.i + 1
                    
                    
                    
                    
                else:
                    print("wtf")
                    remBut1 = Button(rem_popup.remo, text=command_ls.pic[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=picButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=44, column=rem_popup.i - 2 * wrapLen * 9)
                    rem_popup.i = rem_popup.i + 1
                    
                

            
        rem_popup.i=0
        
        
        lenght = len(command_ls.oth)

        
        while lenght > rem_popup.i:
        
            if wrapLen > lenght:
                ft = "oth"
                remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                remBut1.grid(row=45, column=rem_popup.i)
                rem_popup.i = rem_popup.i + 1
                
            else:
                ft = "oth"
                print("much lenght")
                print("len", lenght)
                print("wrapLen",wrapLen)
                if wrapLen > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=45, column=rem_popup.i)
                    rem_popup.i = rem_popup.i + 1
                    
                elif wrapLen * 2 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=46, column=rem_popup.i - wrapLen)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 3 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=47, column=rem_popup.i - wrapLen * 2)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 4 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=48, column=rem_popup.i - wrapLen * 3)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 5 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=49, column=rem_popup.i - wrapLen * 4)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 6 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=50, column=rem_popup.i - wrapLen * 5)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 7 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=51, column=rem_popup.i - wrapLen * 6)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 8 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=52, column=rem_popup.i - wrapLen * 7)
                    rem_popup.i = rem_popup.i + 1
                elif wrapLen * 9 > rem_popup.i:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=53, column=rem_popup.i - wrapLen * 8)
                    rem_popup.i = rem_popup.i + 1
                    
                    
                    
                    
                else:
                    remBut1 = Button(rem_popup.remo, text=command_ls.oth[rem_popup.i], command=lambda idx = rem_popup.i, fts = ft: selected_file(idx, fts), bg=othButtonCl, fg=textCl, wraplength=90)
                    remBut1.grid(row=54, column=rem_popup.i - 2 * wrapLen * 9)
                    rem_popup.i = rem_popup.i + 1
            
            
    rem_popup.remBut2 = Button(rem_popup.remo, text="Recent Folder", command=sub_folder, bg=othButtonCl, fg=textCl)
    rem_popup.remBut2.grid(row=56, column=0)
    
            
            

def add_rm_path(idx):
    
    prsBtn = command_ls.dir[idx]
    
    add_rm_path.addPath = add_rm_path.addPath + "/" + prsBtn
    
    rem_popup.remo.destroy()
    command_ls()
    
    Upload.hosttxt = Label(root, text="Selected Remote Folder: " + hostFolder + add_rm_path.addPath, bg=windowBg, fg=textCl)
    Upload.hosttxt.grid(row=2, column=1)
    
    
    
    
def sub_folder():
    rem_popup.remo.destroy()
    remaining, cutoff = os.path.splitdrive(add_rm_path.addPath)
    add_rm_path.addPath = remaining
    command_ls()
    
       
    
def selected_file(idx, fts):
    if fts == "vid":
        selected_file.curFi = command_ls.vid[idx]
    elif fts == "aud":
        selected_file.curFi = command_ls.aud[idx]
    elif fts == "pic":
        selected_file.curFi = command_ls.pic[idx]
    elif fts == "oth":
        selected_file.curFi = command_ls.oth[idx]
    else:
        print("code error")
        
    
    
    
    rem_popup.remo.destroy()
    Download.hosttxt.destroy()
    Download.hosttxt = Label(root, text="Selected Remote File: " + selected_file.curFi, bg=windowBg, fg=textCl)
    Download.hosttxtLoc = Label(root, text="File Location: " + command_ls.pwd + "/"+ selected_file.curFi, bg=windowBg, fg=textCl)
    Download.hosttxt.grid(row=2, column=1)
    Download.hosttxtLoc.grid(row=3, column=1)  
    selected_file.selected = 1
    foldCheck()
    
    
def foldCheck():
    if selected_file.selected == 1:
        if loc_folder.foldSelected == 1:
            if exec_download.repeat == 1:
                exec_download.DFinish.destroy()
                exec_download.repeat = 0
            foldCheck.DwnldButton = Button(root, text="Download Now", command=exec_download, bg=buttonCl, fg=textCl)
            foldCheck.DwnldButton.grid(row=999, column=1)
            
        else:
            pass
    else:
        pass
def exec_download():
    print("selected_file.curFi:  ", selected_file.curFi)
    print("command_ls.pwd:  ", command_ls.pwd)
    print("add_rm_path.addPath:  ", add_rm_path.addPath)
    print("loc_folder.locFolder:  ", loc_folder.locFolder)
    
    
    print("remfi:  ", command_ls.pwd + "/" + selected_file.curFi)
    print(loc_folder.locFolder + "/" + selected_file.curFi)
    sftp = Sshc.ssh.open_sftp()
    sftp.get(command_ls.pwd + "/" + selected_file.curFi, loc_folder.locFolder + "/" + selected_file.curFi, callback=printTotals,)
    print(Fore.GREEN + "Finished Downloading")
    foldCheck.DwnldButton.destroy()
    exec_download.DFinish = Label(root, text="Download Finished", bg=windowBg, fg=textCl)
    exec_download.DFinish.grid(row=999, column=0)
    exec_download.repeat = 1
    

def exec_upload():
    print(loc_file.locFilePath, hostFolder + add_rm_path.addPath + "/" + loc_file.locFile)
    sftp = Sshc.ssh.open_sftp()
    sftp.put(loc_file.locFilePath, hostFolder + add_rm_path.addPath + "/" + loc_file.locFile, callback=printTotals,)
    print(Fore.GREEN + "Finished Uploading")


def Sshc():

    Sshc.ssh = pm.SSHClient()
    Sshc.ssh.set_missing_host_key_policy(pm.AutoAddPolicy())
    Sshc.ssh.connect(onSend.inhost, onSend.inport, onSend.inusr, onSend.inpass)
    print(Fore.GREEN + Style.BRIGHT + "SSH Connection Ready")
    

def printTotals(transferred, toBeTransferred):
    print("% Uploaded", 100 * (transferred / toBeTransferred))
    
exec_download.repeat = 0
add_rm_path.addPath = ""    
root.geometry("1000x400+300+300")

passField = Entry(root, width=20, bg=fiedlCl, fg=textCl)
usrField = Entry(root, width=20, bg=fiedlCl, fg=textCl)
portField = Entry(root, width=20, bg=fiedlCl, fg=textCl)
hostField = Entry(root, width=20, bg=fiedlCl, fg=textCl)


enterPass = Label(root, text="Enter Password", bg=windowBg, fg=textCl)
enterUsr = Label(root, text="Enter Username", bg=windowBg, fg=textCl)
enterPort = Label(root, text="Enter Port", bg=windowBg, fg=textCl)
enterHost = Label(root, text="Enter Host IP", bg=windowBg, fg=textCl)

bufferGrid0 = Label(root, text="    ",bg=windowBg, fg=textCl)
bufferGrid1 = Label(root, text="    ",bg=windowBg, fg=textCl)
bufferGrid2 = Label(root, text="    ",bg=windowBg, fg=textCl)
bufferGrid3 = Label(root, text="    ",bg=windowBg, fg=textCl)

MainButton = Button(root, text="Log In", command=onSend, bg=buttonCl, fg=textCl)
useDefButton = Button(root, text="Use Default", command=useDef, bg=buttonCl, fg=textCl)
setDefButton = Button(root, text="Set Default", command=setDef, bg=buttonCl, fg=textCl)


bufferGrid0.grid(row=6, column=0)
bufferGrid1.grid(row=7, column=0)
bufferGrid2.grid(row=8, column=0)
bufferGrid3.grid(row=9, column=0)

enterPass.grid(row=2, column=0)
enterUsr.grid(row=3, column=0)
enterPort.grid(row=4, column=0)
enterHost.grid(row=5, column=0)

passField.grid(row=2, column=1)
usrField.grid(row=3, column=1)
portField.grid(row=4, column=1)
hostField.grid(row=5, column=1)




MainButton.grid(row=99, column=1)
useDefButton.grid(row=99, column=9)
setDefButton.grid(row=99, column=8)
clear_ter()

root.mainloop()

