from lib import dog
#or from lib.dog import bark
import math
import sys
import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color', metavar= 'color' ,required=True, choices={'red', 'yellow'}, 
                    help='the color to search for')

args = parser.parse_args()

print(args.color)


#bark()