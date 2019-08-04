mateus:
beq $zero, $zero, init
init: addi $t0, $t0, 2
add $t0, $t0, $t0
mult $t0, $t0
mflo $t0
end: j end