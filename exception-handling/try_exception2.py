class Main:
    def execute(self):
        try:
            name = input("Please input your name: ")
            
            gender = input("Please input your gender (f: female / m: male): ")
            gender = gender.lower()
                
            self.send_message(name, gender)
                
        except Exception as e:
            import traceback
            traceback.print_exc() # untuk mengetahui letak baris kode yg error
            print(f"Exception: {e}") # try catch
            
    def send_message(self, name, gender):
        try:
            first_word = self.get_gender(gender)
        except Exception as e:
            raise e # raise exception
        
        print(f"\nSend greeting message to {first_word}. {name}\n")
        
    def get_gender(self, gender):
        if gender == "m":
            return "Mr"
        elif gender == "f":
            return "Ms"
        else:
            raise Exception("Gender is not found!") # raise exception
    
m = Main()    
while True:
    m.execute()
    

# PARENT (def execute)
# +methodWithTryCatch()
# +tryCatchMethod()
# ^^^^
# CHILD (def send_message, def get_gender)
# +methodThatRaisesException()
# +methodThatRaisesException()

# tiap child class perlu RAISE EXCEPTION biar ditangkep sama parent class
# jadi intinya print(e) [sebutannya try catch] itu cuman di parent class, di child classnya pake raise e aja

# kalo misalnya kita print(e) lagi di child class, kita gabisa kustomisasi pesan errornya atau bahkan gak di return apa2