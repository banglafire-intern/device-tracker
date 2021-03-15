import mysql.connector
import time
import datetime

def sendAttendance(user):
  mydb = mysql.connector.connect(
    host="192.168.1.176",
    user="root",
    password="password",
    database="laravel"
  )

  mycursor = mydb.cursor()
  ts = time.time()
  timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
  now_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

  query = "SELECT * FROM attendances where user_id='"+str(user[0])+"'"

  mycursor.execute(query)
  myresult = mycursor.fetchall()

  if(not myresult):
    #Not found
    query = "INSERT INTO attendances (user_id,date,status,start_time,end_time) VALUES ('"+str(user[0])+"','"+timestamp+"','1','"+now_time+"','"+now_time+"')"
    mycursor.execute(query)
    mydb.commit()
  else:
    for res in myresult:
      #print(res)
      date_here = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
      date_server = res[2].strftime('%Y-%m-%d')
      if(date_here==date_server):
        query = "UPDATE attendances SET end_time = '"+now_time+"' where id='"+str(res[0])+"'"
        mycursor.execute(query)
        mydb.commit()
        break





def address_match(mac_list):

  print(mac_list[0][3])

  mydb = mysql.connector.connect(
    host="192.168.1.176",
    user="root",
    password="password",
    database="laravel"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT id,mac_address FROM users where mac_address is not NULL")

  myresult = mycursor.fetchall()

  for x in myresult:
    for y in mac_list:
      if(y[3]==x[1]):
        #print('Matched!')
        sendAttendance(x)


