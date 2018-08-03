class Contact(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name


john = Contact(first_name="John", last_name="Clark", phone_number="000 111 222", birth_year=1975, email="john@clark.es")
may = Contact(first_name="May", last_name="Valentine", phone_number="333 444 555", birth_year=1985, email="may@valentine.gr")
simon = Contact(first_name="Simon", last_name="Idiot", phone_number="666 777 888", birth_year=0, email="idiot@sem.rs")

print(john.get_full_name())

contacts = [john, may, simon]
num = 1

for contact in contacts:
    print("%s." % num)
    num += 1
    print(contact.first_name)
    print(contact.last_name)
    print(contact.phone_number)
    print(contact.birth_year)
    print(contact.email)
    print("\n")

class Parent(object):
    def __init__(self, first_name, middle_name = False, last_name = False):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
    def print_name(self):
        print(self.first_name)

class Child(Parent):
    def __init__(self, first_name, kindergarten, middle_name=False):
        Parent.__init__(self, first_name, middle_name)
        self.kindergarten = kindergarten

parent = Parent(first_name="Doron")
child = Child(first_name="MaliDoron", kindergarten="Lame")

child.print_name()
print(child.kindergarten)