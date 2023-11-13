from datetime import timedelta

from TimeSpan import TimeSpan
from typing import List


class ScheduleCreating:

    def __init__(self, working_hours: TimeSpan):
        self.schedule: List[TimeSpan] = []
        self.working_hours = working_hours
        return

    def timespans_from_list(self, schedule: list):
        for timespan in schedule:
            self.add_timespan(TimeSpan(timespan["start"], timespan["stop"]))
        return self

    def add_timespan(self, timespan: TimeSpan):
        if timespan.start <= self.working_hours.start \
                or timespan.end >= self.working_hours.end:
            return None

        self.schedule.append(timespan)
        self.schedule.sort(key=lambda x: x.start)
        self.simplify_schedule()
        return self

    def simplify_schedule(self):
        if len(self.schedule) <= 1:
            return self
        schedule = []
        simplified = self.schedule[0]
        for timestamp in self.schedule[1:]:
            result = simplified.safe_add(timestamp)
            if result is None:
                schedule.append(simplified)
                simplified = timestamp
                continue
            simplified = result
        schedule.append(simplified)
        self.schedule = schedule
        return self

    def get_schedule(self, **kwargs):
        window_length: int = kwargs.get("window_length", None)

        schedule = self.reverse_schedule()
        do_strip = window_length is not None
        if window_length:
            window_length = window_length * 60
        result = []
        for timespan in schedule:
            if not do_strip:
                window_length = (timespan.end - timespan.start).total_seconds()
            strip_quantity = int((timespan.end - timespan.start).total_seconds() // window_length)
            for i in range(strip_quantity):
                result.append({'start': (timespan.start + timedelta(seconds=window_length * i)).strftime("%H:%M"),
                               'stop': (timespan.start + timedelta(seconds=window_length * (i+1))).strftime("%H:%M")})
        return result

    def reverse_schedule(self, **kwargs):
        inplace = kwargs.get("inplace", False)

        start = self.working_hours.start
        schedule = []
        for timestamp in self.schedule:
            schedule.append(TimeSpan(start, timestamp.start))
            start = timestamp.end
        schedule.append(TimeSpan(start, self.working_hours.end))
        if inplace:
            self.schedule = schedule
            return self
        return schedule
