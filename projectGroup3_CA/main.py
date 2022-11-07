import random
import random as rand


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
        for i in range(32):
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
        self.busy = False       # flag busy : used for checking whether a structural hazard exists or not
        self.instruction = ""
        pass

    def SetInstruction(self, instruction):  # Setting the instruction
        self.instruction = instruction
        self.busy = True

    def CheckBusy(self):
        return self.busy


class Decode:
    def __init__(self):
        self.busy = False
        pass


class Xecute:
    def __init__(self):
        self.busy = False


class Memory:
    def __init__(self):
        self.busy = False


class WriteBack:
    def __init__(self):
        self.busy = False


def main():
    #  Opening the input and log Files
    binary = open('testBinary.txt', 'r')
    output = open('logFile.txt', 'w')

    # Instantiating the objects of the System
    cpuObject = CPU()
    instMem = InstructionMemory()
    dataMem = DataMemory()
    fetch = Fetch()
    decode = Decode()
    execute = Xecute()
    sysMem = Memory()
    write_back = WriteBack()

    # Loading the program in the instruction memory
    instMem.loadProgram(binary)
    # print(instMem.instructions)

    # Main Logic of the code


    output.close()
    binary.close()
    return


if __name__ == '__main__':
    main()
