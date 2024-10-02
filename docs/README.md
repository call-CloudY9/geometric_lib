# Math formulas

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Общее описание решения
- Следующие функции вычисляют площадь и периметр фигур (круг, квадрат).
- Для каждой фигуры свой файл, где содержатся функции вычисляющие площадь и периметр данных фигур.

### circle.py
``` python 
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
``` python
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

### Docs added

> Thu Mar 4 14:55:29 2021 +0300, commit hash:
[17fad60351c9b4046bd398486fe6da5d9fab3662]

- Добавлен файл docs.

### Circle and square added

> Thu Mar 4 14:54:08 2021 +0300, commit hash:
[407db5bf4636a856f91eaf2868a9f2dc0994d68a]

- Добавлены файлы "Circle" и "Square".