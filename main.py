import os

#Removing the tabs;
with open("exe3.asm", "r") as f, open("output1.asm", "w") as f2:
	list_lines = f.readlines()

	words = []

	for real_line in list_lines:
		words.append(real_line.strip("	"))
		f2.write(real_line.strip("	"))
	
	f.close()
	f2.close()

#Removing the empty lines;
with open("output1.asm", "r") as f, open("output2.asm", "w") as f2:
	for line in f:
		if not line.strip(): continue
		f2.write(line)

	f.close()
	f2.close()

#Reading the first words of each line, identifying and removing comments, sections and labels, writing in output_commands.asm after processing;
with open("output2.asm", "r") as f, open("output_commands.asm", "w") as f2:
	for line in f:
		first_word = line.split(None, 1)[0]
		if line[0] == "." or line[0] == "#": continue
		if first_word[-1] == ":": continue
		f2.write(first_word+"\n")

	f.close()
	f2.close()

os.remove("output1.asm")
os.remove("output2.asm")