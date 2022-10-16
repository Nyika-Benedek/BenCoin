from hashlib import new
from block import Block
import block
from blockChain import BlockChain

transactionList = [
    "A mined 10 coin",
    "B mined 15 coin"
]

newTransactions = [
   "A sends 10 coin to B",
   "B sends 5 coin to A"
]

idCounter = 0
def nextId():
   global idCounter
   idCounter += 1
   return idCounter 

def main():
   #rsa.printAvailableHashAlgrorithm()
   #sha.shaTest()


   # generate the first node
   root = block.generateMerkleTree(transactionList, [])
   node = Block(nextId(), merkleTree=root)

   # createa new blockchain
   blockChain = BlockChain(node, node.proofOfWork('00000000000000000000'))

   # adding a new node
   newRoot = block.generateMerkleTree(transactionList, newTransactions)
   newNode = Block(nextId(), merkleTree=newRoot)
   blockChain.addNode(newNode, newNode.proofOfWork(blockChain.chain[-1]))

   # test it content
   print(blockChain)
   #print(blockchain.proofOfWork())
   #print(root)




if __name__ == "__main__":
   main()