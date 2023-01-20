class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print("the student name is ", self.name,"and student number is ", self.rollno)
test1=Student("Lopamudra",25)
test1.show()
