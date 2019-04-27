add $s0, $zero, $s0
sub $s1, $zero, $s1
addi $s2, $zero, 8
move $s0, $s0
and $s1, $s0, $s0
andi $s1, $s0, 0xee
or $s1, $s0, $s0
ori $s1, $s0, 0o76
sll $s1, $s0, 16
srl $s1, $s0, 16
beq $s2, $s3, mateus
# fulline comment
#dasd
beq $s2, $s3, leandro
bne $s2, $s3, mateus # inline comment
add $s2, $s0, $s1
sll $t1, $s2, 2 
or $t2, $s2, $s1
andi $t2, $t1, 16
addi $t3, $t2, -243




# asdaun