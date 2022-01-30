import binascii
import crc16

g = b'\x80\x08\x00tf\x07\x147\x01\x00\x00\xb5Y'

f = b'\xb5Y'
print(g.hex())

print(f.hex())


def crccitt(hex_string):
    byte_seq = binascii.unhexlify(hex_string)
    crc = crc16.crc16xmodem(byte_seq, 0xffff)
    return '{:04X}'.format(crc & 0xffff)


print(crccitt('8008007466071437010000'))

if f.hex() == crccitt('8008007466071437010000').lower:
    print(True)
