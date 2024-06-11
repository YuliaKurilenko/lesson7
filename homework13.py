team1_num = "Мастера кода"
team2_num = "Волшебники данных"
print("В команде Мастера кода участников: %d!" % (5))
print(f"Итого сегодня в командах участников:  {5} и {6}!")
score_2 = 42
print("Команда Волшебники данных решила задач:{0:d}!".format(score_2))
team1_time = 18015.2
print( "Мастера кода решили задачи за {0:f}c!".format(team1_time))
team2_time = 2153.31451
print("Волшебники данных решили задачи за {0:f}c!".format(team2_time))
score_1 = 40
print(f"Команды решили {score_1} и {score_2}!")
tasks_total = 82
time_avg = 350.2
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = ('Победа команды Волшебники Данных!')
else:
    challenge_result = 'Ничья!'
print(f'"Результат битвы:{challenge_result}')

