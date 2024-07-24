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

    emp_var ="This is an employee class "

    def __init__(self, name, age, gender, id, salary ) -> None:
        super().__init__(name, age, gender)
        self.id = id
        self.salary =salary

    def about_emp(self):
        print(self.name)
        print(self.id)
    def about_person(self):
        return super().about_person()   
    def emp_intro(self):
        print(f'Hi my name is {self.name}. I am {self.age}. My emp id is {self.id}') 


emp = Employee("ram", 20,'male', 124, 1000)
emp2 = Employee("shyam", 24,'male', 134, 2000)

print(emp.__class__.emp_var)
print(emp.age)
print(emp.about_emp())
print(emp.emp_intro())
print(emp.about_person())


print(emp2.__class__.emp_var)
print(emp2.age)
print(emp2.about_emp())
print(emp2.emp_intro())
print(emp2.about_person())
#-----------------------------------------------------------------------------------------------


 
person1= Person("ram", 20,'male' )
person2 = Person("shyam", 24,'male')
emp3 = Employee( person1.name,person1.age, person1.gender, 124, 1000)
emp4 = Employee( person2.name,person2.age, person2.gender,  134, 2000)

print('===================================')
print(emp3.__class__.emp_var)
print(emp3.age)
print('---------------')
print(emp3.about_emp())
print('---------------')
print(emp3.about_person())
print(emp3.emp_intro())

print('===================================')
print(emp4.__class__.emp_var)
print(emp4.age)
print('---------------')
print(emp4.about_emp())
print('---------------')
print(emp4.about_person())
print(emp4.emp_intro())