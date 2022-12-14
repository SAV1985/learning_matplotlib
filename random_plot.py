from random import choice
import matplotlib.pyplot as plt


class RandowWalk():
    '''Класс для генерирования случайных блужданий'''
    def __init__(self, num_points=5000):
        '''Инициализация атрибутов блужданий'''
        self.num_points = num_points
        
        '''Все блуждания начинаются с точки (0, 0)'''
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        '''Шаги генерируются до достижения нужной длины'''
        while len(self.x_values) < self.num_points:
            
            '''Определение направления и длины перемещения'''
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            '''Отклонение нулевых перемещений'''
            if x_step == 0 and y_step == 0:
                continue
            
            '''Вычисление следующих значений х и у'''
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
        
while True:        
    rw = RandowWalk(50000)
    rw.fill_walk()

    '''Нанесение точек на диаграмму'''
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    '''Выделение первой и последней точек'''
    ax.plot(0, 0, c='green', edgecolors='none', s=100)
    ax.plot(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)
    '''Удаление осей'''
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Make another walk& (y/n): ")
    if keep_running == 'n':
        break