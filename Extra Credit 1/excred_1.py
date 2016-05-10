def complement(bits):
    convert = [0] * len(bits)
    carryBit = 1

    for i in range(0, len(bits)):
        if bits[i] == '0':
            convert[i] = 1
        else:
            convert[i] = 0


    if convert[-1] == 0:
            convert[-1] = 1
            return ''.join(str(x) for x in convert)

    for bit in range(0, len(bits)):
        if carryBit == 0:
            break
        index = len(bits) - bit - 1
        if convert[index] == 1:
            convert[index] = 0
            carryBit = 1
        else:
            convert[index] = 1
            carryBit = 0

    return ''.join(str(x) for x in convert)
