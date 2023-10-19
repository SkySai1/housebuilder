import drawsvg as draw
import random

def housebuilder(maxwidth, maxheight): 
    rows = []
    for row in range(random.randint(2,10)):
        current_width = 0
        blocks = []
        while True:
            house = House() # < - Инициализация класса Дом
            house.build() # <- Строим дом
            if current_width >= int(maxwidth) * 0.9: break
            blocks.append(house.svg) # <- Формируем список SVG кодов домов
            current_width += house.width
        rows.append(blocks)
    return rows

# -- Объявляем класс Дом
class House:
    svg = None

    def __init__(self) -> None:
        self.scale = random.randint(30,100)/10 # <- При инциаилаизации класса случайный размер
        self.rndcolor = lambda: random.randint(0,255) # <- При построении элмента дома выбирается случаный цвет элемента
        self.width = 10*self.scale # <- Задаём ширину полотна
        self.height = 20*self.scale # <- Задаём высоту полотна

    def build(self):
        self.svg = random.choice([self.classic])()

    def classic(self):
        x = self.scale

        d = draw.Drawing(self.width, self.height, origin='bottom-right')
        # Рисуем основание дома
        d.append(draw.Lines(-10*x, -3*x,
                            0, -3*x,
                            0, -10*x,
                            -10*x, -10*x,
                            -10*x, -3*x,
                            close=True,
                    fill='#%02X%02X%02X' % (self.rndcolor(),self.rndcolor(),self.rndcolor()),
                    stroke='black'))  

        # Рисуем трубу
        d.append(draw.Lines(-1*x, -10*x,
                            -1*x, -14*x,
                            -2*x, -14*x,
                            -2*x, -10*x,
                            close=True,
                            fill='#%02X%02X%02X' % (self.rndcolor(),self.rndcolor(),self.rndcolor()),
                            stroke='black'
        ))

        # Рисуем крышу
        d.append(draw.Lines(-10*x, -10*x,
                            -5*x, -16*x,
                            0, -10*x,
                            close=True,
                            fill='#%02X%02X%02X' % (self.rndcolor(),self.rndcolor(),self.rndcolor()),
                            stroke='black'
        ))

        # Рисуем окно на чердаке
        d.append(draw.Circle(-5*x, -12*x, 1.5*x,
                            fill='#%02X%02X%02X' % (self.rndcolor(),self.rndcolor(),self.rndcolor()),
                            stroke='black'
        ))

        # Рисуем окно в доме
        d.append(draw.Lines(-9*x, -6*x,
                            -6*x, -6*x,
                            -6*x, -9*x,
                            -9*x, -9*x,
                            close=True,
                    fill='#%02X%02X%02X' % (self.rndcolor(),self.rndcolor(),self.rndcolor()),
                    stroke='black'))      

        return d.as_svg()
