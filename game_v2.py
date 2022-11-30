import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number: int=1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True: 
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count

def score_game(random_predict) -> int:
    """за какое количество в среднем попыток угадываем

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
    
if __name__ == '__main__':
    score_game(random_predict)
#print(f"Количество попыток: {random_predict(2)}")
