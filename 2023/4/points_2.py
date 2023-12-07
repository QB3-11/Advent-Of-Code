file = 'input.txt'
demo_file = 'demo.txt'
cards = {1:1}
sum = 0

with open(file) as input:
	scratch_cards = input.readlines()


for card in scratch_cards:
	
	cnt = 0 
	parts = card.split('|')
	card_num = int(parts[0].split(':')[0].split()[-1])
	winner_numbers = parts[0].split(':')[-1].split()
	ticket_numbers = parts[-1].split()

	if card_num not in cards:
		cards[card_num] = 1
		
	for winner in winner_numbers:

		for number in ticket_numbers:
			
			if winner == number:
				cnt += 1
				break

	for i in range(1, cnt + 1):
		
		num = card_num + i

		if num not in cards:
			cards[num] = 1

		cards[num] += cards[card_num] 	

values = [num for num in cards.values()]

for j in values:
	sum+= j 

print(sum)

