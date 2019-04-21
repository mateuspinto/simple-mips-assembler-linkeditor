# change application name here (executable output name)
EXINP=exemplo.asm
EXOUT=exemplo.bin

# interpreter
INTP=python3

# mounter
MONT = mipsMounter.py

all:
	$(INTP) $(MONT) -o $(EXOUT) $(EXINP)

clear:
	rm $(EXOUT)