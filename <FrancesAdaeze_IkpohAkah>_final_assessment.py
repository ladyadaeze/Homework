'''
Task 1

Design a parent class called CFGStudent. It should have general attributes like name, surname, age,
email, student id and methods to fetch student’s full name and student’s id.

Important: there should be an option to pass student id when a new class object is generated,
HOWEVER, if no id is passed, then student_id should be automatically generated and assigned to the class.
Design a child class called NanoStudent, which inherits from CFGStudent class. This class should
have exactly the same attributes as its parent class, as well as additional two called
‘specialization’ and ‘course grades’.

The child class ‘generate_id’ method should override its parent method to add the su   x ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added. Please
see the skeleton structure in the ﬁnal_assessment.py ﬁle. You can use it as a skeleton code for
your classes OR adjust it and create your own.

SEE ADDITIONAL COMMENTS in the ﬁle.
'''




class CFGStudent:

    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id


    def student_id(self):
        pass

    @staticmethod
    def generate_id(self):
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "

    def get_id(self, student_id):
        return f"The student id of {self.name} is {student_id}"

    def get_fullname(self, name, surname):

        return f"Name: {self.name}, Surname: {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, specialization, course_grades):
        self.specialization = specialization
        self.course_grades = course_grades
        return super().student_id()

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

    def add_new_grade(self, course_grades):
        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self, course_grades):
        'your code goes here'
        'fetch course grades container and its values'

'''
2. Start with writing a stand alone function that can return n’th Fibonacci number
  List comprehension can be useful here
  
  TASK 2
Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0



 
'''

'''
Task 3


Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

#### TESTS ###

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE


'''
array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

class Program:
    
'''
Task 4
1. The method 'save_employee' is not complete.
It should say 'def save_employee(self, deb_engine, name, active_status, department, id):'
2. The 1st attribute of the class save_employee should not have 2 methods assigned to it.
It should say 'self.db_engine' not 'self.db_engine.save'
3.The attributes of save_employee should not have a comma after each one
4.The update_status attribute is wrong. It should say 'self.new_is_active = new_is_active'. 
Instead it currently says self.active_status = new_is_active.
5.The update_department attribute is also wrong. It should say 'self.department_name = department_name'. 
Instead it currently says self.department = department_name.
6. The method 'remove_employee' is not complete. It should say 'def remove_employee(self, db_engine, name, id)'
7. The 'remove_employee' should not call 2 methods 'self.db_engine.delete' and should not put the attributes (self.name and self.id) in brackets
8. The SOLID principles can be added as follows:

Single Responsibility : There shouldn't be more than one seperated piece of code with the class Employee
Open and close : Class Employee should have a child class. The are to many methods within this one class. The code should be extended but not modified
Listov substitution : There should be some modification of extended behaviour after a subclass has been created.
Interface segregation : The interface should be split into smaller interfaces
Dependancy Inversion : If a child class is made, it should be instantiated to the adult class.

'''
