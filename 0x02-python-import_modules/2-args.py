#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_lenght = len(sys.argv)
    if len(sys.argv) == 1:
        print("{} arguments.".format(argument_lenght - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(argument_lenght - 1))
    else:
        print("{} arguments:".format(argument_lenght - 1))

    for i in range(1, argument_lenght):
        print("{}: {}".format(i, sys.argv[i]))
