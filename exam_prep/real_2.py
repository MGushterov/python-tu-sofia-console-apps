class Employee:
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age

    def display_info(self):
        return f''' 
---------------
Employee: {self.fname} {self.lname}
Identification number: {self.i_num}
Education level: {self.education_level}

Employee has {self.work_experience} years of work experience, is {self.age} years of age and earns {self.salary} lv.
---------------'''

    def bonus(self):
        if self.education_level == 'Висше':
            emp_bonus = 0.05 * self.salary
        elif self.education_level == 'Средно':
            emp_bonus = 0.02 * self.salary
        else:
            emp_bonus = 0

        emp_bonus += self.work_experience * self.salary * 0.012
        return emp_bonus


employee_list = []
employees_count = int(input('Enter employees count: ')
    for i in range(len(employee_list)):
        i_num = int(input('Enter Identification number: '))
        fname = input('Enter employee name: ')
        lname = input('Enter employee surname: ')
        work_experience = int(input('Enter employee work experience: ')
        education_level = input('Enter employee education level: ')
        salary = float(input('Enter employee salary:'))
        age = int(input('Enter employee age: '))

        new_employee = Employee(i_num, fname, lname, work_experience, education_level, salary, age)
        employee_list.append(new_employee)


def sort_employee(employee_list):
    for i in range(employees_count):
        for j in range(employees_count):
            if employee_list[i].age > employee_list[j].age:
                employee_list[i], employee_list[j] = employee_list[j], employee_list[i]

    for el in employee_list:
        print(el.display_info())


sort_employee(employee_list)


def search_by_name(employee_list, fname, lname):
    for emp in employee_list:
        if emp.fname == fname and emp.lname == lname:
            return emp.display_info()

    return 'NOT FOUND!'


fname = input('Enter a name: ')
lname = input('Enter a surname: ')

print(search_by_name(employee_list, fname, lname))


def print_by_education_experience(employee_list, education, experience):
    for emp in employee_list:
        if emp.education_level == education and emp.work_experience == experience:
            print(emp.display_info)


education = input('Enter education level: ')
experience = input('Enter work experience: ')

print_by_education_experience(employee_list, education, experience)


def remove_employee(employee_list, i_num):
    for emp in employee_list:
        if emp.i_num == i_num:
            employee_list.remove(emp)
            return 'information deleted !!!'
    return 'Wrong i_num !!!'


i_num = int(input('Enter i_num: ')
print(remove_employee(employee_list, i_num))