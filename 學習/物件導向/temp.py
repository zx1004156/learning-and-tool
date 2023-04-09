class treeNode:
     def __init__(self, val):
         # 初始化節點
         self.val = val
         self.left = None
         self.right = None

    def insertLeft(self, val):
         # 如果要新增左邊節點，先檢查是否已存在，若左節點不存在則放入左節點
         if self.left == None:
             self.left = treeNode(val)
         # 如果左節點已經存在，則放入左節點的下一層左節點，這邊用遞迴的方式進行搜尋，直到可以讓入左節點為止
         else:
             self.left.insertLeft(val)
    
     def insertRight(self, val):
         # 新增右邊節點的方式則和新增左節點的方式相同
         if self.right == None:
             self.right = treeNode(val)
         else:
             self.right.insertRight(val)

# 執行方式
sampleTree = treeNode(5)
sampleTree.insertRight(7)
sampleTree.insertRight(8)
sampleTree.insertLeft(3)
sampleTree.insertLeft(2)
sampleTree.right.insertLeft(6)
sampleTree.left.insertRight(4)

