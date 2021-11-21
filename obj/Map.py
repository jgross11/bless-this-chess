class Map:
    def __init__(self):
        self.internalMap = {}

    def put(self, key, value):
        self.internalMap[key] = value
    
    def get(self, key):
        return self.internalMap[key]

    def containsKey(self, key):
        return key in self.internalMap
    