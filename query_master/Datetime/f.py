def go():
    j = "80 08 00 92 61 6E 13 B0 4B 00 00"
    buf =  j.split(" ")
    buf = [0x80, 0x08, 0x00, 0x92, 0x61, 0x6E, 0x13, 0xB0, 0x4B, 0x00, 0x00]
    
    print(f"crc16 = {hex(CRC_16(buf))}")


def CRC_16(buf):
    crc16_poly = 0x1021
    crc = 0xFFFF
    lenn = len(buf)
    i = 0
    while lenn != 0:
        crc ^= (buf[i] << 8) & 0xFFFF
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ crc16_poly)
            else:
                crc = (crc << 1)
                crc = crc & 0xFFFF
                lenn -= 1
                i += 1
    return crc


if __name__ == '__main__':
    go()
