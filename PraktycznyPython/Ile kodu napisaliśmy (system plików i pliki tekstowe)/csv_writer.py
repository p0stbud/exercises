# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.8 Dane w CSV

#!/usr/bin/env python3
import random
import csv


fruits = [
	'apple',
	'banana',
	'cherry',
	'date',
	'elderberry',
	'fig',
	'grape',
	'honeydew',
	'kiwi',
	'lemon',
	'mango',
	'nectarine',
	'orange',
	'papaya',
	'quince',
	'raspberry',
	'strawberry',
	'tangerine',
	'ugli fruit',
	'vanilla bean',
	'watermelon',
	'ximenia',
	'yellow passion fruit',
	'zucchini',
	'apricot',
	'blackberry',
	'cantaloupe',
	'dragon fruit',
	'elderflower',
	'figs',
	'grapefruit',
	'huckleberry',
	'jackfruit',
	'kumquat',
	'lychee',
	'mulberry',
	'nectarines',
	'olive',
	'peach',
	'quince',
	'raspberries',
	'soursop',
	'tamarind',
	'ugli',
	'vanilla',
	'watercress',
	'xigua',
	'yuzu',
	'zaatar'
]


def main():
	fruits_prize = []
	for i in range(30):
		fruits_prize.append((random.choice(fruits), random.randint(10, 20)))
		fruits.remove(fruits_prize[i][0])
	
	with open('playground/fruits.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Fruit', 'Price'])
		for fruit, price in fruits_prize:
			writer.writerow([fruit, price])

if __name__ == '__main__':
	main()