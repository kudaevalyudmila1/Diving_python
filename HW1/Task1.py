"""Треугольник существует только тогда, когда сумма любых двух
 его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
 Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
   Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
   то треугольника с такими сторонами не существует. Отдельно сообщить является 
   ли треугольник разносторонним, равнобедренным или равносторонним."""

a = int(input("Введите первую сторону треугольника"))
b = int(input("Введите вторую сторону треугольника"))
c = int(input("Введите третью сторону треугольника"))

if a > b + c or b > a + b or c > a + b:
    print(f"{a},{b},{c} не являются сторонами треугольника ")
    
elif a == b == c:
    print("треугольник равносторонний")

elif a == b != c or a == c != b or c == b != a:
    print("треугольник равнобедренный")

else:
    print("треугольник разносторонний")