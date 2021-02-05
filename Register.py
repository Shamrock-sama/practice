# -*- coding:UTF-8 -*-
'''
This is a class frame of students registration
'''


class friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.greeting()
        self.save()

    def greeting(self):
        try:
            print("Welcome " + self.name + "!")
        except:
            print("Register error!")

    def save(self):
        try:
            file = open("friends.txt", 'a')
            file.writelines("Name: " + self.name + "; Age: " + self.age + '\n')
            file.close()
        except:
            print("Saving error!")


while True:
    exit = input("Do you want to add another input (y/n)?")
    if exit.lower() == 'n':
        break
    else:
        name = input("Your name: ")
        if name == "Exit":
            break
        try:
            age = int(input("Your age: "))
            if age == "Exit":
                break
            else:
                friends(name, age)
        except:
            print("Please input a valid value!")
