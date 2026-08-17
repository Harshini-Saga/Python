class Person:
    def __init__(self,name:str,age:int,Id:str):
        self.name=name
        self.age=age
        self.Id=Id
    def profile(self):
        print(f"ID:{self.Id}")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class Student(Person):
    def __init__(self, name:str, age:int, Id:str,dept:str): 
        self.dept=dept
        super().__init__(name,age,Id)
    def get_percentage(self,marks):
        return sum(marks)/len(marks) 
    def get_dept_staff_data(self):
        super().profile()
        print(f"Department:{self.dept}")
class Employee(Person):
    def __init__(self,name:str,age:int,Id:str,dept:str,salary:int,role:str,subjects=[]):
        self.salary=salary
        self.role=role
        self.subjects=subjects
        self.dept=dept
        super().__init__(name,age,Id)
    def add_subject(self,new_subject):
        self.subjects.append(new_subject)
        return self.subjects
    def calculate_salary(self,bonus=0):
        return self.salary+bonus
    def remove_subject(self,subj_name):
        if subj_name in self.subjects:
            self.subjects.remove(subj_name)
    def profile(self):
        super().profile()
        print(f"Department:{self.dept}")
        print(f"Role:{self.role}")
        print(f"Salary:{self.salary}")
class University(Student,Employee):
    def __init__(self, uni_name):
        self.uni_name=uni_name
        self.courses=["Btech","MTech"]
        self.student_data={}
        self.emp_data={}
    def add_student(self,name,age,dept):
        sid=len(self.student_data)+1
        self.student_data[sid]=Student(name,age,str(sid),dept)
    def remove_student(self,sid):
        if sid in self.student_data:
            del self.student_data[sid]
    def add_employee(self,name,age,dept,role,salary,subjects):
        eid=len(self.emp_data)+1
        self.emp_data[eid]=Employee(name,age,str(eid),dept,salary,role,subjects)
    def remove_employee(self,eid):
        if eid in self.emp_data:
            del self.emp_data[eid]
    def search_student(self,sid):
        return self.student_data[sid]
    def search_employee(self,eid):
        return self.emp_data[eid]
u=University("JNTUH")
u.add_student("Harshini",21,"CSE")
u.add_employee("Madhu",35,"CSE","Professor",30000,["Python","C"])
s=u.search_student(1)
e=u.search_employee(1)
print("Student Details:")
s.profile()
print(f"Percentage:{s.get_percentage([90,85,88,66])}")
print()

print("Employee Details:")
e.profile()
print(f"Salary with bonus:{e.calculate_salary(10000)}")
e.add_subject("Java")
print(f"Subjects:{e.subjects}")