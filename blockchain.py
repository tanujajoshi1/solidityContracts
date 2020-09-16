import datetime
import hashlib
from flask import Flask,jsonify,request 


##We have created a genesis block##
class Blockchain:
    def __init__(self):
        #constructor
        self.chain=[]
        
        #genesis block is created first time the constructor is made
        #proof is basically a condition that hash will be generated with what condition
        self.create_block(proof=1, previous_hash='0')
        
        def create_block(self,proof,previos_hash):
            #define data for the blocks
            block={'index': len(self.chain)+1,'timestamp':str(datetime.datetime.now()),
                  'proof':proof,
                  'previous_hash':previous_hash}
            ##this block is having data in dictionary form. For dictionary we use json format
            
            self.chain.append(block)
            return block
        
        def get_previous_block(self):
            return self.chain[-1]
        
        def hash(self,block):
            encoded_block = json.dumps(block).encode()
            return hashlib.sha256(encoded_block).hexdigest()
        
        def proof_of_work(self,previous_proof):
            check_proof= False
            new_proof=1
            
            while check_proof is False:
                hash_operation=hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
                
                if hash_operation[:5]=='00000':
                    check_proof=True
                    
                else:
                    new_proof=new_proof+1
            
            return new_proof
            
        
blockchain=Blockchain() #blockchain is an object of class Blockchain


app=Flask(__name__)
#app.route gives me an address tom mine block
@app.route('/mine_block', methods=['GET'])

def mine_block():
    
    #getting hash of last block
    previous_block=blockchain.get_previous_block()
    
    #getting hash of the previous block
    previous_hash=blockchain.hash(previous_block)
    
    previous_proof=previous_block['proof']
    
    proof=blockchain.proof_of_work(previous_proof)
    
    block=blockchain.create_block(proof,previous_hash)
    response={'message':'Congrats you have mined the block',
             'index':block['index'],
             'timestamp':block['timestamp'],
             'proof':block['proof'],
             'previous_hash':block['previous_hash']}
    
    return jsonify(response),200
    
    
app.run(host=localhost, port=5006)
    
