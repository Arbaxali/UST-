class person:
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name : {0}'.format(self.name))
        print('age : {0}'.format(self.age))
        print('gender : {0}'.format(self.gender))    

class student(person):
    def __init__(self, name, age, gender,studentid,fees):
        person.__init__(self,name,age, gender)
        super().PersonInfo()
        self.studentid = studentid
        self.fees =fees

    def StudentInfo(self):
        super().PersonInfo()
        print('student id:')

        print('student id: {}'.format(self.studentid))  
        print('fees :{}'.format(self.fees))

stu_obj =student('Pooja',25,'female',12298,10000)
stu_obj.StudentInfo()              