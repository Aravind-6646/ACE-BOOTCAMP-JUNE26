class student:
    def __init__(self,name,branch,rno):
        self.name=name
        self.branch=branch
        self.rno=rno
    def name(self):
        print(self.name)
    @property
    def from_branch(self):
        return self.branch
    @from_branch.setter
    def from_branch(self,branch):
        self.branch=branch
    @from_branch.deleter
    def from_branch(self):       
        self.branch=None
s1=student("sachin", "cse", 101)
s2=student("rahul", "ece", 102)
s3=student("rohit", "mech", 103)
print(s1.from_branch) 
s1.from_branch="CSM"
print(s1.from_branch)
del from_branch
