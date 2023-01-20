class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the student name is:",self.name)
a=student("Lopa")
a.show()