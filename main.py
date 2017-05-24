import getopt
import sys

from exception import BusinessException
from interpreter import Interpreter

interpreter = Interpreter()


def talk_to_interpreter(input):
    try:
        answer = interpreter.read(input)
        if answer:
            print answer
    except BusinessException as ex:
        print ex.message


def input_process(pre_input=None):
    print('exit to exit')
    input = pre_input if pre_input else raw_input()
    while True:
        if input == 'exit':
            sys.exit()

        if isinstance(input, list):
            for line in input:
                talk_to_interpreter(line)
        else:
            talk_to_interpreter(input)

        input = raw_input()


def read_file(filename):
    with open(filename) as file:
        content = file.readlines()

    content = [x.strip() for x in content]
    return content


def main():
    pre_input = None
    for opt, arg in get_options():
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("--input-file", "-i"):
            pre_input = read_file(arg)
    input_process(pre_input)


def get_options():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hi:f", ["help", "input-file="])
        return opts
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)


def usage():
    print "usage: main.py [--input-file]"
    print "   --input-file: each line of a file will be used as an input line"
    sys.exit()


if __name__ == '__main__':
    main()
