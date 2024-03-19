# try:
#     a=int(input("enter number:"))
#     b=int(input("enter numberB:"))
#     c=a/b
#     print(c)
# except:
#     print("zero not allowed")

# try:
#     a=int(input("enter number:"))
#     b=int(input("enter numberB:"))
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
# =================================================

from abc import ABC,abstractmethod

class parent(ABC):
    @abstractmethod
    def display(self):
        pass

class child(parent):
    def __init__(self,fn):
        self.firstName=fn
    def display(self):
        return self.firstName

class grandchild(parent):
    def __init__(self,cfn):
        self.grandc =cfn
    def didplay(self):
        return self.grandc


obj1=child("Sharad")
obj2=grandchild("Mahi")
print(child.display())
print(grandchild.display())



