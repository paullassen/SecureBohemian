from wifi import Cell
import requests

networks = Cell.all('wlan0')
netList = sorted(networks, key=lambda x: x.signal, reverse=True)

netDat = {}
for net in netList:
    if not net.ssid == '':
		netDat[net.ssid] = net.signal
        print(net.signal),
        print('\t'),
        print(net.ssid)
r = requests.post("http://5b4b7e6f.ngrok.io", data=netDat)
