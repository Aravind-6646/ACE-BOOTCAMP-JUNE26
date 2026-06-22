class student:
    def __init__(self, name, branch, rno):
        self.name = name
        self.branch = branch
        self.rno = rno
    @classmethod
    def hike(cls):
        return "I am a class method..."
    def name(self):
        print(self.name)
    def __repr__(self):
        return f"student({self.name}, {self.branch}, {self.rno})"
    def __str__(self):
        return f"Name: {self.name}, Branch: {self.branch}, Rno: {self.rno}"
s1=student("sachin", "cse", 101)
s2=student("rahul", "ece", 102)
print(s1)
print(s2)
print(student.hike())        
