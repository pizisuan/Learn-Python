class SchoolMember():
	"""代表任何学校里的学员"""
	def __init__(self, name,age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))

	def tell(self):
		"""告诉我有关我的细节。"""
		print('Name:"{}" Age:"{}"'.format(self.name,self.age),end = " ")


class Teacher(SchoolMember):
	"""代表一位老师。"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Initialized Teacher: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary:"{:d}"'.format(self.salary))
		

class Student(SchoolMember):
	"""代表一位学生"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))


t = Teacher("Mr.Pizi",40,30000)
s = Student("Suan",25,84)

#打印一行空白行
print()

members = [t,s]
for member in members:
	# 对全体师生工作
	member.tell()

# 输出
# (Initialized SchoolMember: Mr.Pizi)
# (Initialized Teacher: Mr.Pizi)
# (Initialized SchoolMember: Suan)
# (Initialized Student: Suan)

# Name:"Mr.Pizi" Age:"40" Salary:"30000"
# Name:"Suan" Age:"25" Marks: "84"
