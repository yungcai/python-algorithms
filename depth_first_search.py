class Node:
    def __inti__(self,name): 
        self.children= []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def dfs(self,arr):
        arr.append(self.name)
        for child in self.children:
            child.dfs(arr)
            return arr