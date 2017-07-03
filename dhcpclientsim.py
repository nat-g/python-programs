#learning from https://github.com/mccomasd/dhcpclientsimpython/blob/master/dhcpclientsimpython.py

import subprocess
import logging
import random
import sys


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)


try:
    from scapy.all import *

except ImportError:
    print "Scapy package for Python is not installed on your system."
    print "Get it from https://pypi.python.org/pypi/scapy and try again."
    sys.exit()
