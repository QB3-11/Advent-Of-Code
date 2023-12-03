file = 'input.txt'
sum = 0

with open(file) as input:
	lines = input.readlines()

for line in lines:
	tmp = ''
	for char in line:
		if char.isdigit():
			tmp += char

	sum += int(tmp[0] + tmp[-1])

print(f"The Calibration Value is {sum}")

