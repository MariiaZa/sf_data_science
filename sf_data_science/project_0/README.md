# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Результат)    
[6. Выводы](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Целое число от 0 до 100
  
:arrow_up:[к оглавлению](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Оглавление)


### Этапы работы над проектом  
В ходе реализации проекта было опробован алгоритм нахождения числа методом дихотомии - число для угадывания выбирается равным середине диапазона, при каждый раз диапазон для угадывания уменьшается в два раза.

:arrow_up:[к оглавлению](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Оглавление)


### Результаты:  
В среднем алгоритм, реализованный по методу дихотомии, угадывает число с 5 попытки. При этом максимальное количество попыток необходимое для угадываение - 7.

:arrow_up:[к оглавлению](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Оглавление)


### Выводы:  
Метод дихотомии позволяет угадывать число в среднем за 5 попыток.

:arrow_up:[к оглавлению](https://github.com/MariiaZa/sf_data_science/blob/main/sf_data_science/project_0/README.md#Оглавление)

