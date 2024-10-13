
from pyfiglet import Figlet
import sys

text = input('Input: ')
f0 = Figlet()




if len(sys.argv) < 3:
    print(f0.renderText(text))
else:
    if sys.argv[1] in ['-f', '--font']:
        f = Figlet(font = sys.argv[2])
        print(f.renderText(text))
    else:
        sys.exit('Invalid font name')





