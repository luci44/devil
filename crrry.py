import sys
import argparse

parser = argparse.ArgumentParser(description='Dencrypt programming')
parser.add_argument('-e',
                    metavar='',
                    type=str,
                    help='Encrypted word',
                    required=False)

parser.add_argument('-p',
                    metavar='',
                    type=str,
                    help='The plaintext you already know',
                    required=False)

args = parser.parse_args()

if args.e == None or args.p == None:
    print("Missing args")
else:
    print("Reading file {0}".format(args.e))
    with open(args.e,'r',encoding='UTF-8') as f:
        endata=f.read()
    with open(args.p,'r',encoding='UTF-8') as f:
        dedata=f.read()

def decrypt(entext,detext):
    keyword = ""
    a=-1
    for x in entext:
        a += 1
        newChr=ord(x)
        for i in range(48,123):
            decrypted=chr((newChr-i)%255)
            if decrypted == detext[a]:
                print(detext[a],end=" ")
                keyword += chr(i)+" "
                break
    return keyword

print(decrypt(endata,dedata))
