
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, 我叫 {self.name} ，今年 {self.age} 岁")



user = Person('子羽','30')
user.greet()




class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        print(f"学号: {self.student_id}")


student1 = Student("张三", 20, "S12345")
student1.greet()  # 输出: Hello, 我叫 张三 ，今年 20 岁
student1.display()  # 输出: 学号: S12345


class Teacher(Person):
    def greet(self):
        print(f"Hello, 我是 {self.name} 教授")

teacher1 = Teacher("李春华", 40)
teacher1.greet()  # 输出: Hello, 我是 李春华 教授


class Car:

    brand = '宝马' # 类属性：公有属性

    def __init__(self, color):
        self.color = color
        self.__mile = 200000  # 私有
    def get_mile(self):  # 公有方法
        return self.__mile

car = Car('黄色')
print(car.brand) # 宝马
print(car.color) # 黄色
# print(car.__mile) # 'Car' object has no attribute '__mile'
print(car.get_mile()) # 200000