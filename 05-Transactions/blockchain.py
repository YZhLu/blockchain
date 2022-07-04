import hashlib
import json
from time import time
import copy
import random

from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

DIFFICULTY = 1 # Quantidade de zeros (em hex) iniciais no hash válido.

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
            'merkleRoot': self.generateMerkleRoot(self.memPool),
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        nonce = 0
        while self.isValidProof(prevBlock, nonce) is False:
            nonce += 1

        return nonce

    def createTransaction(self, sender, recipient, amount, timestamp, privKey):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": timestamp,
            "signature": privKey+""
        }
        self.memPool.append(transaction)


    @staticmethod
    def generateMerkleRoot(transactions):
        
        tree = transactions
        hashedTree = []
        if (len(tree)%2 != 0):
            tree.append(tree[-1])
        
        for leaf in tree:
            hashedTree.append(Blockchain.generateHash(leaf))
        
        auxTree = []
        if(len(hashedTree)==0):
            return ["0000000000000000000000000000000000000000000000000000000000000000"]
        else:
            print('chegou1')
            while(len(hashedTree)!= 1):
                print('chegou2')
                for hashedLeafIndex in range(0,len(hashedTree)-1,2):
                    auxTree.append(Blockchain.generateHash(hashedTree[hashedLeafIndex]+hashedTree[hashedLeafIndex+1]))
                hashedTree = []
                
                print(auxTree)
                hashedTree = auxTree
                auxTree = []
            return hashedTree

    @staticmethod
    def isValidProof(block, nonce):
        block['nonce'] = nonce
        guessHash = Blockchain.getBlockID(block)
        return guessHash[:DIFFICULTY] == '0' * DIFFICULTY 

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

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
| {merkleRoot} |                
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
                               index = self.chain[len(self.chain)-1]["index"],\
                               timestamp = (self.chain[len(self.chain)-1])["timestamp"],\
                               merkleRoot = (self.chain[len(self.chain)-1])["merkleRoot"][0],
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
| {merkleRoot} |                
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
                               index = self.chain[x-1]["index"], \
                               timestamp = (self.chain[x-1])["timestamp"],\
                               merkleRoot=(self.chain[x-1])["merkleRoot"][0],\
                               previousHash2 = (self.chain[x-1])["previousHash"])
            
            
            print(self.txtChainFormated)


    @property
    def prevBlock(self):
        return self.chain[-1]

    @staticmethod
    def sign(privKey, message):
        secret = CBitcoinSecret(privKey)
        msg = BitcoinMessage(message)
        return SignMessage(secret, msg)
        
    @staticmethod
    def verifySignature(address, signature, message):
        msg = BitcoinMessage(message)
        return VerifyMessage(address, msg, signature)


# Teste
blockchain = Blockchain()

sender = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
recipient = '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N'

# Cria 5 blocos, incluindo o Genesis, contendo de 1-4 transações cada, com valores aleatórios, entre os endereços indicados em sender e recipient.
for x in range(0, 4):
    for y in range(0, random.randint(1,4)) : 
        timestamp = int(time())
        amount = random.uniform(0.00000001, 100)
        blockchain.createTransaction(sender, recipient, amount, timestamp, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U')
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

blockchain.printChain()
 