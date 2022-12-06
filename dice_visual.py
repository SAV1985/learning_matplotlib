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


die_1 = Die()
die_2 = Die(10)

'''Моделирование серии бросков с сохранением результатов в списке'''
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

'''Анализ результатов'''
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

'''Визуализация результатов'''
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D6 1000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d6.html')