f1 = open("unfiltered_table.txt","r")
f2 = open("filtered_table.txt","w")

Line1 = f1.readlines()

for line in Line1:
	if line.find("|- class=") == -1:
		i = 0
		phrase = ""
		while i < len(line) :
			if line[i] == "{":
				start = i
				word = ""
				for j in range(i+1, len(line)):
					if line[j] == "}" and line[j-1] == "}":
						end = j 
						break

				middle = line[i:j].find("|")
				k = 1
				while line[i:j][middle + k] != "}":
					word += line[i:j][middle + k]
					k += 1 

				phrase += word
				i = j

			else:
				phrase += line[i]
			i += 1
		f2.write(phrase)

	else:
		f2.write(line)
		
	
f1.close()
f2.close()