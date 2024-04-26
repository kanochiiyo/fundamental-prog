from abc import ABC, abstractmethod

class Smartphone(ABC):
    @abstractmethod
    def operating_system(self):
        return "Operating system"
    def touch(self):
        return "You can touch the phone"

class Xiaomi(Smartphone):
    def operating_system(self):
        return "Xiaomi OS"
    
class Realme(Smartphone):
    def operating_system(self):
        return "Realme OS"

r = Realme()
result = r.operating_system()
result2 = r.touch()
print(result)
print(result2)

x = Xiaomi()
result = x.operating_system()
result2 = x.touch()
print(result)
print(result2)

# perbedaan abstraction dan inheritance adalah 
# kalo kita menurunkan sifat dari class abstraction maka kita juga harus bikin fungsinya di class yang menurunkan abstraction tsb
# beda sama inheritance yang gak perlu membuat fungsi lagi di class yang menurunkan