# import sys
import argparse

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     for _ in range(int(sys.argv[2])):
#         print("meow")
# else:
#     print("Usage: meow.py")

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")