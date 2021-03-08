import netifaces as nif
def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        print(addrs)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            if_ip = addrs[nif.AF_INET][0]['addr']
        #except IndexError, KeyError: #ignore ifaces that dont have MAC or IP
        except:
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None

#print(mac_for_ip('192.168.1.228'))
print(mac_for_ip('192.168.1.112'))