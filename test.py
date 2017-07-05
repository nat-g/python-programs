# To access interpreter
python

# To print an array of all the arguments passed on the CLI [as a script]
# From a command line it would run as: python test.py "hello"
import sys
print sys.argv

# To print the second argument, which is "hello"
# Doesn't matter if you use hello, "hello" or 'hello', result is just printing 
import sys
print sys.argv[1]

