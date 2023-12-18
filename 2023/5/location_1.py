file = 'input.txt'
demo_file = 'demo.txt'
seeds = []
values = []

with open(demo_file) as input:
	almanac = input.readlines()

for seed in almanac[0].split(':')[-1].split():
	seeds.append(int(seed))

for line in almanac:
	
	if line == '\n' or  not line[0].isdigit():
		continue

	else:
		values = [int(val) for val in line.split()]
		desti_range = values[0]
		source_range = values[1]
		range_length = values[2]		
				
		for index, seed in enumerate(seeds):

			if source_range + range_length > seed and seed >= source_range:
				seeds[index] += desti_range - source_range 
				print(seeds)

print(min(seeds))
					
