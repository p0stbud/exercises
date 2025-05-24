# Kurs Praktyczny Python by Gynvael Coldwind
# ex_1.7 Dane w JSONie

# This script demonstrates how to create a JSON file with different data types,
# including integers, lists, dictionaries, floats, booleans, and null values.

#!/usr/bin/env python3
import json


diffrent_types = {
	"int": 2,
	"list[int]": [1, 2, 3, 4, 5],
	"list[string]": ["1", "2", "3", "4", "5"],
	"dict": {"type": "dict"},
	# set is not JSON serializable
	# "set": {1, 2, 3, 4, 5},  # This will raise an error
	"float": 3.14,
	"bool": True,
	"null": None,
	# bytes is not JSON serializable
	# "bytes": b"this is bytes",  # This will raise an error
	"string": "string"
	# tuple is not JSON serializable
	# "tuple": (1, 2, 3)  # This will raise an error
}


# main function to demonstrate what is the difference between
# json.dump() and json.dumps()
def main():
	f_path = "./playground/plik.json"
	with open(f_path, "w") as f:
		# Write the dictionary to a JSON file
		# using json.dump() which writes directly to a file
		json.dump(diffrent_types, f, indent=4)
	with open(f_path, "r") as f:
		# Read the JSON file back into a Python dictionary
		# using json.load() which reads from a file
		json_f = json.load(f)
		print(json_f)
	
	# Convert the dictionary to a JSON string
	# using json.dumps() which returns a string
	json_string = json.dumps(diffrent_types, indent=4)
	with open(f_path, "w") as f:
		f.write(json_string)

	# Read the JSON string back into a Python dictionary
	# using json.loads() which parses a JSON string
	# json.loads() is used for strings, while json.load() is used for files
	json_f = json.loads(json_string)
	print(json_f)


if __name__ == '__main__':
	main()