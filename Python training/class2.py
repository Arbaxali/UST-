import datetime
class Person:
    def __init__(self,name,surname, birthdate, address, phone, email):
        self.name = name
        self.surname =surname
        self.birthdate =birthdate
        self.addreess = address
        self.phone = phone
        self.email = email

    def age(self):
        today =datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


person = Person('Haroon','Baig',datetime.date(1999, 8, 8),
                        'No. 12 Random Street, Golflinks Villa, Dubai',
                        '9845448747', 'haroon.baig@example.com')



print(person.name)
print(person.email)
print(person.age())

