import sys
import re

def init():
	program = []
	if(len(sys.argv) < 2):
		print("ABORT; GIVE ME A FILE! PLS I DIE NOW!")#DEBUG
		exit()
	with open(str(sys.argv[1])) as f:
		program = f.read().split("\n")
	program = parser(program)
	#print(program)#DEBUG
	print(compile(program))

def parser(prog):
	returner = []
	for i in prog:
		if(i != "" and i.startswith("#") == False):
			returner.append(i)
	return returner

def compile(prog):
	c = "#include <stdio.h>\nint main(){\n"
	lang_ifnot = re.compile("Do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*) lacking\?")
	lang_if = re.compile("Do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*)\?")
	lang_elifnot = re.compile("Or do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*)lacking\?")
	lang_elif = re.compile("Or do you feel the energy of (?P<condition>([0-9a-zA-Z]| )*)\?")
	lang_whilenot = re.compile("Feel the vibration of (?P<condition>([0-9a-zA-Z]| )*)lacking\.")
	lang_while = re.compile("Feel the vibration of (?P<condition>([0-9a-zA-Z]| )*)\.")
	lang_endblock = re.compile("You feel it.")
	lang_dec = re.compile("We need (?P<dec>([0-9a-zA-Z]| )*) of (?P<var>([0-9a-zA-Z]| )*)\.")
	lang_assign = re.compile("(?P<var>([0-9a-zA-Z]| )*) is (?P<exp>([0-9a-zA-Z]| )*)\.")
	lang_read = re.compile("Extract the mother tincture of (?P<var>([0-9a-zA-Z]| )*)\.")
	lang_print = re.compile("Shake the (?P<var>([0-9a-zA-Z]| )*)\.")
	for i in prog:
		if(lang_ifnot.match(i)):
			c = c + "if(!" + expression(lang_ifnot.match(i).group("condition")) + "){\n"
		elif(lang_if.match(i)):
			c = c + "if(" + expression(lang_if.match(i).group("condition")) + "){\n"
		elif(lang_elifnot.match(i)):
			c = c + "}else if(!" + expression(lang_elifnot.match(i).group("condition")) + "){\n"
		elif(lang_elif.match(i)):
			c = c + "}else if(" + expression(lang_elif.match(i).group("condition")) + "){\n"
		elif(lang_whilenot.match(i)):
			c = c + "while(!" + expression(lang_whilenot.match(i).group("condition")) + "){\n"
		elif(lang_while.match(i)):
			c = c + "while(" + expression(lang_while.match(i).group("condition")) + "){\n"
		elif(lang_endblock.match(i)):
			c = c + "}\n"
		elif(lang_dec.match(i)):
			c = c + "int " + var(lang_dec.match(i).group("var")) + "=" + expression(lang_dec.match(i).group("dec")) + ";\n"
		elif(lang_assign.match(i)):
			c = c + var(lang_assign.match(i).group("var")) + "=" + expression(lang_assign.match(i).group("exp")) + ";\n"
		elif(lang_read.match(i)):
			c = c + var(lang_read.match(i).group("var")) + "=getchar();\n"
		elif(lang_print.match(i)):
			c = c + "putchar(" + var(lang_print.match(i).group("var")) + ");\n"
		else :
			print("ALERT!! THIS DIDNT WORK! HOLY SHITFUCK! RUN! THE TINCTURE IS GOING TO EXPLODE! I DIE NOW")#DEBUG
			exit()
	c = c + "}"
	return c

def expression(e):
	returner = []
	arr = e.split("potenciated by")
	for summand in arr:
		ret2 = []
		arr2 = summand.split("diluted by")
		for i in arr2:
			ret2.append(var(i))
		returner.append("-".join(ret2))
	return "+".join(returner)

def var(v):
	v = "_".join(v.strip().split(" "))
	return v

init()
