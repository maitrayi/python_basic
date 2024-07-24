class Person() :


    def __init__(self, name , age , gender ) -> None:
        self.name = name 
        self.age = age 
        self.gender = gender 
    
    def about_person(self) :
        print(self.name)
        print(self.gender)
        print(self.age)
    def person_intro(self): 
        print(f'Hi my name is {self.name}. I am {self.age} years {self.gender}')


class Employee(Person): 
    def __init__(self, name, age, gender, id, salary ) -> None:
        super().__init__(name, age, gender)
        