class person:
    def __init__(self, name, age, gender):
        self.name =name
        self.age = age
        self.gender = gender
    def PersonInfo(self):
        print("Name of the personis {0}".format(self.name))
        print("age of the person is {0}".format(self.age))
        print("gender of the person is {0}".format(self.gender))

class employee(person):
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary        
        
    def employeeInfo(self):
        print("emp id {0}".format(self.empid))
        print("salary {0}".format(self.salary))

class fulltime(employee):
    def __init__(self, name, age, gender, empid, salary,WorkExperience):
        super().__init__(name, age, gender, empid, salary)
        self.WorkExperience = WorkExperience

    def FulltimeInfo(self):
        print('work experience {}'.format(self.WorkExperience))

class contractual(employee):
    def __init__(self, name, age, gender, empid, salary,ContractExpiry):
        super().__init__(name, age, gender, empid, salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print("contract expiry:{}".format(self.ContractExpiry))


print('contractual Employee details')
print('*****************************')

contr_obj =contractual('pooja',25,'female',12398,70000,'31-12-2022')
contr_obj.PersonInfo()
contr_obj.employeeInfo()
contr_obj.ContractInfo()


print('fulltime Employee details')
print('*****************************')

fulltime_obj =fulltime('pooja',25,'female',12398,70000,12)
fulltime_obj.PersonInfo()
fulltime_obj.employeeInfo()
fulltime_obj.FulltimeInfo()