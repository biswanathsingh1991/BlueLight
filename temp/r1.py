class Biswa():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def firstname(self):
        return self.first_name

    def lastname(self):
        return self.last_name

    def fullname(self):
        return self.first_name + self.last_name


class Fathername():
    def __init__(self, father_name, mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def fathername(self):
        return "{} {}".format(self.father_name, self.mother_name)

class Noun():
    def __init__(self):
         print ("run")

    def plus(self):
        print("two")
        print("two")
        x = 2
        print(x, x)
        return 1+1



class Biswanth(Noun):
    # def __init__(self, father_name, mother_name, first_name, last_name):
    #     super().__init__(father_name, mother_name, first_name, last_name)

    def plus(self):

        super().plus()
        print("after ")
        y = 4 + x

        return y


t = Biswanth()
# k = Fathername("Chandan Singh", "kajal singh")
print(t.plus())
# print(k.fathername())
