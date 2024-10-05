# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Общее описание решения
- Следующие функции вычисляют площадь и периметр фигур (круг, квадрат, треугольник), а также присутствует функция калькулятора.
- Для каждой фигуры свой файл, где содержатся функции вычисляющие площадь и периметр данных фигур, а также для функции калькулятора имеется свой файл.

### circle.py
```python 
import math

#вызывает библиотеку math

def area(r):
    '''
        Принимает число r, возвращает произведение чисел (Пи, r, r).
    '''
    return math.pi * r * r

def perimeter(r):
    '''
        Принимает число r, возвращает произведение чисел (2, Пи, r).
    '''
    return 2 * math.pi * r
```

### square.py
```python
def area(a):
    '''
        Принимает число a, возвращает квадрат числа a.
    '''
    return a * a
    
def perimeter(a):
    '''
        Принимает число a, возвращает произведение чисел (4, a).
    '''
    return 4 * a
```

### triangle.py
```python
def area(a, b, c):
    '''Функция принимает три числа (a, b, c), возвращает сумму чисел (a, b, c), деленную на 2'''
    return (a + b + c) / 2


def perimeter(a, b, c):
    '''Функция принимает три числа (a, b, c), возвращает сумму чисел (a, b, c)'''
    return a + b + c
```

### calculate.py 
```python 
import circle
import square

'''Импортирем модули "circle" и "square"'''

figs = ['circle', 'square']
funcs = ['perimeter', 'area']

'''Объявляем списки доступных фигур и функций'''

sizes = {}

'''Создаем словарь для хранения размеров фигур'''

def calc(fig, func, size):
	'''Создаём функцию для вычисления периметра или площади'''
	assert fig in figs
	'''Проверяем, что фигура допустима'''
	assert func in funcs
	'''Проверяем, что функция допустима'''

	'''Вычисляем результат с помощью динамического вызова метода'''
	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')
	'''Выводим результат'''


if __name__ == "__main__":
	'''Проверяем, запущен ли скрипт напрямую'''
	func = ''
	fig = ''
	size = list()
    '''Запрашиваем фигуру до тех пор, пока не введем допустимую'''
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	'''Запрашиваем функцию до тех пор, пока не введем допустимую'''
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	'''Запрашиваем размеры до тех пор, пока их количество не совпадет с необходимым'''
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
	'''Вызываем функцию для расчета'''
```

### Docs added

> Thu Mar 4 14:55:29 2021 +0300, commit hash:
[17fad60351c9b4046bd398486fe6da5d9fab3662]

- Добавлен файл docs.

### Circle and square added

> Thu Mar 4 14:54:08 2021 +0300, commit hash:
[407db5bf4636a856f91eaf2868a9f2dc0994d68a]

- Добавлены файлы "Circle" и "Square".