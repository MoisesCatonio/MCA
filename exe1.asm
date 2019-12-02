main:
	addi $s1, $s1, 1
	addi $s2, $s2, 2
	addi $s3, $s3, 3
	addi $v0, 4
	sll $a0, $t0, $t1
	lw $t3, 1024($t9)
	
LOOP:	

	beq $t0, $zero, case0
	beq $t0, $s1, 	case1
	beq $t0, $s2, 	case2
	beq $t0, $s3, 	case3
	slt $t2, $t0, $s2
	beq $t2, $t1, FORA 
	slt $t3, $s0, $t0
	beq $t3, $t1, FORA
	bne  $s4, $t1, EXIT
	addi $s1, $s1, 1 
	addi $s2, $s2, 2 
	add $t2, $s3, $s2
	add $s3, $t2, $t1
	
	slt $s5, $t0, $s3 # x < s
	beq $s5, $t1, EXIT
	addi $s4, $s4, 1
	j LOOP


DENTRO:
	addi $s1, $s1, 1
	j EXIT 
	
FORA:
	addi $s1, $s1, 0
	j EXIT 

	

case0: 
	add $s0, $t1, $t2
	j EXIT

case1: 
	add $s0, $t3, $t4
	j EXIT

case2: 
	sub $s0, $t3, $t4
	j EXIT

case3: 
	sub $s0, $t1, $t4
	j EXIT
	
EXIT:
	addi $v0, $v0, 4
	add $a0, $zero, $s0
	sw $a0, 64($t0)
	addi $v0, $v0, 10

