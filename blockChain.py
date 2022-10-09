import hashlib

class BlockChain:
    chain = []

    def __init__(self, payload, proofOfWork):
        self.chain.append(Node('00000000000000000000', payload, proofOfWork))
        #self.chain[0].preBlock = 
        #self.chain[0].payload = payload
        #self.chain[0].proofOfWork = proofOfWork
    
    def addNode(self, payload, proofOfWork):
        preHash = hashlib.sha256(str(self.chain[-1]).encode('ascii')).hexdigest()
        self.chain.append(Node( preHash,
                                payload,
                                proofOfWork))
        #self.chain[-1].preBlock = hashlib.sha256(str(self[-2]).encode('ascii')).hexdigest()
        #self.chain[-1].payload = payload
        #self.chain[-1].proofOfWork = proofOfWork
    
    def __str__(self) -> str:
        out = ""
        for i in self.chain:
            out += '########## block starts ##########\n'
            out += '\t preblock value: ' + i.preBlock + '\n'
            out += '\t payload paremets: ' + str(i.payload) + '\n'
            out += '\t proof of work value: ' + i.proofOfWork + '\n'
            out += '########## end of block ##########' + '\n \n'
        return out
    
class Node:

    def __init__(self, preBlock, payload, proofOfWork):
        self.preBlock = preBlock
        self.payload = payload
        self.proofOfWork = proofOfWork