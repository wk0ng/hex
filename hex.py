#!/usr/bin/python
# Author : wkong
# 2020 05-09
import os
import sys

if __name__ == "__main__":
    if len(sys.argv)==2:
        targetFile = sys.argv[1]
    else:
        print('python hex.py filename')
        exit()

    if os.path.exists(targetFile) == False:
        print('File \'['+targetFile+'\'] is not found!')
        exit()

    pFile = open(targetFile, 'rb')

    print('Read file ...')
    bitData = pFile.read()
    pFile.close()

    print('Change to hex ...')
    hexData = ''
    for b in bitData:
        hexData = hexData + hex(ord(b))[2:].upper()

    print('Make new file ...')
    pFile = open(targetFile + '-hex.txt', 'w+')
    pFile.write(hexData)
    pFile.close()

    print('Success, filename ' + targetFile + '-hex.txt')
