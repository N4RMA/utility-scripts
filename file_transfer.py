import requests
import sys

url = 'https://file.io'
filename = sys.argv[1]

with open(filename, 'rb') as f:
    response = requests.post(url, files={'file': f})

if response.ok:
    json = response.json()
    print(f"Uploaded {filename} to: {json['link']}")
else:
    print("Upload failed:", response.text)

