# ioBroker_Owlet-SmartSocks
QuicknDirty Implementierung um Werte des Owlet SmartSocks an ioBroker zu übertragen

Der [Owlet SmartSock 3](https://www.idealo.de/preisvergleich/OffersOfProduct/201641215_-smart-sock-3-owlet.html) hat vor kurzem Einzug in unser Leben genommen :relaxed:  
  
Die historischen Daten in der APP werden nur pro Stunde gespeichert und ich suchte eine Lösung um die Daten zugänglicher zu machen.  
  
ryanbdclark hat hier eine Python Implementierung Entwickelt, um die Daten Live aus der Cloud abfragen zu können. https://github.com/ryanbdclark/pyowletapi  
  
Mit den Scripten in meiner Anleitung werden die abgerufenen Daten aus der Owlet-Cloud an ioBroker zur weiteren Auswertung gesendet.  
  
Bitte hinterlasst mir eine kurze Nachrichten per Issue, im [ioBroker-Forum als PN](https://forum.iobroker.net/user/schnup89) oder im ioBroker-Forum-Thread wernn Ihr die Scripte nutzt, sollte es genügend Nutzer geben würde ich mich an einer nativen Implementierung als ioBroker Adapter versuchen.

# Ablauf
*Vorab: Das Script ist "auf die schnelle" Programmiert und bei weitem nicht optimiert oder sonst was, gerne per Pull-Request Verbesserungen einbringen!* 

- Per Crontab wird minütlich über ein Bash-Script geprüft ob das Python Script noch läuft, falls nicht wird dieses gestartet
- Das Python Script läuft unendlich lange und ruft alle 5 Sekunden aktuelle Daten aus der Cloud ab
- Es werden alle ID's in einem Ordner abgefragt und die Werte entsprechend gesetzt

# Installation
*Auf dem ioBroker*
- "Einfache RESTful API" bzw. "Simple-API" ioBroker Adapter installieren und aktivieren
- Ein Ordner unter Objekte anlegen, in meinem Beispiel wurde "admin.0.smartsocks" angelegt, könnt ihr die Werte die abgerufen werden sollen anlegen.
  Siehe dazu Kapitel "Parameter/States"
  
  
*Auf ein Linux-System (egal ob der ioBroker Host oder ein anderes System) verbinden per SSH*  
- ryanbdclark's Script installieren per PIP  
  `pip3 install pyowletapi`  
- Die beiden Dateien aus dem Github Repo herunterladen in z.B. /etc/scripts  
  `mkdir /etc/scripts`  <- Wenn Ihr einen eigenen Ordner wollt, alternativ mit `pwd` prüfen in welchen Ordner ihr euch befindet und diesen merken.  
  `cd /etc/scripts/`    <- In den Ordner wechseln  
  `wget xxx`  
  `wget yyy`  
- Solltet ihr /etc/scripts verwenden, dann muss die Datei checkowlet.sh nicht angepasst werden, falls doch die Ordnerangaben darin anpassen  
- In der Datei owletio.py unter Konfiguration die Daten eintragen:  
  `nano owletio.py` <- Werte anpassen und mit STRG+X und einem folgenden Y die Datei speichern.  
  Ihr könnt für die URL http://127.0.0.1:8087 stehen lassen solltet ihr auf dem ioBroker Host arbeiten, ansonsten hier die IP oder Name des ioBroker eintragen.  


# Paramter/States
Der Name der States muss mit den Werten welche die Cloud liefert übereinstimmen, damit die Werte angezeigt werden.  

Folgende Tabelle zeigt die aktuell verfügbaren Werte:  
`'app_active': Boolean`  
`'high_heart_rate_alert': Boolean`  
`'high_oxygen_alert': Boolean`  
`'low_battery_alert': Boolean`  
`'low_heart_rate_alert': Boolean`  
`'low_oxygen_alert': Boolean`  
`'ppg_log_file': Boolean`   
`'firmware_update_available': Boolean`    
`'lost_power_alert': Boolean`    
`'sock_disconnected': Boolean`  
`'sock_off': Boolean`   
`'oxygen_saturation': Number`  
`'heart_rate': Number`   
`'moving': Boolean`   
`'sock_connection': Number`  
`'skin_temperature': Number`   
`'base_station_on': Boolean`  
`'battery_percentage': Number`   
`'battery_minutes': Number`   
`'charging': Boolean`   
`'alert_paused_status': Boolean`  
`'signal_strength': Number`   
`'sleep_state': Number`   
`'oxygen_10_av': Number`  
`'last_updated': String`  
  
Wollt ihr nur den Wert `oxygen_saturation` abfragen so legt einen State des Typ Number und der ID oxygen_saturation an, Beispiele:  
![image](https://github.com/Schnup89/ioBroker_Owlet-SmartSocks/assets/28166743/42f6a184-7047-4a34-8c91-bc8f33d8eef2)
