"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Метод для нахожения загаданного числа
    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.
    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number=1
    max_number=100
    predict_number = (min_number+max_number)//2
    while True:
        count += 1
        
        if number == predict_number:
            break
        elif predict_number < number:
            min_number = predict_number+1
            predict_number = (min_number+max_number)//2 
        elif predict_number > number:
            max_number = predict_number-1
            predict_number = (min_number+max_number)//2
        else:
            break
    return count

def score_game(random_predict) -> int:
    """За сколько в среднем попыток алгоритм угадывает число
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """

    count_ls = []  
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(250))   # загадали список чисел

    i=0
    for number in random_array:
        i+=1
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее число попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)

score_game(random_predict)

if __name__ == "__main__":
    # RUN
    score_game(random_predict)