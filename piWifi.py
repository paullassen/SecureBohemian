from wifi import Cell
import requests

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

networks = Cell.all('wlan0')
netList = sorted(networks, key=lambda x: x.signal, reverse=True)

netDict = {}
for net in netList:
    if not net.ssid == '':
    	if net.ssid in netDict:
	    pass
        else:
	    netDict[net.ssid] = net.signal
        print(net.signal),
        print('\t'),
        print(net.ssid)
print('')
netDict["RasPId"] = getserial()
print(netDict)
r = requests.post("http://5b4b7e6f.ngrok.io", data=netDict)
