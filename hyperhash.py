'''This is the cricky.py file 
USAGE:
  python cricky.py [hash-type] [hash-text] [dictfile] 
'''

import sys
import importlib

try:
    VERSION = '0.0.1'

    typeShit = sys.argv[1]


    if(typeShit == "--version"):
            print 'HyperHash Version ',VERSION
            sys.exit(0)



    if(typeShit == "--help"):
            print(" _ _ _ _                                 _ _ _ _ ")
            print("| .   . |                               | .   . |")
            print("|   ^   |                               |   ^   |")
            print("| \_-_/ |                               | \_-_/ |")
            print("|_ _ _ _|                               |_ _ _ _|")
            print(" _ _ _ _      [The HyperHash Project]    _ _ _ _ ")
            print("|       |     [KEEP SOCIAL DISTANCE]    |       |")
            print("|       |                               |       |")
            print("|       |                               |       |")
            print("|_ _ _ _|                               |_ _ _ _|")
            print("    |                                       |    ")
            print("    |                                       |    ")
            print("USAGE:\nFor cracking: python cricky.py --crack [hash-type] [hash-text] [dictfile]")
            print("For generating: python cricky.py --generate [hash-type] [hash-text]\n\n")
            sys.exit(0)



    if(typeShit == "--crack"):
            hashType = sys.argv[2]
            hashText = sys.argv[3]
            dictFile = sys.argv[4]
            i=importlib.import_module(hashType)
            # Using readlines() 
            file1 = open(dictFile, 'r') 
            Lines = file1.readlines()
            coun = 1

            for line in Lines: 
                 xarr = i.hash(line.strip())
                 print "Trying attempt [",coun,"] Text: ",line
                 if(xarr == hashText):
                        print "Detected Hash Successfully [",coun,"] Hash: ",line
                        sys.exit(0)



    if(typeShit == "--generate"):
            hashType = sys.argv[2]
            hashText = sys.argv[3]
            i=importlib.import_module(hashType)
            xarr = i.hash(hashText.strip())
            print "Hash for ",hashText,"is: ",xarr

except IndexError:
            print("Something Incorrect in arguments detected.")
            print("USAGE:\nFor cracking: python cricky.py --crack [hash-type] [hash-text] [dictfile]")
            print("For generating: python cricky.py --generate [hash-type] [text]\n\n")
            sys.exit(0)

except ImportError:
           print("Something Wrong with hash type you provided.")
           print("USAGE:\nFor cracking: python cricky.py --crack [hash-type] [hash-text] [dictfile]")
           print("For generating: python cricky.py --generate [hash-type] [text]\n\n")
           sys.exit(0)