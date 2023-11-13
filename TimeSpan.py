from datetime import datetime


class TimeSpan:

    def __init__(self, start_time, end_time):
        start: datetime
        end: datetime
        self.set_timespan(start_time, end_time)

    def __repr__(self):
        return f"TimeSpan({self.start.strftime('%H:%M')}, {self.end.strftime('%H:%M')})"

    def set_timespan(self, start_time, end_time):
        self.start = self._to_datetime(start_time)
        self.end = self._to_datetime(end_time)

    @staticmethod
    def _to_datetime(time):
        if type(time) is datetime:
            return time
        if type(time) is str:
            return datetime.strptime(time, "%H:%M")
        return None

    def __add__(self, timespan):
        if not ((timespan.start <= self.end <= timespan.end)
                or (self.start <= timespan.start <= self.end)):
            raise Exception("cant add separated timestamps")
        times = [self.start, self.end, timespan.start, timespan.end]
        start = min(times)
        end = max(times)
        return TimeSpan(start, end)

    def timespan(self):
        return self.start, self.end

    def delta(self):
        return self.end - self.start

    def safe_add(self, timespan):
        try:
            return self + timespan
        except Exception:
            return None
