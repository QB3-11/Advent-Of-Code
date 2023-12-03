file = 'input.txt'
sum = 0
nums = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

with open(file) as input:
	lines = input.readlines()

for line in lines:
	tmp = []

	for index, ch in enumerate(line):
		
		if ch.isdigit():
			tmp.append(ch)
		
		else:
			for number, word in enumerate(nums):
				if line[index:].startswith(word):
					tmp.append(str(number+1))

	sum += int(tmp[0] + tmp[-1])
print(sum)
