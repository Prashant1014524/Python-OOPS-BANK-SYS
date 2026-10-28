# OOPs 
class Factory:
    @staticmethod
    def Hello():
        print("Hello")
    # dender method 
    def __init__(self,material,zips,pock):
        self.material=material
        self.zips=zips
        self.pock=pock
    def show(self):
        print(f"your object details are{self.material},{self.pock},{self.zips}")
    # static method that doesnot need the self in the paramerer 
   


reebook=Factory("Leather",3,2);
campus=Factory("HardL",5,7);
# print(reebook.pock)
# print(campus.pock)
reebook.show()
