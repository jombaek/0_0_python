class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.
    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        if hours < 0 or minutes < 0 or seconds < 0 or milliseconds < 0:
            raise ValueError
        
        self.hours = (hours + (minutes + (seconds + milliseconds // 1000) // 60) // 60) % 24
        self.minutes = (minutes + (seconds + milliseconds // 1000) // 60) % 60 
        self.seconds = (seconds + milliseconds // 1000) % 60
        self.milliseconds = milliseconds % 1000
    def GetHour(self):
        return self.hours
    def GetMinute(self):
        return self.minutes
    def GetSecond(self):
        return self.seconds
    def GetMillisecond(self):
        return self.milliseconds
    # Прибавляет указанное количество времени к текущему объекту.
    # После выполнения этой операции параметры времени должны остаться корректными.
    def Add(self, time):
        self.hours = (self.hours + time.hours + (self.minutes + time.minutes + (self.seconds + time.seconds + (self.milliseconds + time.milliseconds) // 1000) // 60) // 60) % 24
        self.minutes = (self.minutes + time.minutes + (self.seconds + time.seconds + (self.milliseconds + time.milliseconds) // 1000) // 60) % 60 
        self.seconds = (self.seconds + time.seconds + (self.milliseconds + time.milliseconds) // 1000) % 60
        self.milliseconds = (self.milliseconds + time.milliseconds) % 1000
    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        return '{:02}:{:02}:{:02}.{}'.format(self.hours, self.minutes, self.seconds, self.milliseconds)

time = Time(25, 9, 1, 1)
print(str(time))
time.Add(Time(0, 0, 1, 1010))
print(str(time))