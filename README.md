# FCAddon for pygame
Библиотека, добавляющая возможность создавать наборы фигур с коллизией.

Механика движения sin-cos, пока что дополняется.

## Начало работы
Скачайте пакет в папку с вашим проектом и добавьте его.
```
import figure
```
Создайте объект класса
```
example = Block() # либо example = Circle()
```

## Классы и их методы
### Figure (Родительский класс)

**Примечание**:

example - объект класса Figure

examples[i] - i-тый элемент array, состоящего из объектов example. Использование с циклом.

Родительский класс, отвечающий за генерацию фигур, используя дочерние классы и их механики

**Обновление экрана**
| Метод | Описание |
|---|---|
| ```example.update()``` | Обновляет экран, сколько раз задано в значении FPS от pygame |

**Коллизия**
| Метод | Описание |
|---|---|
| ```example.wall_collision()``` | Отскоки объекта от стен по размерам окна |
| ```examples[i].block_collision(examples[j])``` | Проверка на столкновение каждого объекта с каждым другим |

Пример использования **block_collision()**
```
for j in range(len(example)):
  if i != j:
    example[i].block_collision(example[j])
```
**Гравитация**
| Метод | Описание |
|---|---|
| ```example.gravity(x_boost, y_boost)``` | Устанавливает гравитацию |

Где (x_boost, y_boost) - гравитация по определенным осям. 

Коэффиценты [0 -> 1]

**Потеря скорости**
| Метод | Описание |
|---|---|
| ```example.loss_of_speed(loss)``` | Устанавливает количество потеряной скорости в процентном эквиваленте при каждом отскоке |

Где (loss) - количество потеряной скорости в процентном эквиваленте. 

Коэфиценты [0 -> 1]

**Скорость**
| Метод | Описание |
|---|---|
| ```example.speed(speed)``` | Устанавливает скорость передвижения объекта |

Где (speed) - количество пикселей, пройденных за кадр. 

Коэфиценты [-∞ -> +∞]


### Block (дочерний Figure)
```
example = Block(self, screen, x, y, width, height)
```

Где (screen) - pygame.display.set_mode(RESOLUTION),

(x, y) - размеры объекта

(width, height) - screen.get_width(), screen.get_height()

### Circle (дочерний Figure)
```
example = Block(self, screen, x, y, rad)
```

Где (screen) - pygame.display.set_mode(RESOLUTION),

(x, y) - размеры объекта

(rad) - радиус объекта.

**Примечание:**

rect() в pygame пишется из левой крайней точки, а circle() из центра.

Чтобы вписать окружность в квадрат стоит следовать формуле:

``` self.hrect = pygame.draw.rect(self.screen, self.color, (self.x-self.rad, self.y-self.rad, self.rad*2, self.rad*2), 250) ```,

что эквивалентно:

```self.hrect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)```


**Хитбоксы**
| Метод | Описание |
|---|---|
| ```examples[i].hitbox_update()``` | Ведет хитбоксы за объектами. |


## Примеры
Примеры написания можно найти в /examples (будет дополняться)

## License
MIT











