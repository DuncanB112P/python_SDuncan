#import external packages after installing those packages with the "pip install" command
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex('Hello, ' + sys.argv[1])