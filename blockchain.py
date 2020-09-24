#To make your own blockchain from genesis 

import datetime
import hashlib
from flask import Flask,jsonify,request 
from urllib.parse import urlparse
from uuid import uuid4



##We have created a genesis block##
class Blockchain:
    def __init__(self):
        #constructor
        self.chain=[]
        self.transactions=[]
        self.nodes=set()
        
        #genesis block is created first time the constructor is made
        #proof is basically a condition that hash will be generated with what condition
        self.create_block(proof=1, previous_hash='0')
        
    def create_block(self,proof,previous_hash):
            #define data for the blocks
            block={'index': len(self.chain)+1,'timestamp':str(datetime.datetime.now()),
                  'proof':proof,
                  'previous_hash':previous_hash}
            ##this block is having data in dictionary form. For dictionary we use json format
            
            self.transactions=[]
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
    
    def is_chain_valid(self,chain):
        previous_block=chain[0]
        block_index=1
        while(block_index<len(chain)):
            block=chain[block_index]
            
            if block['previous_hash']!=self.hash(previous_block):
                return False
            previous_proof=previous_block['proof']
            new_proof=block['proof']
            new_proof=block['proof']
            hash_operation=hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4]!='0000':
                return False
            previous_block=block
            block_index+=1
        return True
    
    def add_transaction(self,sender,receiver,amount):
        self.transactions.append({'sender':sender,'receiver':receiver,'amount':amount})
        previous_block=self.get_previous_block()
        return previous_block['index']+1
    
    def add_nodes(self,address):
        parsed_url=urlparse(address)   #urlparse('http://127.0...) Urlparse break the url into diffeent components-scheme,netloc,path,query
        self.nodes.add(parsed_url.netloc) #adds another node to your network
            
        
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


##getting the chain of blocks
@app.route('/get_chain',methods=['GET'])
def get_chain():
    response={'chain':blockchain.chain,
             'length':len(blockchain.chain)}
    return jsonify(response),200

@app.route('/isvalid', methods=['GET'])
def is_valid():
    is_valid=blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response={'message':'The chain is valid'}
    else:
        response={'message':'The chain is invalid'}
    return jsonify(response),200

@app.route('/add_transaction',methods=['POST'])
def add_transsaction():
    json=request.get_json()
    transaction_keys=['sender','receiver','amount']
    if not all(key in json for key in transaction_keys):
        return 'Some values are missing',400
    index=blockchain.add-transaction(json['sender'],json['receiver'],json['amount'])
    response={'manage': f'The transaction has been added to block {index}'}
    return jsonify(response),201

@app.route('/connect_nodes',methods=['POST'])
def connect_nodes():
    json=request.get_json()
    nodes=json.get('nodes')
    if nodes is None:
        return "No nodes",400
    for node in nodes:
        blockchain.add_nodes(node)
    response={'message':'all nodes are now conneccted', 'Total number of nodes':list(blockchain.nodes)}
    return jsonify(response),201
    

    
app.run(host='127.0.0.1',port=5006)
