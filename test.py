'''import netifaces as nif
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
print(mac_for_ip('192.168.1.112'))'''


import mysql.connector

import time
import datetime

mydb = mysql.connector.connect(
host="192.168.1.176",
user="root",
password="password",
database="laravel"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM attendances where user_id=3")
#id user_id date status start_time end_time
myresult = mycursor.fetchall()

if(not myresult):
    print('Null')
else:
    print(myresult[2])
    print(myresult[2][2])

    #timestamp = datetime.timestamp(datetime.now())
    #print("timestamp =", timestamp)

    #dt_object = datetime.fromtimestamp(timestamp)

    #print("dt_object =", dt_object)

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    print(timestamp)
    

    from dateutil.parser import parse

    date1 = myresult[2][2].strftime('%Y-%m-%d')

    if(date1==timestamp):
        print("Match! date")

    if(myresult[2][2]==timestamp):
        print("Match!")
    else:
        print("Not!")

    #query = "UPDATE attendances SET date = '"+timestamp+"'  where id=5"
    #print(query)


    #mycursor.execute(query)
    #mydb.commit()

