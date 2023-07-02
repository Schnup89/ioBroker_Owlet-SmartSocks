from pyowletapi.api import OwletAPI
from pyowletapi.sock import Sock

import asyncio
import json
import requests
import time

#### Konfiguration
sIO_Url="http://127.0.0.1:8087/"
sIO_Path="admin.0.smartsocks."  #SimpleAPI-Adapter Port + Pfad anpassen!
sAPI_User="xxxxxxxxxx@xxx.com"  #Owlet APP Email-Adresse
sAPI_Pass="xxxxxxxxxxxx"        #Owlet APP Passwort
###

async def run():
  #Initialisiere API
  api = OwletAPI('europe', sAPI_User, sAPI_Pass)
  #Verbindung aufbauen und authentifizieren
  await api.authenticate()
  #Hole erstes Gerät
  devices = await api.get_devices()
  socks = { device["device"]["dsn"]: Sock(api, device["device"]) for device in devices }
  #Hole Daten für Socken
  for sock in socks.values():
    properties = await sock.update_properties()
    properties = properties[1]
    #Hole Info von IOBroker welche ID's abzurufen sind (simple-api Adapter notwendig)
    jIO_Obj = json.loads(requests.get(sIO_Url+"states?pattern="+sIO_Path+"*").content)
    print(properties)
    for key in jIO_Obj:
      #Hole state name aus Objektnamen (admin.xxx.xxx.xxx)
      sStateID = key.rsplit('.',1)[1]
      requests.get(sIO_Url+"set/"+sIO_Path+sStateID+"?value="+str(properties[sStateID]))

  #Warte auf Connection Close
  await api.close()



#Starte Programm und wiederhole unendlich lange
while(1):
  asyncio.run(run())
  time.sleep(5)
