import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# this might be database or a file
di ={'17BIT0382': 'K9v!r@Pz',
    '17BEC0647': 'fY3#Lm8w',
    '17BEC0150': 'R!2zMe$1',
    '17BCE2119': 'dT@5uQ#v',
    '17BIT0123': 'X6!pNz0&' }

while(True):
	name, addr1 = UDPServerSocket.recvfrom(bufferSize) 
	# receiving pwd from client
	pwd, addr1 = UDPServerSocket.recvfrom(bufferSize) 
	
	name = name.decode() 
	pwd = pwd.decode()
	msg =''
	
	if name not in di:
		msg ='İsim mevcut değil !'
		flag = 0
	
	for i in di:
		if i == name:
			if di[i]== pwd:
				msg ="Şifre Doğru"
				flag = 1
			else:
				msg ="Şifre Yanlış"
		
		bytesToSend = str.encode(msg)
	  # sending encoded status of name and pwd
		UDPServerSocket.sendto(bytesToSend, addr1) 
