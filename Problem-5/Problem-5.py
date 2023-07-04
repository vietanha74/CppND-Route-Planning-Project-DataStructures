import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        previous_hash = None
        if self.head is not None:
            previous_hash = self.head.hash
        new_block = Block(timestamp, data, previous_hash)
        new_block.next = self.head
        self.head = new_block

    def display_chain(self):
        current_block = self.head
        while current_block:
            print("Block Hash:", current_block.hash)
            print("Timestamp:", current_block.timestamp)
            print("Data:", current_block.data)
            print("Previous Hash:", current_block.previous_hash)
            print()
            current_block = current_block.next

    def validate_integrity(self):
        current_block = self.head
        while current_block and current_block.next:
            current_hash = current_block.hash
            next_hash = current_block.next.previous_hash
            if current_hash != next_hash:
                return False
            current_block = current_block.next
        return True

# Test Case: Adding blocks to the blockchain
blockchain = Blockchain()
blockchain.add_block("Block 0")
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")

# Test Case: Displaying the blockchain
blockchain.display_chain()

# Test Case: Validating integrity
is_valid = blockchain.validate_integrity()
print("Is blockchain valid?", is_valid)