# Модуль фитнес-трекера
Программный модуль фитнес-трекера, который обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания. 

Этот модуль должен выполнять следующие функции:
1)принимать от блока датчиков информацию о прошедшей тренировке,
2)определять вид тренировки,
3)рассчитывать результаты тренировки,
4)выводить информационное сообщение о результатах тренировки.

Информационное сообщение должно включать такие данные:
1)тип тренировки (бег, ходьба или плавание);
2)длительность тренировки;
3)дистанция, которую преодолел пользователь, в километрах;
4)среднюю скорость на дистанции, в км/ч;
5)расход энергии, в килокалориях.

Как запустить проект: 
Клонировать репозиторий и перейти в него в командной строке:

git clone <> 

Cоздать и активировать виртуальное окружение:

python3 -m venv env source env/bin/activate 

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip pip install -r requirements.txt
