"""
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""

# проверку правильности ввода длин не делаем, для простоты работаем с целыми положительными числами

a = int(input("\tВведите длину стороны A треугольника = "))
b = int(input("\tВведите длину стороны B треугольника = "))
c = int(input("\tВведите длину стороны C треугольника = "))

if a == b == c:
    print('Треугольник равносторонний')
elif a == b | a == c | b == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')