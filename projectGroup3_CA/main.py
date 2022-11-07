import random
import random as rand


def BTD(s):
    a = int(s, 2)
    return a


def DTB(num):
    string = ''
    while num != 0:
        remainder = num % 2
        string = string + str(remainder)
        num = num // 2
    string = string[::-1]
    length = len(string)
    added = "0" * (32 - length)
    return added + string


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
        pass


class Decode:
    def __init__(self):
        pass


class Xecute:
    def __init__(self):
        pass


class Memory:
    def __init__(self):
        pass


class WriteBack:
    def __init__(self):
        pass


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
    print(instMem.instructions)
    # while True:
    # all 5 stages manipulated
    # Fetch: instruction from instructionMemory obj
    # Decode :  extract useful group of bits from the fetched instruction
    # Xecute : execute and store the arithmetic operations in a temp variable
    # Memory : load or store instruction manipulation
    # WriteBack : update register file
    # PTR :
    # 1) Each stage object will converse with prev stage object .
    # 2) Each stage object will converse with next stage as well : to avoid structural hazard
    #     : use of flag (busy)
    # 3) Data Hazard : RAW WAR WAW [TO BE DECIDED !!!]
    #     : current stage destination register should not clash with prev
    # Display the register file
    # cpuObject.clock = cpuObject.clock + 1  # Updating the Clock Cycle Number
    # pass

    # Closing the opened files
    output.close()
    binary.close()
    return


if __name__ == '__main__':
    main()
