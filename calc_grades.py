from sys import argv
from numpy import mean
class_dict = {
	"4390" : "Computer Networks",
	"4365" : "Artifical Intelligence",
	"4348" : "Operating System Concepts",
	"4384" : "Automata Theory"
}



class Class:
	def __init__(self,class_num):
		self.classname = class_dict[class_num]
		filename = class_num + "/grades/grades.txt"
		f = open(filename)
		self.data = f.read().split("\n")
		for i in xrange(len(self.data)):
			self.data[i] = tuple(self.data[i].split(":"))

		f.close()

	def get_grades(self):
		class_grade = 0
		for name, weight, grades in self.data:
			unweighted_grade = mean(map(float,grades.split(" ")))
			weighted_grade = float(weight) * unweighted_grade
			print name, "unweighted: ", unweighted_grade,"weighted:", weighted_grade
			class_grade += weighted_grade
		print "%s grade"%self.classname, class_grade


 
if __name__ == "__main__":
	grades = Class(argv[1])
	grades.get_grades()















