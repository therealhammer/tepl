import sys
import re

def init():
	program = []
	with open(str(sys.argv[1])) as f:
		program = f.read().split("\n")
	program = parser(program)
	print(compile(program))

def parser(prog):
	returner = []
	for i in prog:
		if(i != "" and i.startswith("#") == False):
			returner.append(i)
	return returner

def compile(prog):
	c = "#include <stdio.h> int main(){"
	lang_ifnot = re.compile("Do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*) lacking\?")
	lang_if = re.compile("Do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*)\?")
	for i in prog:
		if(lang_ifnot.match(i)):
			c = c + "if(!" + expression(lang_ifnot.match(i).group("condition")) + ")"
		if(lang_if.match(i)):
			c = c + "if(" + expression(lang_ifnot.match(i).group("condition")) + ")"
	c = c + "}"
	return c

def expression(e):
	return e

init()
