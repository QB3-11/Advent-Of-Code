file = 'input.txt'
sum = 0

with open(file) as input:
	lines = input.readlines()

for line in lines:
	words = line.replace(';', '').replace(',', '').split()
	balls = {'red':0, 'blue':0, 'green':0}

	for index, word in enumerate(words):
		if index > 1:

			if index % 2 == 0:
				color = words[index + 1]
				if int(word) > balls[color]:
					balls[color] = int(word)
	
	sum += ( balls['red'] * balls['green'] * balls['blue'])

print(sum)
