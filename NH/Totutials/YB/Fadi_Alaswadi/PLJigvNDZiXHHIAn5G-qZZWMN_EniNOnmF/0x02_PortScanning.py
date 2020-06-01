import socket as socket

host = input("Please enter the IP address: ")


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) # wait 1 sec for the port to respond
    for port in range(1, 1000):
        res = s.connect_ex((host, port)) # return 0 if connect successed
        print("scanning port {} ... ".format(port), end="")
        if(res == 0):
            print("opened")
        else:
            print("closed")
except:
    print("the port is closed")

