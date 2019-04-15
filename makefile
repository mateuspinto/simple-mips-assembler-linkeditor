# change application name here (executable output name)
EXINP=fibonnaci.asm
EXOUT=fibonnaci.bin

# interpreter
INTP=python3

# mounter
MONT = mipsMounter.py

all:
	$(INTP) $(MONT) -o $(EXINP) $(EXOUT)