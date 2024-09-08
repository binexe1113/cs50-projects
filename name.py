import sys
if len(sys.argv) <2:
    print
    print ("hello, my name is", sys.argv[1])
except IndexError:
    print ("too few arguments")
