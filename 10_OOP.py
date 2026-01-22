class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def describe(self):    #self is neccessary to  put as first parameter in method
        return f'{self.name} makes {self.sound} sound'

Animal1=Animal("cow","mooo")

Animal1.color="white"

print(Animal1.name)
print(Animal1.sound)
print(Animal1.color)

print(Animal1.describe())