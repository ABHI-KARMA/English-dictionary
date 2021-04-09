import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

class Dictionary():
	def __init__(self,data):
		self.data = data
	
	def find_meaning(self):
		self.data = self.data.lower()
		if self.data in data:
			return data[self.data]
		elif len(get_close_matches(self.data,data.keys())) > 0:
			yn = input("Did you mean %s instead? Enter Y if yes, or N if No : "% get_close_matches(self.data, data.keys())[0]).lower()
			if yn == 'y':
				return data[get_close_matches(self.data, data.keys())[0]]
			elif yn == 'n':
				return "The word doesn't exist, please cheak it"
			else:
				return "We didn't understand your entry"
		else:
			return "The word doesn't exist, please cheak it"

word = input("Enter Word : ")
d = Dictionary(word)

if type(d) == list:
	for item in output:
		print(item)
else:
	print(d.find_meaning())

input('Press enter to exit')
