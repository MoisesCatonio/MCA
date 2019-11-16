#Removing the tabs;
with open("exe3_test.asm", "r") as f, open("output1.asm", "w") as f2:
	list_lines = f.readlines()

	words = []

	for real_line in list_lines:
		words.append(real_line.strip("	"))
		f2.write(real_line.strip("	"))
	
	f.close()
	f2.close()
#Removing the empty lines;
with open("output1.asm", "r") as f, open("output_final.asm", "w") as f2:
	for line in f:
		if not line.strip(): continue
		f2.write(line)

	f.close()
	f2.close()

