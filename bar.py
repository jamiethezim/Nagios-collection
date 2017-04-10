#!/Users/jamiezimmerman/anaconda/bin/python

#TODO This shebang path MUST be changed before execution
# 1. bash$ which python
# 2. copy the pathname to the first line of this file with proper #!

#-----------------------------------------------------------------------#

#Written by Jamie Zimmerman 3/29/2017
#Testing that python script successfully runs bash commands (running nagios executable scripts) as expected

import argparse
import subprocess

def check(command):
	res = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
	print(res)

#----------------------------------------------------------#
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='SNMP get string process')
	parser.add_argument('-c', "--command", type=str, required=True, help='command to run')
	args = parser.parse_args()
	
	check(args.command)
