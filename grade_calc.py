#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:31:48 2020

@author: rasmuskaarelkilp
"""
#10 % of marks scored from submission of Assignments
#70 % of marks scored from Test
#20 % of marks scored in Lab-Works
#1. score >= 90 : "A"
#2. score >= 80 : "B"
#3. score >= 70 : "C"
#4. score >= 60 : "D"
# 1. Jack's dictionary 
jack = { "name":"Jack Frost", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 
         
# 2. James's dictionary 
james = { "name":"James Potter", 
          "assignment" : [82, 56, 44, 30], 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72] 
        } 
  
# 3. Dylan's dictionary 
dylan = { "name" : "Dylan Rhodes", 
          "assignment" : [77, 82, 23, 39], 
          "test" : [78, 77], 
          "lab" : [80, 80] 
        } 
          
# 4. Jessica's dictionary 
jess = { "name" : "Jessica Stone", 
         "assignment" : [67, 55, 77, 21], 
         "test" : [40, 50], 
         "lab" : [69, 44.56] 
       } 
         
# 5. Tom's dictionary 
tom = { "name" : "Tom Hanks", 
        "assignment" : [29, 89, 60, 56], 
        "test" : [65, 56], 
        "lab" : [50, 40.6] 
      } 
name_list = [jack, james, dylan, jess, tom]
def averagegrade(name):
   # for nom in name:
        #count = 0
    mark = 0
    marks = []
    for grade in name["assignment"]:
        #count += 1
        mark += grade
        marks = []
        marks = marks.append(grade)
        #assign_mark = mark/len("assignment")*0.1
        #assign_mark = sum("assignment")*0.1
        #total_sum = sum(marks) 
        assign_mark = mark/len("assignment")
        assign_mark = float(assign_mark) 
    return assign_mark
       # assign_mark = mark/4*0.1
    for grade in name["test"]:
        #count += 1
        marks = []
        mark += grade
        #test_mark = mark/len("test")*0.7
        #test_mark = sum("test")*0.7
        #test_mark = mark/len("test")*0.7
       # test_mark = mark/2*0.7
    #return test_mark 
        marks = marks.append(grade)
        total_sum = mark/len("test")
        test_mark = float(total_sum) 
    return test_mark
    for grade in name["lab"]:
        #count += 1
        marks = []
        mark += grade
        #lab_mark = mark/len("lab")*0.2
        #lab_mark = sum("lab")*0.2
       # lab_mark = mark/2*0.2
    #return lab_mark
        marks = marks.append(grade)
        total_sum = mark/len("lab") 
        lab_mark = float(total_sum) 
    return lab_mark
    total_mark = assign_mark * 0.1 + test_mark * 0.7 + lab_mark * 0.2
    if total_mark >= 90:
        score = "A"
    elif total_mark  >= 80:
        score = "B"
    elif total_mark  >= 70:
        score = "C"
    elif total_mark >= 60:
        score = "D"
    else:
        score = "E"
    student_score = score
    student_grade = total_mark
   # print(student_score,student_grade,assign_mark,test_mark,lab_mark,total_mark)
    return student_score,student_grade,assign_mark,test_mark,lab_mark,total_mark
#student_grades = [averagegrade(name)]
print (averagegrade(jack))
print (averagegrade(jess))
print (averagegrade(james))
print (averagegrade(dylan))
print (averagegrade(tom))