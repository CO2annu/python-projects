import socket
import time
#print(dir(socket))
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #tsp protocol by default
                    #ipaddress , protocol UDP
#finally s is having capability to create UDP socket
target_ip = "127.0.0.1"
target_port = 9999
final_target = (target_ip , target_port)
#taking input form user
while 3>2:
    msg = input("please enter your message:")
    #since python3 is supporting minimum endcoding
    new_msg = msg.encode('ascii')
    #finally lets send data
    s.sendto(new_msg , final_target)
    #lets receive text data
    data = s.recvfrom(100);
    new_data = data[0].decode('ascii')
    print(new_data)
    file_name = data[1][0]
    file_name = file_name + '.txt'
    fp = open(file_name , 'a')
    fp.write(new_data + '\n')
    if new_data.lower() == 'exit':
        break 
    time.sleep(2)
    #creating chat user file or folder
    #dynamic creation of folder
    #open software
    #print(s.recvfrom(100))