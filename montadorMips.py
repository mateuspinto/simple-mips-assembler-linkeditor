import sys

class mipsMounter(object):

    def __init__(self, inputFilename, outputFilename):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename

    def printFilenames(self):
        print("Arquivo de entrada:", self.inputFilename)
        print("Arquivo de saída:", self.outputFilename)

    @staticmethod
    def __intToBinary(n, bits):
        '''Returns the string with the binary representation of non-negative integer n.'''
        result = ''  
        for x in range(bits):
            r = n % 2 
            n = n // 2
            result += str(r)

        result = result[::-1]
        return result

    @staticmethod
    def __NumToTc(n, bits):
        '''Returns the string with the binary representation of non-negative integer n.'''
        binary = mipsMounter.__intToBinary(n, bits)
        for digit in binary:
            if int(digit) < 0:
                binary = (1 << bits) + n
        return binary

    @staticmethod
    def __numToBinary(n, bits):
        return mipsMounter.__NumToTc(int(n), bits)

    @staticmethod
    def __regToBin(reg):
        if reg=="$zero":
            return "00000"
        elif reg[1]=="s":
            index = int(reg[2:])
            if 0<=index<=7:
                return mipsMounter.__numToBinary(int(reg[2:]) + 16, 5)
        elif reg[1]=="t":
            index = int(reg[2:])
            if 0<=index<=7:
                return mipsMounter.__numToBinary(int(reg[2:]) + 8, 5)

    def mount(self):
        with open(self.inputFilename, "r") as input:
            with open(self.outputFilename, "w") as output:
                for line in input:

                    swap = line.split(" ",1)
                    instruction = swap[0].lower()
                    parameters = swap[1].split(",")

                    for i in range(len(parameters)):
                        parameters[i] = parameters[i].strip()
                    
                    if "add" == instruction:
                        if len(parameters)!=3: #COLOCAR O PRINT AQUI
                            sys.exit()

                        print("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "100000")
                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "100000\n")

a=mipsMounter("fibonnaci.asm", "fibonnaci.bin")
a.mount()