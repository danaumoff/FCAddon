# FCAddon for pygame
Библиотека, добавляющая возможность создавать наборы фигур с коллизией.

## Начало работы
Скачайте пакет в папку с вашим проектом и добавьте его.
```
import Figure
```
Создайте объект класса
```
example = Figure()
```

## Классы и их методы
### Figure (Родительский класс)

Примечание:

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


### Block, Circle (дочерние Figure)
```
example = Circle()
example = Block()
**Хитбоксы**
| Метод | Описание |
|---|---|
| ```examples[i].hitbox_update()``` | Ведет хитбоксы за объектами. |


## Примеры
Примеры написания можно найти в /examples (будет дополняться)

## License
MIT











