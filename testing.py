from ScheduleCreating import ScheduleCreating
from TimeSpan import TimeSpan


if __name__ == '__main__':

    busy = [{'start': '10:30', 'stop': '10:50'},
            {'start': '18:40', 'stop': '18:50'},
            {'start': '14:40', 'stop': '15:50'},
            {'start': '16:40', 'stop': '17:20'},
            {'start': '20:05', 'stop': '20:20'}]

    print(ScheduleCreating(TimeSpan("09:00", "21:00")).timespans_from_list(busy).get_schedule(window_length=30))
