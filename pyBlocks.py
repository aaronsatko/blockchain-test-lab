# import necessary libraries
import hashlib  # for hashing sha 256
import json  # for JSON encoding
import time  # for timestamping


# define the Block class to represent each block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # data stored in block
        self.previous_hash = previous_hash  # hash of previous block
        self.nonce = 0  # value added to the block during PoW

    # hash block using SHA-256
    def hash_block(self):
        sha = hashlib.sha256()
        # concatenate all relevant block attributes into a single string
        input_str = f'{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}'
        sha.update(input_str.encode('utf-8'))
        return sha.hexdigest()

    # method to print out block in a readable format
    def __str__(self):
        return (f"Index: {self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash_block()}\n")

    # static method to create genesis block
    @staticmethod
    def create_genesis_block():
        return Block(0, time.time(), 'Genesis Block', '0')

# proof-of-work function
def proof_of_work(block):
    proof = block.hash_block()
    while proof[:4] != '0000':
        block.nonce += 1
        proof = block.hash_block()
    return block

# function to create the next block in chain
def next_block(last_block):
    index = last_block.index + 1  # increment the index
    timestamp = time.time()  # set the timestamp to the current time
    data = f'Block: {index}'  # set the data to indicate the block's index
    previous_hash = last_block.hash_block()  # set the previous hash to the hash of the previous block
    block = Block(index, timestamp, data, previous_hash)  # create a new block with these values
    return proof_of_work(block)  # add a nonce to the block using proof-of-work

# function to create a new blockchain with a set number of blocks
def create_blockchain(num_blocks):
    blockchain = [Block.create_genesis_block()]  # create the first block (the genesis block)
    for i in range(1, num_blocks):
        block = next_block(blockchain[-1])  # create next block
        blockchain.append(block)  # add block
    return blockchain

# function to print out the entire blockchain to txt file 
def print_blockchain_to_file(blockchain):
    with open('blockchain.txt', 'w') as f:
        f.write("Blockchain:\n")
        for block in blockchain:
            f.write(str(block))

# visualize the blockchain with index, data, and hash values
def visualize_blockchain(blockchain):
    print("Blockchain Visualization:")
    for block in blockchain:
        print("Index:", block.index)
        print("Data:", block.data)
        print("Hash:", block.hash_block())
        if block.index < len(blockchain) - 1:
            print("↓")  # indicate the next block in the blockchain
        else:
            print()  # add a blank line at the end of the visualization


blockchain = create_blockchain(10)
print_blockchain_to_file(blockchain)

vB = visualize_blockchain(blockchain)
print(vB)

