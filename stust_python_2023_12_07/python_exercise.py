

class Student:

    def __init__(self,name,age,student_id,gpa):
        self.name=name
        self.age=age
        self.student_id=student_id
        self.gpa=gpa


    @property
    def student_name(self):
        print(f'"{self.name}"was accessed.')
        return self.name

    @student_name.setter
    def student_name(self,value):
        print(f'"{self.name}"is now"{value}".')
        self.name=value

    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}"was deleted')
        del self.name


def display_stust_info(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Student ID:",self.student_id)
    print("CPA:",self.gpa)


if __name__=="__main__":
    student1=Student("John Doe",20,"S12345",3.5)

    print(student1.student_name)
    student1.student_name="Peter Pan"
    del student1.student_name





