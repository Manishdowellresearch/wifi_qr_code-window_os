from tkinter import *
from tkinter import ttk
import subprocess
import time
import json
import requests
import pprint

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
    global entry
    string= entry.get()
    wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    data = wifi.decode('utf-8')
    posSsid = data.find("SSID")
    posBssid = data.find("BSSID")
    culprit = data[posSsid:posBssid]
    cpos = culprit.find(":")
    #print(culprit[cpos+1:])
    a=culprit[cpos+1:]
    time.sleep(10)

    url = "http://100002.pythonanywhere.com/" 
    #searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
    payload = json.dumps({
    "cluster": "qr",
    "database": "qrcode",
    "collection": "wifi_qr_details",
    "document": "wifi_qr_details",
    "team_member_ID": "6766666",
    "function_ID": "ABCDE",
    "command": "insert",
    "field": {
        "Username": string,
        "wifiname": a
    },
    "update_field": {
        "order_nos": 21
    },
    "platform": "bangalore"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    time.sleep(15)
    win.destroy()

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()