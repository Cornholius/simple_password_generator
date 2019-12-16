

class Gen:
    def __init__(self):
        self.number = "1234567890"
        self.letter = "qwertyuiopasdfghjklzxcvbnm"
        self.bigletter = self.letter.upper()

    def generate(self):
        list1 = list(self.number)
        list2 = list(self.letter)
        list3 = list(self.bigletter)
        password = []
        for i in list1, list2, list3:
            password.append(i)
        print(password)


q = Gen()
q.generate()
