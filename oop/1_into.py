baseSalary =10000
overtime = 10
rate = 20


def normal_func(baseSalary , overtime, rate):
    return baseSalary +(overtime* rate)


# doing same with oops 

class employee:
    # class atribute 
    baseSalary =10000

    #Instance atrribute
    def __init__(self,rate) -> None:
        self.overtime = 10
        self.rate = rate

    def normal_fun_in_oops(self):
        return baseSalary +(overtime* rate)



# Driver code
# Object instantiation
emp=employee(20)


# accessing attribute 
emp.__class__.baseSalary


# Accessing instance attributes
emp.rate

print(f'class atribute base sal {emp.baseSalary}')
print(f'instance atribute overtime {emp.overtime}')
print(f'instance atribute rate {emp.rate}')
print(f'function out {emp.normal_fun_in_oops()}')


