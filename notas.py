import numpy
studentGrades = [55, 12, 77, 88, 99]

def calculateAvg(grades):
  sum = sum(grades)
  average = sum / len(grades)
  return average

result = calculateAvg(studentGrades)

isApproved = "Aprobado" if result >= 60 else "Reprobado"

print(f'El promedio de las notas del estudiantes es {result}. Por lo que ha {isApproved} el curso.')

