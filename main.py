import os

#For reading the archive;
name = input("Insira o nome do arquivo sem a sua extensão: ")

#Lis of all commands;
#list_of_possible_inst = ["add", "sub", "addi", "mult", "div", "and", "or", "xor", "mfhi", "mflo", "sll", "srl", "slt", "bne", "beq", "lw", "sw", "j", "jr"] 

#Break into labeled/named lists;
#memory_read_inst = ["lw", "mfhi", "mflo"]
#memory_write_inst = ["sw"]
#conditional_jump_inst = ["bne", "beq"]
#unconditional_jump_inst = ["j", "jr"]
#arithmetic_and_logic_inst = ["and", "or", "xor", "sll", "srl", "slt", "sub", "mult", "div", "add", "addi"]
#registers_used = []

#unregistered_inst = []

#command_types = {"memory_read": memory_read_inst, "memory_write": memory_write_inst, "conditional_jump": conditional_jump_inst, "unconditional_jump": unconditional_jump_inst, "arithmetic_and_logic": arithmetic_and_logic_inst}

command_types = {"add": "arithmetic_or_logic", "sub": "arithmetic_or_logic", 
"addi": "arithmetic_or_logic", "mult": "arithmetic_or_logic", "div": "arithmetic_or_logic", 
"and": "arithmetic_or_logic", "or": "arithmetic_or_logic", "xor": "arithmetic_or_logic", 
"mfhi": "memory_read", "mflo": "memory_read", "sll": "arithmetic_or_logic", "srl": "arithmetic_or_logic",
"slt": "arithmetic_or_logic", "bne": "conditional_jump", "beq""bne": "conditional_jump", 
"lw": "memory_read", "sw": "memory_write", "j": "unconditional_jump", "jr": "unconditional_jump"}

file_name = name+".asm"
print("")

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
	print("Comandos gerais: \n")
	
	for key in commands_dict:
		print(key+": "+str(commands_dict[key]))
	total_commands = sum(commands_dict.values())
	total_commands_str = str(total_commands)
	print("")


	print("totalizando "+total_commands_str+ " comandos.")

#list to receive the ocurrences of each type;
list_of_types = []

for item in list_of_commands:
	if(item in command_types):
		list_of_types.append(command_types[item])
	else:
		list_of_types.append("not_documented")


os.remove("output1.txt")
os.remove("output2.txt")