file = 'input.txt'
symbols = ('@', '#', '$', '%', '&', '*', '-', '+', '=', '/', '?')
engine = []
sum = 0

with open(file) as data:
	lines = data.readlines()

for line in lines:
	engine.append(list(line))

for i in range(len(engine)):

	num = []
	add = False

	for j in range(len(engine[i])):		

		checks  = {
				i : [ j - 1, j + 1 ],
			 	i + 1 : [ j, j + 1 , j - 1 ],
				i - 1 : [ j, j + 1 , j - 1 ]
			}
 
		if (engine[i][j]).isdigit():

			num.append(engine[i][j])
		
			for y in checks:
				for x in checks[y]:

					try:
						if engine[y][x] in symbols:
							add = True	

					except IndexError:
						pass

		else:
			if add:
				sum += int(''.join(num))
				add = False
			num = []	
print(sum)
