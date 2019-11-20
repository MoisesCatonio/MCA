	.data

	.text
	.globl main

main:
	addi $s0, $s0, 0 #inicializando i com 0
	addi $t1, $t1, 10 #inicializando aux com 10
	beq $s0, $t1, end
		
loop:
	addi $s0, $s0, 1
	bne $s0, $t1, loop
	
end: 
	li $v0, 10
	syscall
