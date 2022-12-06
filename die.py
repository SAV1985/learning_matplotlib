from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die():
    '''Класс представляющий один кубик'''
    def __init__(self, num_sides=6):
        '''По умолчанию используется шестигранных кубик'''
        self.num_sides = num_sides
        
    def roll(self):
        '''Возвращает случайное число от 1 до числа граней'''
        return randint(1, self.num_sides)


die = Die()

'''Моделирование серии бросков с сохранением результатов в списке'''
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

'''Анализ результатов'''
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

'''Визуализация результатов'''
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling on D6 1000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6.html')