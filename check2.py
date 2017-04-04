#!/Users/jamiezimmerman/anaconda/bin/python

#TODO This shebang path MUST be changed before execution
# 1. bash$ which python
# 2. copy the pathname to the first line of this file with proper #!

#-----------------------------------------------------------------------#

#Written by Jamie Zimmerman 3/29/2017
#Backwards compatible for Python 2.6.6 deployment on RHEL server

#Usage: ./check2.py -c [bash command] -o [math operator] -a [amount to operate by]
#Example: ./check2.py -c 'echo SNMP - OK - -98 total power 25 KW' -a 10 -o '/'

import argparse
import operator
import os
import re

def check(string, OP, amount):
	ops = {'*': operator.mul, '/': operator.truediv}
	res = os.popen(string).read().strip()
	#os.popen() runs the bash command string, read() reads the output, strip deletes \n
	li = re.split("[= ]+", res) #splits by multiple delimiters: =, <space>
	for i in range(len(li)):
		try:
			new_value = calculate(float(li[i]), ops[OP], amount)
			li[i] = "{0:.1f}".format(new_value)
		except ValueError:
			pass
	# reg ex split function destroys the equals sign critical to the string
	# equal sign necessary on very last number only if there was a bar in the bash command
	if '|' in string:
		i = find(li)
		li[i] = "=" + li[i]
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

#helper function finds index of last instance of a number in a list
def find(lis):
	for j in range(len(lis)-1, -1, -1):
		try:
			dummy = float(lis[j])
			return j
		except ValueError:
			pass
	return None


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
