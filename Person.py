class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayname(self):
        print('hello my name is ' + self.name)


class Student(Person):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color

    def sayhaircolor(self):
        print('the color of my hair is ' + self.hair_color)
        