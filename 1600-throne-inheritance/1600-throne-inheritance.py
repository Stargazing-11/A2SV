class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.isDead = set()
        self.king = kingName
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.isDead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def getChilds(parent, cur):
            cur.append(parent)
            
            for child in self.graph[parent]:
                getChilds(child, cur)
            return cur
        
        cur_order = []
        
        for child in getChilds(self.king, []):
            if child not in self.isDead:
                cur_order.append(child)
        
        return cur_order
        
        
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()