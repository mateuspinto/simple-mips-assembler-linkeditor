import sys

class mipsMounter(object):
    '''A Mounter for MIPS who turn assembly code into binary code'''

    def __init__(self, inputFilename, outputFilename):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.labels = []
        self.registers = {"$zero":"00000",
                            "$s0":"10000",
                            "$s1":"10001",
                            "$s2":"10010",
                            "$s3":"10011",
                            "$s4":"10100",
                            "$s5":"10101",
                            "$s6":"10110",
                            "$s7":"10111",
                            "$t0":"01000",
                            "$t1":"01001",
                            "$t2":"01010",
                            "$t3":"01011",
                            "$t4":"01100",
                            "$t5":"01101",
                            "$t6":"01110",
                            "$t7":"01111"}
        self.mounted = []
        self.instructions = {"add":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100000"
        },
        
        "addu":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100001"
        },

        "and":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100100"
        },

        "break":{
            "type":["r"],
            "inputs":[],
            "fn":"001101"
        },

        "div":{
            "type":"r",
            "inputs":["rs","rt"],
            "fn":"011010"
        },

        
        "divu":{
            "type":"r",
            "inputs":["rs","rt"],
            "fn":"011011"
        },

        "mfhi":{
            "type":"r",
            "inputs":["rd"],
            "fn":"010000"
        },

        "mflo":{
            "type":"r",
            "inputs":["rd"],
            "fn":"010010"
        },

        "mthi":{
            "type":"r",
            "inputs":["rs"],
            "fn":"010001"
        },

        "mtlo":{
            "type":"r",
            "inputs":["rs"],
            "fn":"010011"
        },

        "mult":{
            "type":"r",
            "inputs":["rs","rt"],
            "fn":"011000"
        },

        "multu":{
            "type":"r",
            "inputs":["rs","rt"],
            "fn":"011001"
        },

        "nor":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100111"
        },

        "or":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100101"
        },

        "sll":{
            "type":"r",
            "inputs":["rd", "rt","sa"],
            "fn":"000000"
        },

        "sllv":{
            "type":"r",
            "inputs":["rd", "rt", "rs"],
            "fn":"000100"
        },

        "slt":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"101010"
        },

        "sltu":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"101011"
        },

        "sra":{
            "type":"r",
            "inputs":["rd", "rt", "sa"],
            "fn":"000011"
        },

        "srav":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"000111"
        },

        "srl":{
            "type":"r",
            "inputs":["rd","rt","sa"],
            "fn":"000010"
        },

        "srlv":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"000110"
        },

        "sub":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100010"
        },

        "subu":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"100011"
        },

        "syscall":{
            "type":"r",
            "inputs":[],
            "fn":"001100"
        },

        "xor":{
            "type":"r",
            "inputs":["rd", "rs", "rt"],
            "fn":"001100"
        }
        
        
        }

    def printFilenames(self):
        print("Input filename: ", self.inputFilename)
        print("Output filename: ", self.outputFilename)

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

        if str(n).startswith("0o") or str(n).startswith("0O"):
            return mipsMounter.__NumToTc(int(n[2:], 8), bits)

        if str(n).startswith("0B") or str(n).startswith("0b"):
            return mipsMounter.__NumToTc(int(n[2:], 2), bits)

        if str(n).replace("-", "").isnumeric():
            return mipsMounter.__NumToTc(int(n), bits) #The general case deals with decimal numbers

    def __insertLabelReturnBinary(self, newLabel):
        '''Try to find the index of an assembly label. If it not exists, create a new one'''
        try:
            return mipsMounter.__intToBinary(self.labels.index(newLabel), 16)
        except:
            self.labels.append(newLabel)
            return mipsMounter.__intToBinary(self.labels.index(newLabel), 16)

    @staticmethod
    def __lineError(line):
        print("PARAMETER ERROR ON " + line)
        sys.exit()

    def mount(self):
        '''Turn MIPS assembly code into binary'''

        self.labels=[]

        with open(self.inputFilename, "r") as input:
            with open(self.outputFilename, "w") as output:
                for line in input:

                    if (line.startswith("#") or line.isspace()): #Ignore fullline comments or blank lines
                        pass

                    else: # Flow goes here when the line is a MIPS command

                        line = (line.split("#",1))[0] #ignore inline comments

                        swap = line.split(":")
                        if len(swap) == 2:
                            label = swap[0].strip() + ":"
                            swap = swap[1]
                        elif len(swap) == 1:
                            label = ""
                            swap = swap[0]
                        else:
                            self._mipsMounter__lineError

                        swap = swap.split(" ",1)
                        instruction = swap[0].lower().strip()
                        parameters = swap[1].split(",")

                        # remove all parameters spaces Ex: "  $s0" turns into "$s0"
                        for i in range(len(parameters)):
                            parameters[i] = parameters[i].strip()
                        
                        if(instruction in self.instructions):
                            self.mounted.append(label)

                            if(self.instructions[instruction]["type"] == "r"):

                                opcode = "000000"
                                rd = "00000"
                                rs = "00000"
                                rt = "00000"
                                shamt = "00000"
                                fn = "000000"

                                if(len(self.instructions[instruction]["inputs"]) != len(parameters)):
                                    self._mipsMounter__lineError(line)
                                    
                                for input_number, input_name in enumerate(self.instructions[instruction]["inputs"]):

                                    if input_name == "rs":
                                        rs = self.registers[parameters[input_number]]
                                    elif input_name == "rd":
                                        rd = self.registers[parameters[input_number]]
                                    elif input_name == "rt":
                                        rt = self.registers[parameters[input_number]]
                                    elif input_name == "sa":
                                        shamt = mipsMounter.__numToBinary(parameters[input_number], 5)

                                fn = self.instructions[instruction]["fn"]

                                self.mounted[len(self.mounted)-1] += (opcode + rd + rs + rt + shamt + fn)

                            elif(self.instructions[instruction]["type"] == "i"):
                                pass

                            elif(self.instructions[instruction]["type"] == "j"):
                                pass
                        
                        else:
                            self._mipsMounter__lineError(line)

# if __name__ == '__main__':
#     try:
#         mounter = mipsMounter(str(sys.argv[3]), str(sys.argv[2]))
#         mounter.mount()
#     except:
#         print('FATAL ERROR. INPUT MUST BE "INPUT.ASM -O OUTPUT.BIN"')
#         sys.exit()

mounter = mipsMounter("exemplo.asm", "exemplo.bin")
mounter.mount()