class Employee:
    def __init__(self, name, department):
            self.name = name
            self.department = department
    
    def printDetails(self):
        print(f'{self.name} works at {self.department} department')


e1= Employee("Sara","Sales")
e2= Employee("Gabriel","HR")

e1.printDetails()
e2.printDetails()





    