#! /usr/bin/python3
from symulator import Symulator
width, height = 800, 600

def main():
    Symulator().start(width, height)
    print('in main')

if __name__ == "__main__":
    main()

