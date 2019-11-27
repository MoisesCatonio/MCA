import os

name = raw_input("Insira o nome do arquivo: ")

file_name = name+".asm"

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
	print(commands_dict)

os.remove("output1.txt")
os.remove("output2.txt")