#!/usr/bin/python
#Written by Jamie Zimmerman 3/27/2017
import argparse
import operator
import subprocess

#Usage: python3 check.py -c [bash command] -o [math operator] -a [amount to operate by]
#Example: python3 check.py -c 'echo SNMP - OK - -98 total power 25 KW' -a 10 -o '/'

def check(string, OP, amount):
	ops = {'*': operator.mul, '/': operator.truediv}

	li = bashrun(string) #get the string result of whatever the command specified
	for i in range(len(li)):
		try:
			new_value = calculate(float(li[i]), ops[OP], amount)
			li[i] = "{0: .2f}".format(new_value)
		except ValueError:
			pass
	return " ".join(li)

#----------------------------------------------------------#
#helper function to run command and get result
def bashrun(cmd):
	'''
	input -> string
	splits the string, runs the bash command, and returns output from command
	output -> list (of words generated in the result)
	'''
	result = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE)
	retrieved = result.stdout.decode('utf-8').split(' ')
	return retrieved


#helper function to calculate new value
def calculate(input, op, output):
	'''
	input -> float/int
	op -> mathematical function from operator library
	output -> float/int
	'''
	return op(input, output)


#----------------------------------------------------------#
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='SNMP get string process')
	parser.add_argument('-c', "--command", type=str, required=True, help='command to run')
	parser.add_argument('-o', "--operation", type=str, required=True, help='operation to perform, ie % "%" to divide or "*" to multiply')
	parser.add_argument('-a', "--amount", type=int, required=True, help='int(amount) to divide/multiply by')
	
	args = parser.parse_args()

	command = args.command
	operation = args.operation
	amount = args.amount

	#print("command is {}\noperate is {}\namount is {}".format(command, operation, amount))
	res = check(command, operation, amount)
	print(res)
