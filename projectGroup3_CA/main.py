import random
import random as rand


def BTD(binary):  # Converts a given binary string (32 bits) to decimal integer (base 10)
    binary = binary[::-1]
    num = 0
    for i in range(31):
        if binary[i] == '1':
            num = num + pow(2, i)
    binary = binary[::-1]
    if binary[0] == '1':
        num = num + (pow(2, 31) * -1)
    return num


def reverse(x):
    return x[::-1]


def DTB(num):  # Converts a given integer(base 10) to binary string of 32
    string = ''
    flag = False  # false --> positive number
    if num < 0:
        flag = True  # Negative Number
    num = abs(num)
    while num != 0:
        remainder = num % 2
        string = string + str(remainder)
        num = num // 2
    string = string[::-1]
    length = len(string)
    added = "0" * (32 - length)
    number = added + string
    #    Taking 1's complement of the given binary string
    if flag:
        for i in range(32):
            if number[i] == '1':
                number = number[:i] + '0' + number[i + 1:]
            else:
                number = number[:i] + '1' + number[i + 1:]
        # Adding 1 to the given number
        carry = 0
        # number = number[::-1]
        for i in range(31, -1, -1):
            if number[i] == '1':
                number = number[:i] + '0' + number[i + 1:]
                carry = 1
            else:
                number = number[:i] + '1' + number[i + 1:]
                break
    return number


class Clock:
    def __init__(self, count):
        self.counter = count

    def getCounter(self):
        return self.counter


class CPU:
    def __init__(self):
        self.clock = Clock(0)
        self.registerFile = list()
        initialValue = "0" * 32
        self.program_counter = initialValue  # Initial State
        self.r0 = (initialValue,)  # Immutable Special Register : tuple has been used
        self.registers = list()
        for i in range(31):
            self.registers.append(initialValue)


class InstructionMemory:
    def __init__(self):  # Constructor for instructionMemory
        self.instructions = list()

    def loadProgram(self, file):  # Loading the complete program in instruction Memory Obj: data member
        for row in file:
            temp = row.strip()
            self.instructions.append(temp)
        return


class DataMemory:
    def __init__(self):  # Constructor
        self.memory = dict()  # Initializing the Dictionary

    def initializeMemory(self):  # Initializing Memory with all 0
        initialValue = "0" * 32  # initial Value of each of the memory locations
        for i in range(1000):  # Number of different memory locations : 1000 (starting from 0)
            addr = DTB(i)  # address of the memory location
            self.memory[addr] = initialValue


class Fetch:
    def __init__(self):
        self.instruction = ""
        pass

    def FetchInstruction(self, instruction):  # Setting the instruction
        self.instruction = instruction


class Decode:
    def __init__(self):
        self.busy = False
        self.result = list()
        pass

    def DecodeInstruction(self, binary):  # decoding the binary instruction fetched from the
        self.busy = True
        imm = 0
        rs1 = 0
        rs2 = 0
        rd = 0
        type = ""
        binary = reverse(binary)
        if binary[0:7] == "1100110" and binary[12:15] == "000" and binary[25:] == "0000000":
            type = "add"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100110" and binary[12:15] == "000" and binary[25:] == "0000010":
            type = "sub"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100110" and binary[12:15] == "111" and binary[25:] == "0000000":
            type = "and"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100110" and binary[12:15] == "011" and binary[25:] == "0000000":
            type = "or"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100110" and binary[12:15] == "100" and binary[25:] == "0000000":
            type = "sll"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100110" and binary[12:15] == "101" and binary[25:] == "0000010":
            type = "sra"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            result = [type, rd, rs1, rs2]

        elif binary[0:7] == "1100100" and binary[12:15] == "000":
            type = "addi"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            imm = BTD(reverse(binary[20:]))
            result = [type, rd, rs1, imm]

        elif binary[0:7] == "1100000" and binary[12:15] == "010":
            type = "lw"
            rd = BTD(reverse(binary[7:12]))
            rs1 = BTD(reverse(binary[15:20]))
            imm = BTD(reverse(binary[20:]))
            result = [type, rd, rs1, imm]

        elif binary[0:7] == "1100011" and binary[12:15] == "000":
            type = "beq"
            imm1 = reverse(binary[7:12])
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            imm2 = reverse(binary[25:])
            imm = BTD(imm2 + imm1)
            result = [type, rs1, rs2, imm]

        elif binary[0:7] == "1100010" and binary[12:15] == "010":
            type = "sw"
            imm1 = reverse(binary[7:12])
            rs1 = BTD(reverse(binary[15:20]))
            rs2 = BTD(reverse(binary[20:25]))
            imm2 = reverse(binary[25:])
            imm = BTD(imm2 + imm1)
            result = [type, rs1, rs2, imm]
        # Remember to unset the flag busy on completing the work , busyFlag : regarding the structural hazard stalling
        return result


class Xecute:
    def __init__(self):
        self.busy = False  # Used for checking stalling logics
        self.result = None  # Until no value is being assigned

    def Add(self, signals, CpuObject):
        # signals = [type,rd,rs1,rs2] :  we have to add rs1 and rs2 in this function
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 + val2

    def Sub(self, signals, CpuObject):
        # signals = [type,rd,rs1,rs2] :  we have to add rs1 and rs2 in this function
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 - val2

    def AND(self, signals, CpuObject):
        # signals = [type,rd,rs1,rs2] :  we have to add rs1 and rs2 in this function
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 and val2

    def OR(self, signals, CpuObject):
        # signals = [type,rd,rs1,rs2] :  we have to add rs1 and rs2 in this function
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 or val2

    def AddImm(self, signals, CpuObject):
        # signals = [type,rd,rs1,imm] :  we have to add rs1 and rs2 in this function
        val1 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        imm = signals[3]
        self.result = val1 + imm

    def SLL(self, signals, CpuObject):
        # signals = [type, rd, rs1, rs2]
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 << val2

    def SRA(self, signals, CpuObject):
        # signals = [type, rd, rs1, rs2]
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        self.result = val1 >> val2

    def LoadWord(self):
        # Nothing has to be done here
        pass

    def StoreWord(self):
        # Nothing has to be done here
        pass

    def BranchIfEqual(self, signals, CpuObject):
        # signals = [type, rs1, rs2, imm]
        val1 = 0
        val2 = 0
        if signals[2] > 0:  # Not register x0
            val1 = BTD(CpuObject.registers[signals[2] - 1])
        if signals[3] > 0:  # Not register x0
            val2 = BTD(CpuObject.registers[signals[3] - 1])
        result = val1 == val2
        if result:
            CpuObject.program_counter = CpuObject.program_counter + signals[3]
            # AFTER THIS KILL ALL INSTRUCTIONS



class Memory:
    def __init__(self):
        self.busy = False

    def loadWord(self, signals, data):
        addr = ''  # memory (binary)
        register = ' '  # register number
        pass

    def storeWord(self, signals, data):
        addr = ''  # memory (binary)
        valueTobeStores = -1
        pass


class WriteBack:
    def __init__(self):
        self.busy = False


def main():
    #  Opening the input and log Files
    binary = open('testBinary.txt', 'r')
    # output = open('logFile.txt', 'w')

    # Instantiating the objects of the System
    cpuObject = CPU()
    instMem = InstructionMemory()
    dataMem = DataMemory()
    fetch = Fetch()
    decode = Decode()
    execute = Xecute()
    sysMem = Memory()
    write_back = WriteBack()

    # Loading the program in the instruction memory & data memory
    instMem.loadProgram(binary)
    dataMem.initializeMemory()

    # Main Logic of the code

    binary.close()
    print(dataMem.memory)
    # output.close()
    return


if __name__ == '__main__':
    main()
