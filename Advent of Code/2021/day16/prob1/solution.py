import math
from dataclasses import dataclass

@dataclass
class Abstract_Packet():
    version: int
    packetType: int

@dataclass
class Literal_Packet(Abstract_Packet):
    value: int

@dataclass
class Operator_Packet(Abstract_Packet):
    subs: list[Abstract_Packet]

def hex_to_binary(h):
    out = ""
    for digit in h:
        if digit.isnumeric():
            bi = decimal_to_binary(int(digit))
        else:
            bi = decimal_to_binary(ord(digit) - 55)
        for i in range(4-len(bi)):
            out += "0"
        out += bi
    return out

def decimal_to_binary(d):
    if d == 0:
        return "0"
    if d == 1:
        return "1"

    out = ""
    for power in range(math.floor(math.log(d, 2)), -1, -1):
        place = 2**power
        if place <= d:
            out += "1"
            d -= place
        else:
            out += "0"
    assert d == 0
    return out

def binary_to_decimal(b):
    out = 0
    for i, digit in enumerate(b[::-1]):
        if digit == "1":
            out += 2**i
    return out


def get_packets(infile):
    with open(infile) as f:
        data = f.read().strip()
    return hex_to_binary(data)

def parse_packets(packetData):
    if len(packetData) == 0 or packetData == "0"*len(packetData):
        return []
    packetType = binary_to_decimal(packetData[3:6])
    if packetType == 4:
        return parse_literal_packet(packetData)
    else:
        return parse_operator_packet(packetData)

def parse_literal_packet(packetData):
    version = binary_to_decimal(packetData[0:3])
    packetType = binary_to_decimal(packetData[3:6])

    binaryValue = ""
    valueIndex = 6
    valueEnd = False
    while not valueEnd:
        binaryValue += packetData[valueIndex+1:valueIndex+5]
        valueEnd = (packetData[valueIndex] == "0")
        valueIndex += 5
    value = binary_to_decimal(binaryValue)
    nextIndex = valueIndex
    packet = Literal_Packet(version, packetType, value)
    remainingPackets = packetData[nextIndex:]
    

    return [packet] + parse_packets(remainingPackets)

def parse_operator_packet(packetData):
    version = binary_to_decimal(packetData[0:3])
    packetType = binary_to_decimal(packetData[3:6])
    lengthTypeID = packetData[6]

    #count internal packets by size (15 bit number of bits)
    if lengthTypeID == "0":
        numBits = binary_to_decimal(packetData[7:22])
        internalPackets = parse_packets(packetData[22:22+numBits])

        packet = Operator_Packet(version, packetType, internalPackets)
        remainingPackets = packetData[22+numBits:]
        return [packet] + parse_packets(remainingPackets)

    #count internal packets by the number of packets
    else:
        numPackets = binary_to_decimal(packetData[7:18])
        allRemainingPackets = packetData[18:]
        parsedPackets = parse_packets(allRemainingPackets)
        internalPackets = parsedPackets[0:numPackets]
        remainingParsedPackets = parsedPackets[numPackets:]
        packet = Operator_Packet(version, packetType, internalPackets)
        return [packet] + remainingParsedPackets

def sum_versions(packets):
    versionSum = 0
    for packet in packets:
        versionSum += packet.version
        if type(packet) == Operator_Packet:
            versionSum += sum_versions(packet.subs)
    return versionSum

def main():
    infile = "input.txt"
    packetData = get_packets(infile)
    packets = parse_packets(packetData)
    print(sum_versions(packets))

if __name__ == "__main__":
    main()

        




