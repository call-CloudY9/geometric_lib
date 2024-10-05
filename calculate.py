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