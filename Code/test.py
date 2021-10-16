import os
import requests

ident = 0
ipfs_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
hd={"pinata_api_key":os.environ['PINATA_API_KEY'],"pinata_secret_api_key" : os.environ['PINATA_API_SECRET']}
file = (("file", ("0.png", open('/home/notes/Programming/Yapeswap/yape-art-generator/Yapes/' + str(ident) +'.png'))))

print(r.status_code)
print(r.json()['message'])

#this is a well formed image request

r = requests.post(ipfs_url,
                    files={"file": (str(ident)+".png", open('/home/notes/Programming/Yapeswap/yape-art-generator/Yapes/' + str(ident) +'.png', "rb"))},
                    headers=hd)

#Gets the hash for ipfs
hash = r.json()['IpfsHash']
print(r.json()['IpfsHash'])

#Well formed json request
r = requests.post(ipfs_url,
                    files={"file": (str(ident)+".json", open('/home/notes/Programming/Yapeswap/yape-art-generator/Metadata/' + str(ident) +'.json', "rb"))},
                    headers=hd)

print(r.status_code)