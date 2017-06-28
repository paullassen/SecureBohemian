from wifi import Cell
import requests

networks = Cell.all('wlan0')
netList = sorted(networks, key=lambda x: x.signal, reverse=True)

r = requests.post("http://fa4886b0.ngrok.io", data={'ssid': 'netName', 'sgstr1': '-31'})

for net in netList:
    if not net.ssid == '':
		if net.ssid == 'cafelabohemesanfrancisco' or net.ssid == 'CGNVM-18C0' or net.ssid == 'PasswordIsPassword':
			r = requests.post("http://fa4886b0.ngrok.io", data={'ssid': net.ssid, 'sgstr': net.signal})
        print(net.signal),
        print('\t'),
        print(net.ssid)
