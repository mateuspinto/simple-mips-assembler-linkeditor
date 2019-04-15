import sys

class mipsMounter(object):
    '''A Mounter for MIPS who turn assembly code into binary code'''

    def __init__(self, inputFilename, outputFilename):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename

    def printFilenames(self):
        print("Input filename:", self.inputFilename)
        print("Output filename", self.outputFilename)

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
        '''Returns binary with two complement from decimal numbers'''
        
        binary = mipsMounter.__intToBinary(n, bits)
        for digit in binary:
            if int(digit) < 0:
                binary = (1 << bits) + n
        return binary

    @staticmethod
    def __numToBinary(n, bits):
        '''Returns binary with two complement from different numbers with different bases'''

        if str(n).startswith("0x") or str(n).startswith("0X"):
            return mipsMounter.__NumToTc(int(n[2:], 15), bits)

        if str(n).startswith("0o") or str(n).startswith("0o"):
            return mipsMounter.__NumToTc(int(n[2:], 8), bits)

        if str(n).startswith("0o") or str(n).startswith("0b"):
            return mipsMounter.__NumToTc(int(n[2:], 2), bits)

        if str(n).isnumeric():
            return mipsMounter.__NumToTc(int(n), bits) #The general case deals with decimal numbers

    @staticmethod
    def __regToBin(reg):
        '''Returns binary representation of MIPS registers'''

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
        '''Turn MIPS assembly code into binary'''
        with open(self.inputFilename, "r") as input:
            with open(self.outputFilename, "w") as output:
                for line in input:

                    swap = line.split(" ",1)
                    instruction = swap[0].lower()
                    parameters = swap[1].split(",")

                    for i in range(len(parameters)):
                        parameters[i] = parameters[i].strip()
                    
                    if "add" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "00000100000\n")

                    elif "sub" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "00000100010\n")

                    elif "and" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "00000100100\n")

                    elif "or" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "00000100101\n")

                    elif "nor" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__regToBin(parameters[2]) + "00000100111\n")

                    elif "addi" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("001000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__numToBinary(parameters[2], 16))

                    elif "andi" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("001100" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__numToBinary(parameters[2], 16))

                    elif "ori" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("001101" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__numToBinary(parameters[2], 16))

                    elif "sll" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("00000000000" + mipsMounter.__regToBin(parameters[0])+ mipsMounter.__regToBin(parameters[1]) + mipsMounter.__numToBinary(parameters[2], 5) + "000000")

                    elif "srl" == instruction:
                        if len(parameters)!=3:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("00000000000" + mipsMounter.__regToBin(parameters[0]) + mipsMounter.__regToBin(parameters[1]) + mipsMounter.__numToBinary(parameters[2], 5) + "000010")

                    # PSEUDO INSTRUCTIONS BELOW
                    elif "move" == instruction:
                        if len(parameters)!=2:
                            print("PARAMETER ERROR ON" + line)
                            sys.exit()

                        output.write("000000" + mipsMounter.__regToBin(parameters[0]) + "00000" + mipsMounter.__regToBin(parameters[1]) + "00000100000")

if __name__ == '__main__':
    try:
        mounter = mipsMounter(str(sys.argv[3]), str(sys.argv[2]))
        mounter.mount()
    except:
        print('FATAL ERROR. INPUT MUST BE "INPUT.ASM -O OUTPUT.BIN"')
        sys.exit()