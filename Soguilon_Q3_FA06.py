student = {}

student['name'] = str(input(">> Enter your name: "))
student['age'] = int(input(">> Enter your age: "))
student['subject'] = str(input(">> Enter your favorite subject: "))


print("\n|| Student record:")
print(">> Name: ", student.get('name'))
print(">> Age: ", student.get('age'))
print(">> Subject: ", student.get('subject'))
