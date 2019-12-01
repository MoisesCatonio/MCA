import os
import math

#For reading the archive;
name = input("Insira o nome do arquivo sem a sua extensão (ex: lab6): ")

#listing the possible types;
list_of_possible_types = ["arithmetic_or_logic", "memory_read", "memory_write", "conditional_jump", "unconditional_jump", "not_documented"]

#identifying the command types in a dict;
command_types = {"add": "arithmetic_or_logic", "sub": "arithmetic_or_logic", 
"addi": "arithmetic_or_logic", "mult": "arithmetic_or_logic", "div": "arithmetic_or_logic", 
"and": "arithmetic_or_logic", "or": "arithmetic_or_logic", "xor": "arithmetic_or_logic", 
"mfhi": "memory_read", "mflo": "memory_read", "sll": "arithmetic_or_logic", "srl": "arithmetic_or_logic",
"slt": "arithmetic_or_logic", "bne": "conditional_jump", "beq": "conditional_jump", "bne": "conditional_jump", 
"lw": "memory_read", "sw": "memory_write", "j": "unconditional_jump", "jr": "unconditional_jump"}

file_name = name+".asm"
print("\n")

#Removing the tabs;
with open(file_name, "r") as f, open("output1.txt", "w") as f2:
	list_lines = f.readlines()

	words = []

	for real_line in list_lines:
		words.append(real_line.strip("	"))
		f2.write(real_line.strip("	"))
	
	f.close()
	f2.close()

#Removing the empty lines;
with open("output1.txt", "r") as f, open("output2.txt", "w") as f2:
	for line in f:
		if not line.strip(): continue
		f2.write(line)

	f.close()
	f2.close()

#Reading the first words of each line, identifying and removing comments, sections and labels, writing in output_commands.asm after processing;
with open("output2.txt", "r") as f, open("output_commands.txt", "w") as f2:
	for line in f:
		first_word = line.split(None, 1)[0]
		if line[0] == "." or line[0] == "#": continue
		if first_word[-1] == ":": continue
		f2.write(first_word+"\n")

	f.close()
	f2.close()

#getting rid of unused archives;
os.remove("output1.txt")
os.remove("output2.txt")

#Generating a list and a set with the commands found;
with open("output_commands.txt", "r") as commands:
	list_of_commands = commands.read().splitlines()
	commands_dict = dict()
	for command in list_of_commands:
		if command in commands_dict.keys():
			commands_dict[command] += 1
		else:
			commands_dict[command] = 1
	commands.close()
	print("Comandos gerais utilizados: \n")
	
	for key in commands_dict:
		print(key+": "+str(commands_dict[key]))
	total_commands = sum(commands_dict.values())
	total_commands_str = str(total_commands)
	print("")


	print("totalizando "+total_commands_str+ " comandos.")

print("\n")

#list to receive the ocurrences of each type;
list_of_types = []

#analyzing the values and adding the values;
for item in list_of_commands:
	if(item in command_types):
		list_of_types.append(command_types[item])
	else:
		list_of_types.append("not_documented")

#turning the results of the previous list in dict counting the ocurrences;
dict_of_types = {}

for item in list_of_types:
	if item in dict_of_types.keys():
		dict_of_types[item] += 1
	else:
		dict_of_types[item] = 1 

#creating the function to read and atribute the values;
def count_percentage(some_dict):
	
	total = sum(some_dict.values())
	one_percent = (total/100)

	for key in some_dict:
		print(key+" com "+str(some_dict[key]) + " ocorrências.")
		print("\n")
		some_dict[key] = ("%.2f"%(some_dict[key]/one_percent))

count_percentage(dict_of_types)

#Final percentage exibition.
print("\n")
print("Porcentagens totais de participação relacionadas ao programa: \n")

for item in list_of_possible_types:
	if item in dict_of_types:
		print(item+": "+str(dict_of_types[item])+"% \n")
	else:
		print(item+": "+"0% \n")	