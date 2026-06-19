# Creating a dictionary
student = { "name": "Aravind", "age": 21,
    "course": "Python"
}
print(student)
print("\nName:", student["name"])
student["city"] = "Hyderabad"
print(student)
student["age"] = 22
print(student)
student.pop("course")
print(student)
print(student.keys())
print(student.values())
print(student.items())
