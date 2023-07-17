class Student:

    def shuru(self):
        a = 123
        return a

    def shuchu(self, b):
        print(b)


s1 = Student()

s1.shuchu(s1.shuru())
