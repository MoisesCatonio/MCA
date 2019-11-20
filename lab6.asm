	.data
str1:	.asciiz "Resultado: "
str2:	.asciiz "Digite o primeiro numero: "
str3:	.asciiz "Digite o segundo numero: "
	.text
	.globl main

main:
	#Imprimir str2
	li $v0, 4
	la $a0, str2
	syscall
	
	#receber o numero do terminal
	li $v0, 5
	syscall
	move $t0, $v0
	
	#Imprimir str3
	li $v0, 4
	la $a0, str3
	syscall
	
	#receber o numero do terminal
	li $v0, 5
	syscall
	move $t1, $v0
	
	slt $s0, $t0, $t1
	beq $s0, $zero, else
	addi $t0, $t0, 4
	j end
	
else:
	addi $t0, $t0, 5
	
end: 
	#Imprimir str1
	li $v0, 4
	la $a0, str1
	syscall

	#Imprimir int
	li $v0, 1
	move $a0, $t0
	syscall
	
	li $v0, 10
	syscall
