import datetime
import json
from api import register_booking

class Booking:
    def __init__(self, name: str, start: datetime, end: datetime) -> None:
        if end <= start:
            raise ValueError
        
        self.room_name = name
        self.start = start
        self.end = end
        return
    
    @property
    def duration(self) -> int:
        return (self.end - self.start).seconds / 60
    
    @property
    def start_date(self) -> str:
        return self.start.date().isoformat()
    
    @property
    def end_date(self) -> str:
        return self.end.date().isoformat()
    
    @property
    def start_time(self) -> str:
        return self.start.time().isoformat()[:5]
    
    @property
    def end_time(self) -> str:
        return self.end.time().isoformat()[:5]
    
    def to_dict(self) -> dict:
        return {
            "room_name": self.room_name,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "duration": self.duration
        }

# def register_booking(booking: Booking) -> bool:
#     pass

def create_booking(room_name: str, start: datetime, end: datetime) -> str:
    print("Начинаем создание бронирования")
    booking = Booking(room_name, start, end)
    try:
        result = register_booking(booking)
        msg = "Бронирование создано" if result else "Комната занята"
    except:
        result = False
        msg = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")
    return json.dumps({
        "created": result,
        "msg": msg,
        "booking": booking.to_dict()
    })
