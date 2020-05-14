class Trie(object):

    def __init__(self):
        self.arr = []
        self.arr.append([])
        
        

    def insert(self, word):
        self.arr.append(word)
        
        

    def search(self, word):
        for x in self.arr:
            if(x==word):
                return True
       
        

    def startsWith(self, prefix):
        for x in self.arr:
            if(x[0:len(prefix)]==prefix):
                return True
        return False
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
