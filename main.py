from hashlib import new
from block import Block


def main():
   #rsa.printAvailableHashAlgrorithm()
   #sha.shaTest()
   block = Block('asd',1)
   print(block.proofOfWork())



if __name__ == "__main__":
   main()