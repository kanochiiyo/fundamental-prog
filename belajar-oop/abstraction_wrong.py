from abc import ABC, abstractmethod

class Smartphone(ABC):
    @abstractmethod
    def operating_system(self):
        return "Operating System!"
    
    def touch(self):
        return "You can touch the phone"
    
class Xiaomi(Smartphone):
    def os(self):
        return "Xiaomi Operating System!"
    
x = Xiaomi()
result = x.os()
result_2 = x.touch()
print(result)
print(result_2)