#1.	Define a class Student with instance variables roll no., name, semester, branch. 
# Also define instance member functions for user input data to set values of instance variables and 
# display student’s data.
class Student:
    def __init__(self, rollno, semester, branch):
        self.rollno = rollno
        self._semester = semester
        self._branch = branch
    
    @property
    def student(self):
        return self._semester, self._branch
    
    @student.setter
    def student(self, new_semester, new_branch):
        self._semester = new_semester
        self._branch = new_branch

Piyush = Student(1, "VII", "EXTC")
Piyush.student("VI","ETRX")

#Piyush = Student("VI","ETRX")

#print(f"Piyush is studing in {Piyush.semester} & his roll no. is {Piyush.rollno}, in {Piyush.branch} branch.")