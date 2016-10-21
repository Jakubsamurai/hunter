#!/usr/bin/python

import os
import sys, traceback

def main():
    try:
        print(
"\033[1;31m\nBienvenido a Hunter, el cazador de paquetes\n\033[1;m"
"\033[1;31m\nJakub Janarek | http://www.jakubjanarek.com | github: Jakubsamurai\n\033[1;m"
        )
    except KeyboardInterrupt:
        print ("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()      
    




