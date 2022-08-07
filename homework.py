class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_massage(self):
        return (f'Тип тренировки: {self.training_type};'
                f' Длительность: {self.duration:.3f} ч.;'
                f' Дистанция: {self.distance:.3f} км;'
                f' Ср. скорость: {self.speed:.3f} км/ч;'
                f' Потрачено ккал: {self.calories:.3f}.'
                )


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dis = self.action * self.LEN_STEP / self.M_IN_KM
        return dis

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        train_info = InfoMessage(type(self).__name__,
                                 self.duration,
                                 self.get_distance(),
                                 self.get_mean_speed(),
                                 self.get_spent_calories()
                                 )
        return train_info


class Running(Training):
    koef_cal_1 = 18
    Koef_cal_2 = 20
    time_hour = 60
    """Тренировка: бег."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_spent_calories(self):
        run = (self.koef_cal_1 * self.get_mean_speed()
              - self.Koef_cal_2) * self.weight / self.M_IN_KM* (self.duration
              * self.time_hour)
        return run


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    koef_cal_sw_1: float = 0.035
    koef_cal_sw_2: float = 0.029
    time_hour: int = 60

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        sports_walking = (self.koef_cal_sw_1 * self.weight
                         + (self.get_mean_speed()**2 // self.height)
                         * self.koef_cal_sw_2 * self.weight) * (self.duration * self.time_hour)
        return sports_walking


class Swimming(Training):
    """Тренировка: плавание."""
    koef_cal_swim_1 = 1.1
    koef_cal_swim_2 = 2
    LEN_STEP = 1.38
    time_hour = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return (self.length_pool * self.count_pool
        / self.M_IN_KM / self.duration)

    def get_spent_calories(self):
       return ((self.get_mean_speed() + self.koef_cal_swim_1)
       * self.koef_cal_swim_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train = {'SWM': Swimming,
             'RUN': Running,
             'WLK': SportsWalking
             }
    return  train[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_massage())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
