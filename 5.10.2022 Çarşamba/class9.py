class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
    

print(Person.number_of_people)
p1 = Person("Merve")
print(Person.number_of_people)
p2 = Person("Oğuz Kaan")
print(Person.number_of_people)



