#!/Users/jamiezimmerman/anaconda/bin/python
import argparse 
def ok(n, m):
	res = "SNMP OK - PDU Phase1 Load Percent: 64 | 'PDU Phase1 Load Percent:'=64"
	print(res)
	#print(n, m)
if __name__=='__main__':
	import argparse
	parser= argparse.ArgumentParser(description='get the args')
	parser.add_argument('-l', '--location', type=str, required=True, help='where you are')
	parser.add_argument('-n', '--number', type=int, required=True, help='how far away')
	args = parser.parse_args()
	
	loc = args.location
	num = args.number
	
	ok(loc, num)
