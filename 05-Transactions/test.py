import hashlib
import json
from time import time
import copy
import random

from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

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
        
        #if len(transactions) == 1:
        tree = transactions
        hashedTree = []
        if (len(tree)%2 != 0):
            tree.append(tree[-1])
        
        for leaf in tree:
            hashedTree.append(Blockchain.generateHash(leaf))
        
        auxTree = []
        while(len(hashedTree) != 1):
            for hashedLeafIndex in range(hashedTree-1):
                auxTree.append(Blockchain.generateHash(hashedTree[hashedLeafIndex]+hashedTree[hashedLeafIndex]))
            hashedTree = []
            hashedTree = auxTree
            auxTree = []

        return hashedTree

        


    @staticmethod
    def isValidProof(block, nonce):
        block['nonce'] = nonce
        guessHash = Blockchain.getBlockID(block)
        return guessHash[:1] == '0' * 1 

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
        pass # Mantenha seu método de impressão do blockchain feito em práticas passadas.

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
#blockchain = Blockchain()

sender = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
recipient = '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N'
memPool = []
privKey = 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U'

def createTransaction(sender, recipient, amount, timestamp, privKey):
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount,
        "timestamp": timestamp,
        "signature": privKey + ""
    }
    memPool.append(transaction)

def generateHash(data):
    blkSerial = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(blkSerial).hexdigest()

for y in range(0, random.randint(1,4)) : 
    timestamp = int(time())
    amount = random.uniform(0.00000001, 100)
    createTransaction(sender, recipient, amount, timestamp, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U')

def generateMerkleRoot(transactions):
        
        #if len(transactions) == 1:
        tree = transactions
        hashedTree = []
        print("Len de TREE", len(tree))
        if (len(tree)%2 != 0):
            tree.append(tree[-1])
        
        for leaf in tree:
            hashedTree.append(generateHash(leaf))
            print("hashed Leaf",generateHash(leaf))
        print("arvore hash", hashedTree)
        auxTree = []
        while(len(hashedTree) != 1):
            for hashedLeafIndex in range(0,len(hashedTree)-1, 2):
                auxTree.append(generateHash(hashedTree[hashedLeafIndex]+hashedTree[hashedLeafIndex+1]))
                print("arvore AUX", auxTree)
            hashedTree = []
            hashedTree = auxTree
            auxTree = []
        print(hashedTree[0])
        return hashedTree

generateMerkleRoot(memPool)
#print(memPool)
