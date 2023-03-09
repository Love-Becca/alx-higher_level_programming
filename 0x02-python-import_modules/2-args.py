#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_lenght = len(sys.argv)
    print("{} arguments:".format(argument_lenght - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
