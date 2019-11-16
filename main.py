
f = open("column-major.asm", "r")

total_chars_in_line = []

flines = f.readlines()

for line in flines:
	lenght_of_line = len(line)
	total_chars_in_line.append(lenght_of_line)
	print(line)

f.close()

for lenght in total_chars_in_line:
	print(lenght)

print("")
print("")
print("")

print(len(total_chars_in_line))
