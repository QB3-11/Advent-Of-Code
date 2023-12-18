file = 'input.txt'
demo_file = 'demo.txt'
points = 0

with open(file) as data:
	scratch_cards = data.readlines()

for card in scratch_cards:

	card_value = 0
	add_points = False

	parts = card.split('|')
	winners = parts[0].split(':')[1].split()
	ticket_numbers = parts[1].split()

	for winner in winners:

		for number in ticket_numbers:			

			if winner == number:
				if card_value == 0:
					card_value += 1
					break

				else:
					card_value *= 2 
					break

	points += card_value

print(points)

		
		
			
