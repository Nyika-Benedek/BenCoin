from ast import If
from datetime import datetime
from hashlib import new
import hashlib
import os
import string
from sys import byteorder
from time import time
from unicodedata import name
import random
from unittest import result
from unittest.mock import NonCallableMagicMock

#Get the curent datetime
def currentDatetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)
    return dt_string

#Generate a nonce value
def generate_nonce(length=4):
    # Generate a nonce value(default 4 byte)
    return int.from_bytes(os.urandom(length), byteorder='big')

#Generate merkle Tree
def generateMerkleTree():
    # TODO implement merkle
    return 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

#This class represent a block(before it's hashing)
class Block:

    def __init__(self, preBlock,id):
        self.time = currentDatetime()
        self.nonce = generate_nonce()
        self.merkleRoom = generateMerkleTree()
        self.preBlock = preBlock
        self.id = str(id)
    
    # Generate a hash from the block
    def generateHash(self):
            #concatenate every prop hash
            result = str(time) + str(self.nonce) + str(self.merkleRoom) + str(self.preBlock) + str(self.id)
            
            result = hashlib.sha256(result.encode('ascii')).hexdigest()

            #hash every property
            #time = hashlib.sha256(self.time.encode('ascii')).hexdigest()
            #nonce = hashlib.sha256(str(self.nonce).encode('ascii')).hexdigest()
            #merkleRoom = hashlib.sha256(str(self.merkleRoom).encode('ascii')).hexdigest()
            #preBlock = hashlib.sha256(str(self.preBlock).encode('ascii')).hexdigest()
            #id = hashlib.sha256(str(self.id).encode('ascii')).hexdigest()


            # printing the equivalent hexadecimal value.
            #print("The hexadecimal equivalent of SHA256 is : ")
            #print(result.hexdigest())
            return result
    
    # call Proof of Work recursively untill match

    def proofOfWork(self) -> str:
        temp = self.generateHash()
        iterationCounter = 1
        #print('\n' + temp + '\n')
        #if (temp[0] != '0'):
        #    self.nonce = generate_nonce()
        #    self.proofOfWork()
        #else:
        #    return temp
        #return temp
        while(temp[0] != '0'):
            self.nonce = generate_nonce()
            temp = self.generateHash()
            iterationCounter += 1
        
        print('iterations until first match: ' + str(iterationCounter))
        return temp