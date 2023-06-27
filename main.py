import argparse
import fish

if __name__ == '__main__':
     # Set up argument parser for ease of command-line use
    parser = argparse.ArgumentParser(description='Macros for Destiny 2 stuff') 
    parser.add_argument('-f', '--fishing', action=argparse.BooleanOptionalAction, help="Gone fishin'")
    parser.add_argument('-c', '--controller', action=argparse.BooleanOptionalAction, help="Use controller")
    
    args = parser.parse_args()
    
    if args.fishing:
        fish.fish(args.controller)
