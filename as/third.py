from datetime import datetime

class Event:
    def __init__(self, title, day, month, year, start_time, end_time):
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if start_time >= end_time:
            raise ValueError("Start time must be earlier than end time")

        self.title = title
        self.day = day
        self.month = month
        self.year = year
        self.start_time = start_time  
        self.end_time = end_time      

    def display_event(self):
        return f"{self.title} on {self.day}/{self.month}/{self.year} from {self.start_time} to {self.end_time}"

    def is_same_date(self, other_event):
        return (self.day == other_event.day and 
                self.month == other_event.month and 
                self.year == other_event.year)

def events_on_date(events, day, month, year):
    return [event.display_event() for event in events 
            if event.day == day and event.month == month and event.year == year]


event1 = Event("Doctor Appointment", 15, 3, 2025, "14:00", "15:30")
event2 = Event("Team Meeting", 15, 3, 2025, "16:00", "17:00")
event3 = Event("Family Dinner", 16, 3, 2025, "19:00", "21:00")

all_events = [event1, event2, event3]


for e in events_on_date(all_events, 15, 3, 2025):
    print(e)
