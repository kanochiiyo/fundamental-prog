from app_log import AppLog
import traceback


class Main:
    def execute(self):
        try:
            name = input("Please input your name: ")

            gender = input("Please input your gender (f: female / m: male): ")
            gender = gender.lower()

            self.send_message(name, gender)

        except Exception as e:
            AppLog().error(traceback.format_exc())

    def send_message(self, name, gender):
        try:
            first_word = self.get_gender(gender)
        except Exception as e:
            raise e

        print(f"\nSend greeting message to {first_word}. {name}\n")

    def get_gender(self, gender):
        if gender == "m":
            return "Mr"
        elif gender == "f":
            return "Ms"
        else:
            raise Exception("Gender is not found!")


m = Main()
while True:
    m.execute()