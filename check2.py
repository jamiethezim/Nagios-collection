#!/Users/jamiezimmerman/anaconda/bin/python
#Written by Jamie Zimmerman 3/29/2017
#Backwards compatible for Python 2.6.6 deployment on RHEL server

import argparse
import operator
#import subprocess
import os

#Usage: ./check.py -c [bash command] -o [math operator] -a [amount to operate by]
#Example: ./check.py -c 'echo SNMP - OK - -98 total power 25 KW' -a 10 -o '/'

def check(string, OP, amount):
	ops = {'*': operator.mul, '/': operator.truediv}

	li = os.popen(string).read().strip().split(' ') #get the string result of whatever the command specified
	for i in range(len(li)):
		try:
			new_value = calculate(float(li[i]), ops[OP], amount)
			li[i] = "{0:.2f}".format(new_value)
		except ValueError:
			pass
	return " ".join(li)

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
