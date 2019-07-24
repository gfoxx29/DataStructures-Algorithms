import hashlib
from datetime import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
    	self.timestamp = timestamp
    	self.data = data
    	self.previous_hash = previous_hash
    	self.hash = self.calc_hash()

    def calc_hash(self):
	    sha = hashlib.sha256()
	    hash_str = self.data.encode('utf-8')
	    sha.update(hash_str)

	    return sha.hexdigest()


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        previous_hash = self.head.value.hash if self.head else None
        block = Block(datetime.now(), data, previous_hash)
        self.head = Node(block, self.head)


# Tests
block0 = BlockChain()
block0.append("Some Information")


block1 = BlockChain()
block1.append("Some Information")

block2 = BlockChain()
block2.append("Some Information")


print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)