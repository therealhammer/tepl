import json
js = ""

def init():
	language = []
	with open("tepl.json", "r") as jsonfile:
		js = json.load(jsonfile)
	print(js["language"])
	for p in js["language"]:
		print(str(p) + " = " + str(js["language"][p]))
		
init()