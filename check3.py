#!/Users/jamiezimmerman/anaconda/bin/python

#TODO This shebang path MUST be changed before execution
# 1. bash$ which python
# 2. copy the pathname to the first line of this file with proper #!

#-----------------------------------------------------------------------#

#Written by Jamie Zimmerman 4/3/2017
#Backwards compatible for Python 2.6.6 deployment on RHEL server
#Rewritten for numbers encapsulated in ***

#Usage: ./check3.py -c [bash command] -o [math operator] -a [amount to operate by]
#Example: ./check3.py -c 'echo SNMP - OK - -98 total power 25 KW' -a 10 -o '/'
from string import punctuation
import argparse
import operator
import os

def check(string, OP, amount):
	ops = {'*': operator.mul, '/': operator.truediv}

	res = os.popen(string).read().strip()
	#os.popen() runs the bash command string, read() reads the output, strip deletes \n
	li = [char for char in res]
	new_li = []
	i = 0
	dotted = False
	while i < len(li):
		if li[i].isalpha() or (li[i] in punctuation+' ' and li[i] != '.'):
			new_li.append(li[i])
		if li[i].isdigit():
			if new_li[-1].isdigit() or new_li[-1].startswith('-'):
				new_li[-1] = new_li[-1] + li[i]
			else:
				new_li.append(li[i])
		if li[i] == '.':
			if new_li[-1].isdigit():
				new_li[-1] = new_li[-1] + li[i]
				dotted = True
			else:
				new_li.append(li[i])
		if li[i].isdigit() and dotted:
			new_li[-1] = new_li[-1] + li[i]
			dotted = False
		i = i+1
	
	for i in range(len(new_li)):
		try:
			new_value = calculate(float(new_li[i]), ops[OP], amount)
			new_li[i] = "{0:.1f}".format(new_value)
		except ValueError:
			pass
	return "".join(new_li)

#----------------------------------------------------------#

#helper function to calculate new value
def calculate(inp, op, out):
	'''
	inp -> float/int
	op -> mathematical function from operator library
	out -> float/int
	'''
	return op(inp, out)


#----------------------------------------------------------#
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='SNMP get string process')
	parser.add_argument('-c', "--command", type=str, required=True, help='command to run')
	parser.add_argument('-o', "--operation", type=str, required=True, help='operation to perform, ie: "/" to divide or "*" to multiply')
	parser.add_argument('-a', "--amount", type=int, required=True, help='int(amount) to divide/multiply by')
	
	args = parser.parse_args()

	command = args.command
	operation = args.operation
	amount = args.amount

	#print("command is {}\noperate is {}\namount is {}".format(command, operation, amount))
	res = check(command, operation, amount)
	print(res)
