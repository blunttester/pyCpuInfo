import socket

s = socket.socket()
s.connect(('127.0.0.1', 7878))

def get_file(s, file_name):
    cmd = 'get\n%s\n' % (file_name)
    s.sendall(cmd)
    r = s.recv(2)
    size = int(s.recv(16))
    recvd = ''
    while size > len(recvd):
        data = s.recv(1024)
        if not data: 
            break
        recvd += data
    s.sendall('ok')
    return recvd

print get_file(s, './toplog')
##print get_file(s, 'file2')
s.sendall('end\n')