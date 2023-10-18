class Person:
    def __init__(self, first_name, last_name, title):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
    
    def formal_greeting(self):
        return " ".join((self.title, self.first_name, self.last_name))
    
class Student(Person):
    def rollcall_name(self):
        return ", ".join((self.last_name, self.first_name))
    
class Teacher(Person):
    def __init__(self, first_name, last_name, title):
        self.goes_by_first_name = False
        super().__init__(first_name, last_name, title)

    def greeting_for(self, other):
        if isinstance(other, Teacher):
            return self.first_name
        elif isinstance(other, Student):
            if self.goes_by_first_name:
                return self.first_name
            else:
                return " ".join((self.title, self.last_name))
        elif isinstance(other, Person):
            return super().formal_greeting()
            
def checks():
    p = Person("John", "Smith", "Mr.")
    s = Student("Sara", "Connor", "Ms.")
    t = Teacher("Nick", "Zufelt", "Dr.")
    t2 = Teacher("Clair", "Dahm", "Dr.")

    t.goes_by_first_name = True

    print(s.rollcall_name() == "Connor, Sara")
    print(t.greeting_for(p) == "Dr. Nick Zufelt")
    print(t.greeting_for(s) == "Nick")
    print(t.greeting_for(t2) == "Nick")
    print(p.formal_greeting() == "Mr. John Smith")
    print(t2.greeting_for(s) == "Dr. Dahm")

checks()
