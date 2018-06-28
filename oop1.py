class Student():
    pass

xiaoMing=Student()

class PythonStudent():
    name=None
    age=19
    course="Python"

    def doHomework(self):
        print('I am doing homework now.')
        print(self.name,self.age,self.course)
        return None

xiaoYue=PythonStudent()
print(xiaoYue.__dict__)
xiaoYue.name='小月'
xiaoYue.age=20
#xiaoYue.course='English'
xiaoYue.doHomework()
#类所有成员检查
print(xiaoYue.__dict__)


