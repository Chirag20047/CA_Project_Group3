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

    output.close()
    binary.close()
    return


if __name__ == '__main__':
    main()
