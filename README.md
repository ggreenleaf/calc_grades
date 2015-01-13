python script for calculating the grades of the a class

formatting grades file
	The grades file is formatted so the 
	assignment type is listed first
	then the weight of the assignemnt
	then grades sepereated by spaces in the next section
	each section is seperated by a ':'

	for example if you had a class that had this grading structure
	homework 5 assignments 20%
	Exam 1 20%
	Exam 2 20%
	Exam 3 20%
	Final 20%

	then it would like this in the grades.txt file

	homework:.20:0 0 0 0 0 #number of homework assignments
	Exam 1:.20:0
	Exam 2:.20:0
	Exam 3:.20:0
	Final:.20:0

Running the script
	Running the script requires a argument to the directory where the class information and the class directory has the grades/ directory which holds the grades.txt file

	for example 4 classes 4390,4365, 4384, 4348 would have the structure

	spring15
		calc_grades.py
		4390
			grades
				grades.txt
		4384
			grades
				grades.txt
		4348
			grades
				grades.txt
		4365
			grades
				grades.txt

	running the script to see grades for class 4390 would like this 
	python calc_grades.py 4390
	

Future: 
	add support for another file classes.txt which can 
	be used to look up the class name from the directory passed


