#!/usr/bin/python

def firstFunction():
    print("Function in first module")

def SecondFunction():
    print("Function in second module")

def main():
    print("First module name is {}".format(__name__))
    print("First module name is {}".format(__name__))

if __name__ == '__main__':
    main()