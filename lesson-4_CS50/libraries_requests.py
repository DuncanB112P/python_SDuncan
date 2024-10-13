import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = (requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])).json()

for element in response['results']:
    print('\n', element['artistName'], element['trackName'], element['releaseDate'], '\n', sep='\n')




