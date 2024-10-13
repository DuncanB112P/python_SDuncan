import sys


from libraries_create_own import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])