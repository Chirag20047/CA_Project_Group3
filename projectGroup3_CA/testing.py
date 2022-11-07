def BTD(binary):         # Converts a given binary string (32 bits) to decimal integer (base 10)
    binary = binary[::-1]
    num = 0
    for i in range(31):
        if binary[i] == '1':
            num = num + pow(2, i)
    binary = binary[::-1]
    if binary[0] == '1':
        num = num + (pow(2, 31)*-1)
    return num