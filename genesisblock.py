v##We have created a genesis block##
class Blockchain:
    def __init__(self):
        #constructor
        self.chain=[]
        
        #genesis block is created first time the constructor is made
        
        self.create_block(proof=1, previous_hash='0')
        
        def create_block(self,proof,previos_hash):
            #define data for the blocks
            block={'index': len(self.chain)+1,'timestamp':str(datetime.datetime.now()),
                  'proof':proof,
                  'previous_hash':previous_hash}
            
            self.chain.append(block)
            return block
        
blockchain=Blockchain() #blockchain is an object of class Blockchain

