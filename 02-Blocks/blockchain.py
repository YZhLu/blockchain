#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:17:05 2019

@author: luizdefrancaafonsoferreirafilho
"""

import hashlib
import json
import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()
        self.blockIndex = 1

    def createGenesisBlock(self):
        # Implemente aqui o método para gerar o bloco Genesis, invocado no construtor da classe,
        # chamando o método createBlock() previamente implementado.
        genesisBlock = {
            'index': 1,
            'timestamp': int(time.time()),
            'nonce': 0,
            'merkleRoot': 000000000000000000000000000000000000000000000000000000000000000,
            'previousHash': "0000000000000000000000000000000000000000000000000000000000000000",
            'transactions': []
        }
        
        self.chain.append(genesisBlock)

    def createBlock(self, nonce=0, previousHash=None):
        # Implemente aqui o método para retornar um bloco (formato de dicionário)
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.
        self.blockIndex = self.blockIndex + 1

        self.prevBlockCopy= self.chain[self.blockIndex-2].copy()
        self.prevBlockCopy.pop("transactions")
        self.prevBlockHeadCopy = self.prevBlockCopy
      
        newBlock = {
            'index': self.blockIndex,
            'timestamp': int(time.time()),
            'nonce': 0,
            'merkleRoot': 0000000000000000000000000000000000000000000000000000000000000000,
            'previousHash': self.generateHash(self.prevBlockHeadCopy),
            'transactions': []
        }
        self.chain.append(newBlock)
        

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
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

# Teste
blockchain = Blockchain()
for x in range(0, 3): 
    blockchain.createBlock()
blockchain.printChain()
print(blockchain.createGenesisBlock())