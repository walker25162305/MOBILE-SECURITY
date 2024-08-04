from OpenSSL import SSL
import socket

def get_cert_info(hostname, port=443):
    conn = socket.create_connection((hostname, port))
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    ssl_conn = SSL.Connection(context, conn)
    ssl_conn.set_connect_state()
    ssl_conn.do_handshake()
    cert = ssl_conn.get_peer_certificate()
    ssl_conn.close()
    conn.close()
    return cert

cert = get_cert_info('www.example.com')
print(cert.get_subject())
