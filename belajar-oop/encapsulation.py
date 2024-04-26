class Capsule:
    def __init__(self) -> None:
        self.__ingredient_1 = None
        self.__ingredient_2 = None
        # kenapa ada 2 underscore? karena menandakan var itu private (hanya bisa diakses di class itu sendiri)
        # kenapa dibikin jadi private? biar terorganisir

    def set_ingredient_1(self, ingredient_1:str):
        self.__ingredient_1 = ingredient_1

    def get_ingredient_1(self):
        return self.__ingredient_1
    
    def set_ingredient_2(self, ingredient_2:str):
        self.__ingredient_2 = ingredient_2

    def get_ingredient_2(self):
        return self.__ingredient_2

c = Capsule()
c.set_ingredient_1("600mg Paracetamol")
c.set_ingredient_2("600mg caffein")

print(c.get_ingredient_1)
print(c.get_ingredient_2)    