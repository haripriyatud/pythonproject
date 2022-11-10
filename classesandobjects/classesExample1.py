class Employee:
    def __init__(self, name='', department='', salary=0, designation=''):
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_department(self):
        return self.department

    def set_department(self, x):
        self.department = x

    def get_salary(self):
        return self.salary

    def set_salary(self, x):
        self.salary = x

    def get_designation(self):
        return self.designation

    def set_designation(self, x):
        self.designation = x

    def print_details(self):
        print(f'{self.name} works at {self.department} department as a {self.designation} '
              f'with a salary of {self.salary}')

    def promote_employee(self,new_position, new_salary):
        self.set_designation(new_position)
        self.set_salary(new_salary)


e1 = Employee("Gabriel", "HR", 565600, 'HR Manager')

e1.promote_employee('Senior HR Manager', 600000)

e1.print_details()
