import hashlib
import json

class Blockchain(object):

    @staticmethod
    def generateHash(data):
       
        hashDumped = json.dumps(data, sort_keys=True)
        sha_signature = \
            hashlib.sha256(hashDumped.encode()).hexdigest()
        return sha_signature



# Testando sua implementação: espera-se um retorno True.

var1 = {
            'nome': "Jon Snow",
            'idade': 18,
        }
expected_hash1 = "4145c81419ee987c94f741936c3277e9b281e2ffc9faa3edb5693128e1ee65c1"
var1_hash = Blockchain.generateHash(var1)
print(f'Dados: {var1}')
print(f'Hash   gerado: {var1_hash}')
print(f'Hash esperado: {expected_hash1}')
print(f'Iguais? {expected_hash1==var1_hash}\n')