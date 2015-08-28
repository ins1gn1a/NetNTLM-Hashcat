#!/usr/bin/env python

import sys
import re
import argparse

# Arg Input (Like a pirate)
p = argparse.ArgumentParser(description='Convert NetNTLM John Hashes to Hashcat Format')
p.add_argument('-i','--hash',action='store_true',help='Enter one-time hash input mode',required=False)
p.add_argument('-f','--file',dest='file',help='Path to file containing multiple hashes',required=False,default="")
p.add_argument('-o','--output',dest='output',help='File path to save the converted hashes',required=False)
a = p.parse_args()

# RegEx to re-arrange the hash
reg = re.compile('(.*?):(\$.*?)\$(.*?)\$(.*)')

if a.hash:
        try:
                hash = raw_input("Enter your hash:\n")
                if hash:
                        print reg.sub(r'\1::::\4:\3',hash)

        except KeyboardInterrupt:
                sys.exit("\n")

        except:
                sys.exit("Error: Something is broken\n")

elif a.file:
        try:
                with open(a.file) as temp:

                        for line in temp:
                                outhash =  reg.sub(r'\1::::\4:\3',line)
                                outhash = outhash.rstrip('\n\n')

                                if a.output is None:
                                        print outhash
                                else:
                                        with open(a.output,'w') as f:
                                                f.write(outhash)
                                        f.close()

        except KeyboardInterrupt:
                sys.exit("\n")

        except:
                sys.exit("Error: Input file doesn't exist.\n")

else:
        p.print_help()

