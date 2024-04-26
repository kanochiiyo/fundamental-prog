# berubah sesuai dengan kebutuhan (menyesuaikan siapa yang memanggil)
class Animal:
    def sound(self):
        return "Every animal has sound"
    
class Cat(Animal):
    def sound(self):
        return "meow!"
    
class Dog(Animal):
    def sound(self):
        return "woof!"
    
class Duck(Animal):
    def sound(self):
        return "quack!"
    
class Cow(Animal):
    def sound(self):
        return "moo!"

c = Cat()
result = c.sound()
print(result)
        
d = Dog()
result = d.sound()
print(result)
        
cow = Cow()
result = cow.sound()
print(result)
        
duck = Duck()
result = duck.sound()
print(result)

# kita menimpa fungsi yang ada di animal
# nama method yang sama menghasilkan fungsi yang berbeda