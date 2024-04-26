class Message:
    def __init__(self) -> None:
        self.__recepient = None
        self.message = None

m = Message()
m.message = "Hello"
print(m.__recepient)