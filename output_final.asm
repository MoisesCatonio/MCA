.data 
x:	.asciiz "Digite x: "
r:	.asciiz "Raiz: "
.text	
.globl main 
main:
#Imprimir x
li $v0, 4
la $a0, x
syscall
li $v0, 5 
syscall
move $t0, $v0
li $s1, 1 #r
li $s2, 2 #d
li $s3, 4 #s
li $s4, 1 #t
li $t1, 1 #aux
LOOP:	
bne  $s4, $t1, EXIT
addi $s1, $s1, 1    #r+1
addi $s2, $s2, 2    #d+2
add $t2, $s3, $s2   #s+d
add $s3, $t2, $t1   #s+d+1
slt $s5, $t0, $s3 # x < s
beq $s5, $t1, EXIT
li $s4, 1
j LOOP
EXIT:
#Imprimir r
li $v0, 4
la $a0, r
syscall
li $v0, 1
move $a0, $s1 
syscall
li $v0, 10 
syscall
