from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE = ('Тип тренировки: {training_type};'
               ' Длительность: {duration:.3f} ч.;'
               ' Дистанция: {distance:.3f} км;'
               ' Ср. скорость: {speed:.3f} км/ч;'
               ' Потрачено ккал: {calories:.3f}.'
               )

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action_numb: int = action
        self.duration_hour: float = duration
        self.weight_kg: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return (self.action_numb * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration_hour

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        train_info = InfoMessage(type(self).__name__,
                                 self.duration_hour,
                                 self.get_distance(),
                                 self.get_mean_speed(),
                                 self.get_spent_calories()
                                 )
        return train_info


class Running(Training):
    COEF_CAL_1: int = 18
    COEF_CAL_2: int = 20

    """Тренировка: бег."""

    def get_spent_calories(self):
        return ((self.COEF_CAL_1 * self.get_mean_speed()
                - self.COEF_CAL_2) * self.weight_kg / self.M_IN_KM
                * (self.duration_hour * self.MIN_IN_HOUR))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEF_CAL_SP_1: float = 0.035
    COEF_CAL_SP_2: float = 0.029

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height_cm: float = height

    def get_spent_calories(self) -> float:
        sports_walking = ((self.COEF_CAL_SP_1 * self.weight_kg
                          + (self.get_mean_speed()**2 // self.height_cm)
                          * self.COEF_CAL_SP_2 * self.weight_kg)
                          * (self.duration_hour * self.MIN_IN_HOUR))
        return sports_walking


class Swimming(Training):
    """Тренировка: плавание."""
    COEF_CAL_SW_1: float = 1.1
    COEF_CAL_SW_2: int = 2
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self):
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration_hour)

    def get_spent_calories(self):
        return ((self.get_mean_speed() + self.COEF_CAL_SW_1)
                * self.COEF_CAL_SW_2 * self.weight_kg)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train = {'SWM': Swimming,
             'RUN': Running,
             'WLK': SportsWalking
             }
    return train[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
