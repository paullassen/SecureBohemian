from wifi import Cell

networks = Cell.all('wlan0')
netList = sorted(networks, key=lambda x: x.signal, reverse=True)

for net in netList:
    if not net.ssid == '':
        print(net.signal),
        print('\t'),
        print(net.ssid)
