class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '_main_':
            p1 = person("John", 25)
            print(p1.age)
            print(p1.name)