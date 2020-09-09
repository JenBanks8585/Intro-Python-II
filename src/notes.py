
''' Example of INHERITANCE'''

class Student:
    def __init__(self, name):
        self.name = name

class Graduate(Student):
    def __init__(self, name, grad_date):
        super().__init__(name)
        self.grad_date = grad_date

grad1= Graduate('Jay Lennon', 'Dec 4 2010')
#print(grad1.name, grad1.grad_date)



''' Example of ASSOCIATION/COMPOSITION'''

class Duck:
    def __init__(self, name, bill_description, tail_length):
        self.name = name
        self.bill = Bill(bill_description)
        self.tail = Tail(tail_length)

    def about(self):
        print(f"This duck has a {self.bill.description}  bill and a {self.tail.length} tail.")


class Bill:
    def __init__ (self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


duck1= Duck("Quackers", "wide orange", "long")
duck1.about()



''' Example of AGGREGATION'''

class Duck2:
    def __init__(self, name, bill_description, tail_length, leash):
        self.name = name
        self.bill = Bill2(bill_description)
        self.tail = Tail2(tail_length)
        self.leash = leash

    def about(self):
        print(f"This duck has a {self.bill.description}  bill and a {self.tail.length} tail, and a pretty {self.leash.color} leash") 


class Bill2:
    def __init__ (self, description):
        self.description = description


class Tail2:
    def __init__(self, length):
        self.length = length


class Leash:
    def __init__(self, color):
        self.color = color

my_red_leash = Leash("red")
duck1= Duck2("Quackers", "wide orange", "long", my_red_leash)
duck2= Duck2("Feathers", "thin blue", "short", my_red_leash)
duck1.about()
duck2.about()