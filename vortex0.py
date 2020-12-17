import socket
import binascii
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("vortex.labs.overthewire.org", 5842))
a = s.recv(16)
print(binascii.hexlify(a))
ints = [0, 0, 0, 0]
for i in range(4):
    for j in range(4):
        ints[i] += (a[i * 4 + j] << (j * 8))
res = sum(ints)
print(ints, res, "%08x" % res)
res = struct.pack('<Q', res)
print(res)
s.send(res[:4])
print(s.recv(10000))
s.close()
