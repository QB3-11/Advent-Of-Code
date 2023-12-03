file = 'input.txt'
sum = 0

balls = {'red':12, 'green':13, 'blue':14}

with open(file) as input:
	lines = input.readlines()

for line in lines:
	words = line.replace(';', '').replace(',', '').split()
	for index, word in enumerate(words):
		if index > 1:

			if index % 2 == 0:
				if int(word) > balls[words[index+1]]:
					break
	
	else:
		sum +=  int(words[1].replace(':', ''))
	
print(sum)


		


