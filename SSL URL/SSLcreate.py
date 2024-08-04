import socket
import ssl

# Create a socket
sock = socket.create_connection(('www.example.com', 443))

# Wrap the socket with SSL
ssl_sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)

# Send a request
ssl_sock.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')

# Receive the response
response = ssl_sock.recv(4096)
print(response.decode())

# Close the connection
ssl_sock.close()
