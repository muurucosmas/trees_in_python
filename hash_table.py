class HashTable:
  def __init__(self,size=10):
    self.size = size
    self.table = [[] for _ in range(size)]
    # Each bucket is a list (chaining)
    # _ we use this to get empty lists 
  #1.add a simple hash function which converts strings to index that can be stored
  def _hash(self,key):
    return  hash(key) % self.size
  #so when inserting a hash there are key value pairs because it is like a dict
  def insert(self,key,value):
    index = self._hash(key)
    bucket = self.table[index]

    for i,(k,v) in enumerate(bucket):
      if k == key :
        bucket[i] = (key,value) # Update existing key
        return
    bucket.append((key,value)) # Insert new key-value pair

  def get(self,key):
    index = self._hash(key)
    bucket = self.table[index]

    for k,v in bucket:
      if k == key:
        return v 
      return  None
     
  def delete(self,key):
    index = self._hash(key)
    bucket = self.table[index]

    for i,(k,_) in enumerate(bucket):
      if k == key:
        del bucket[i]
        return True
    return False  

if __name__ == '__main__':
  ht = HashTable()

  ht.insert('apple',10)
  ht.insert('banana',20)
  ht.insert('orange',30)

  print("Get 'apple':",ht.get('apple'))
  print("Get 'banana':",ht.get('banana'))
  print("Get 'apple':",ht.get('apple'))

  ht.delete('banana')
  print("Get 'banana' after delete:",ht.get('banana'))

  ht.insert('apple',99)
  print("Get updated'apple:",ht.get('banana'))

  print("Hash Table Buckets:",ht.table)
  
  
