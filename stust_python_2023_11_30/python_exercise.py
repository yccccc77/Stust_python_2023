class Student:
    def __init__(self, school_name, department, director_name, student_name, student_id, address, credits_earned, gpa):
        self._department = department  
        self._director_name = director_name  
        self._student_name = student_name 
        self._student_id = student_id  
        self._address = address  
        self._credits_earned = credits_earned 
        self._gpa = gpa
 
    def get_school_name(self):
        return self._school_name
 
    def set_school_name(self, value):
        self._school_name = value
 
    def get_department(self):
        return self._department
 
    def set_department(self, value):
        self._department = value
 
    def get_director_name(self):
        return self._director_name
 
    def set_director_name(self, value):
        self._director_name = value
 
    def get_student_name(self):
        return self._student_name
 
    def set_student_name(self, value):
        self._student_name = value
 
    def get_student_id(self):
        return self._student_id
 
    def set_student_id(self, value):
        self._student_id = value
 
    def get_address(self):
        return self._address
 
    def set_address(self, value):
        self._address = value
 
    def get_credits_earned(self):
        return self._credits_earned
 
    def set_credits_earned(self, value):
        self._credits_earned = value
 
    def get_gpa(self):
        return self._gpa
 
    def set_gpa(self, value):
        self._gpa = value
 
        st1 = Student("STUST", "NTS#1", "4B0G0173")
 
        print(st1.get_schoolName())
 
        st1.set_schoolName("南台科大")
        print(st1.get_schoolName())