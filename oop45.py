class HumanBeing:
    def __init__(self, N, H):
        self.name = N
        self.height = H
        
    def get_age(self):
        self.age=int(input("What Is Your Age"))

s = HumanBeing('Pranay',124)
s.name