import random
import random as rand


class Clock:
    def __init__(self, count):
        self.counter = count

    def getCounter(self):
        return self.counter


class CPU:
    def __init__(self, clock):
        self.counter = clock


class InstructionMemory:
    def __init__(self, clock):
        self.counter = clock
        self.instructions = list()


class DataMemory:
    def __init__(self, clock):
        self.counter = clock


class PipeLine:
    def __init__(self):
        pass


class RegisterFile:
    def __init__(self):
        self.program_counter = 0  # Initial State
        self.r0 = (0,)  # Immutable Special Register
        self.registers = list()
        for i in range(1, 32):
            number = random.randint(-100, 100)
            self.registers.append(number)  # Initializing the register file


def main():
    binary = open('testBinary.txt', 'r')
    output = open('logFile.txt', 'w')
    clock = Clock(0)    # Clock obj starting from 0
    while True:
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
        #     :
        #     :
        # Display the register file
        # clock += 1

        pass

    output.close()
    binary.close()
    return


if __name__ == '__main__':
    main()
