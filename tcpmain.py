import socket
# HA = Host Address
# HP = Host Port
HA = "ex: www.google.com OR IP"
HP = ex: 80 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HA,HP))

#send data here 
client.send("")

# Get some data back 
response = client.recv(5000)

print response
