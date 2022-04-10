
class Student(object):
    def __init__(self,name,gender,tell):
        self.name=name
        self.gender=gender
        self.tell=tell
    def __str__(self):
        return f"{self.name},{self.gender},{self.tell}"
