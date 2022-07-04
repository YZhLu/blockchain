import hashlib
import json
from time import time
import copy

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash válido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        self.createBlock(previousHash='0'*64, nonce=0)
        self.mineProofOfWork(self.prevBlock) 

    def createBlock(self, nonce=0, previousHash=None):
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': '0'*64,
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        # TODO Implemente seu código aqui.
        if(self.getBlockID(prevBlock)[0:DIFFICULTY]=="0"*DIFFICULTY):
            return prevBlock['nonce']
        else:
            for nonce in range(1<<32):
                prevBlock['nonce'] = nonce
                if(self.getBlockID(prevBlock)[0:DIFFICULTY]=="0"*DIFFICULTY):
                    break
            
            
            return prevBlock['nonce']


    @staticmethod
    def isValidProof(block, nonce):
        # TODO Implemente seu código aqui.
        block['nonce'] = nonce
        passedBlockCopy = copy.copy(block)
        passedBlockCopy.pop("transactions", None)
        blkID = json.dumps(passedBlockCopy, sort_keys=True).encode()
        
        return hashlib.sha256(blkID).hexdigest()[0:DIFFICULTY]=="0"*DIFFICULTY

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        # TODO Implemente seu código aqui.

        passedBlockCopy = copy.copy(block)
        passedBlockCopy.pop("transactions", None)
        blkID = json.dumps(passedBlockCopy, sort_keys=True).encode()
        return hashlib.sha256(blkID).hexdigest()
       

    def printChain(self):
        # Mantenha seu método de impressão do blockchain feito na prática passada.
        # Implemente aqui um método para imprimir de maneira verbosa e intuitiva o blockchain atual.
        self.currentHash = self.chain[len(self.chain)-1].copy()
        self.currentHash.pop("transactions")
        
        self.txtLastBlock = ('''              
 __________________________________________________________________
| {currentHash} |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| {index}               {timestamp}              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| {previousHash2} |                
 ------------------------------------------------------------------ 
            ''')
        self.txtLastBlockFormated = self.txtLastBlock.format(currentHash = \
                               self.generateHash(self.currentHash),\
                               index = self.chain[len(self.chain)-1]["index"], timestamp = (self.chain[len(self.chain)-1])["timestamp"],\
                               previousHash2 = (self.chain[len(self.chain)-1])["previousHash"])
        
        print(self.txtLastBlockFormated)
        
        for x in range(len(self.chain)-1,0,-1):
            
            self.txtChain = ('''
                                A                                    
                                |                    
              
 __________________________________________________________________
| {currentHash} |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| {index}               {timestamp}              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| {previousHash2} |                
 ------------------------------------------------------------------
        ''')
            
            
            self.txtChainFormated = self.txtChain.format(currentHash = \
                               (self.chain[x])["previousHash"],\
                               index = self.chain[x-1]["index"], timestamp = (self.chain[x-1])["timestamp"],\
                               previousHash2 = (self.chain[x-1])["previousHash"])
            
            
            print(self.txtChainFormated)


    @property
    def prevBlock(self):
        return self.chain[-1]

# Teste
blockchain = Blockchain()
for x in range(0, 4): 
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)
    

for x in blockchain.chain :
    print('[Bloco #{} : {}] Nonce: {} | É válido? {}'.format(x['index'], Blockchain.getBlockID(x), x['nonce'], Blockchain.isValidProof(x, x['nonce'])))

