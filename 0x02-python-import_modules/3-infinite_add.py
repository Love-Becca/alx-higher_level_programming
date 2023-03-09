#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv
    sum = 0
    if len(arguments) == 1:
        print("{}".format(sum))
    else:
        for i in range(1, len(arguments)):
            sum +=int(arguments[i])
        print("{}".format(sum))
