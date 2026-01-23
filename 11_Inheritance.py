class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age

    def introduction(self):
        return f'My name is {self.firstName} {self.lastName} and I am {self.age} years old.'


class Student(Person):
    def __init__(self,firstName,lastName,age,studentID,major):
        super().__init__(firstName,lastName,age)
        self.studentID=studentID
        self.major=major


    def introduction(self):
        return f'{super().introduction()} my student ID is {self.studentID} and I major in {self.major}.'
    

student=Student('Adeel',"Haider",25,"S12345","Computer Science")

print(student.introduction())