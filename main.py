from hashlib import new
from block import Block
import block

transactionList = [
    "A mined 10 coin",
    "B mined 15 coin"
]

newTransactions = [
   "A sends 10 coin to B",
   "B sends 5 coin to A"
]


def main():
   #rsa.printAvailableHashAlgrorithm()
   #sha.shaTest()
   root = block.generateMerkleTree(transactionList, newTransactions)
   blockchain = Block('asd',1, merkleTree=root)
   #print(blockchain.proofOfWork())
   print(root)



if __name__ == "__main__":
   main()