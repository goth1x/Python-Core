import sys


def parse_args():
    result = ""
    result = ' '.join(sys.argv[1:])

    return result

a = parse_args()
print(tuple(a))