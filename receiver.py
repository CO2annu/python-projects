import socket
import time
#print(dir(socket))
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #tsp protocol by default
                    #ipaddress , protocol UDP
#finally s is having capability to create UDP socket
my_ip = "127.0.0.1"
my_port = 9999
my_address = (my_ip , my_port)
#lets start above defined address
s.bind(my_address)
#lets receive text data
while 3>2:
  data = s.recvfrom(100)
  new_data = data[0].decode('ascii')
  print(new_data)
  file_name = data[1][0]
  file_name = file_name + '.txt'
  fp = open(file_name , 'a')
  fp.write(new_data + '\n')
  if new_data.lower() == 'exit':
    break 
    #lets receive text data
  new_msg = input("please enter your message")
  new_msg = new_msg.encode('ascii')
  s.sendto(new_msg , data[1])
  time.sleep(2)
    # file handeling
  #  file_name = data[1][0]
    #with open('chat_users/')