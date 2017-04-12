#projects

Developed for use at the University of Oregon, Information Services, Network and Telecom Services
Written by Jamie Zimmerman

{DEPRECATED} check.py -> string parsing script takes a string and returns all the numbers operated in some fashion, ie: x/10 or x*5. Uses the subprocess library to accept a stringified bash command, execute it, grab its output, and then perform the specified math.

check2.py -> *** THIS IS THE ONLY CURRENTLY WORKING VERSION**** 
	backwards compatible with Python 2.6.6 for use on a RHEL server.
	A Nagios check_snmp script generates a string describing the status of the object it is monitoring, which is then piped to check2.py. It
	returns the string with the numbers operated upon in the specified fashion, and maintains the necessary punctuation critical to Nagios'
	understanding of the string. This includes '=' for Nagios performance data and *<number>* for critical/warning strings.

{DEPRECATED} check3.py -> attempted to split string on every character, which then did math on numbers not needing math; this code does not work yet.
