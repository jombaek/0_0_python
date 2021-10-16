class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.
    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        # if hours < 0 or minutes < 0 or seconds < 0 or milliseconds < 0 or hours > 24:
        #     raise ValueError()
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
        
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
    def FormatTime(self, hours, minutes, seconds, milliseconds):
        newtime = Time()
        newtime.milliseconds = milliseconds % 1000
        newtime.seconds = (seconds + milliseconds // 1000) % 60
        newtime.minutes = (minutes + seconds // 60) % 60
        newtime.hours = (hours + minutes // 60) % 24
        return newtime        

    def Add(self, time):
        self.milliseconds += time.milliseconds
        self.seconds += time.seconds
        self.minutes += time.minutes
        self.hours += time.hours
        self = self.FormatTime(self.hours, self.minutes, self.seconds, self.milliseconds)
        
    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        return '{}:{}:{}:{}'.format(self.hours, self.minutes, self.seconds, self.milliseconds)

time = Time(25, 11, 12, 1)
print(str(time))
time.Add(Time(0, 0, 0, 1010))
print(str(time))