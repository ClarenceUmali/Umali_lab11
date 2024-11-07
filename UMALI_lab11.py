gradeList = []
studentGrade = 1

while studentGrade < 6:
    gradeInput = float(input(f"Enter grade {studentGrade}"))
        
    if 40 <= gradeInput <= 100 :
            gradeList.append(gradeInput)
            studentGrade += 1
    else:
        print("Invalid input.")
        
gradeAverage = sum(gradeList) / len(gradeList)  

passing = 0
for gradeInput in gradeList:
    if gradeInput >= 75:
        passing += 1
        
passingPercent = (passing / len(gradeList)) * 100

print(f"Grades: " , gradeList)
print(f"Grade Average: " , gradeAverage)
print(f"Passed Grade: ", passing)
print(f"Percentage: " , passingPercent)
      
    
            
                
            
                
        
    
        
        
    

    

    
    
            
    