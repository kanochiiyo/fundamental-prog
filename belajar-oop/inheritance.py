# penurunan sifat
class Instrument:
    def music(self):
        print("Every music instrument has sound")

class Guitar(Instrument):
    def play(self):
        print("How to play guitar is just strum the guitar!")

class AcousticGuitar(Guitar):
    def sound(self):
        print("The sound of the acoustic guitar is very soft!")

ag = AcousticGuitar() # ini object (variabel yang menampung class)
ag.music()
ag.play()
ag.sound()

# kenapa AcousticGuitar() bisa menjalankan fungsi music dan play?
# karena AcousticGuitar() menurunkan sifat Guitar dan Guitar menurunkan sifat Instrument