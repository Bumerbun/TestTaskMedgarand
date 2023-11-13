import unittest
import sys
from ScheduleCreating import ScheduleCreating
from TimeSpan import TimeSpan


class ScheduleCreatingTesting(unittest.TestCase):

    def test_main(self):
        data = [{'start': '10:30', 'stop': '10:50'},
                {'start': '18:40', 'stop': '18:50'},
                {'start': '14:40', 'stop': '15:50'},
                {'start': '16:40', 'stop': '17:20'},
                {'start': '20:05', 'stop': '20:20'}]
        working_hours = TimeSpan("09:00", "21:00")
        window_length = 30
        actual_result = ScheduleCreating(working_hours)\
            .timespans_from_list(data)\
            .get_schedule(window_length=window_length)

        result = [{'start': '09:00', 'stop': '09:30'}, {'start': '09:30', 'stop': '10:00'},
                  {'start': '10:00', 'stop': '10:30'}, {'start': '10:50', 'stop': '11:20'},
                  {'start': '11:20', 'stop': '11:50'}, {'start': '11:50', 'stop': '12:20'},
                  {'start': '12:20', 'stop': '12:50'}, {'start': '12:50', 'stop': '13:20'},
                  {'start': '13:20', 'stop': '13:50'}, {'start': '13:50', 'stop': '14:20'},
                  {'start': '15:50', 'stop': '16:20'}, {'start': '17:20', 'stop': '17:50'},
                  {'start': '17:50', 'stop': '18:20'}, {'start': '18:50', 'stop': '19:20'},
                  {'start': '19:20', 'stop': '19:50'}, {'start': '20:20', 'stop': '20:50'}]

        self.assertEqual(actual_result, result)

    def test_no_window(self):
        data = [{'start': '10:30', 'stop': '10:50'}, {'start': '14:40', 'stop': '15:50'}]
        working_hours = TimeSpan("09:00", "21:00")
        actual_result = ScheduleCreating(working_hours)\
            .timespans_from_list(data)\
            .get_schedule()

        result = [{'start': '09:00', 'stop': '10:30'}, {'start': '10:50', 'stop': '14:40'},
                  {'start': '15:50', 'stop': '21:00'}]

        self.assertEqual(actual_result, result)

    def test_impossible_window(self):
        data = [{'start': '10:30', 'stop': '10:50'}, {'start': '14:40', 'stop': '15:50'}]
        working_hours = TimeSpan("09:00", "21:00")
        window_length = sys.maxsize
        actual_result = ScheduleCreating(working_hours)\
            .timespans_from_list(data)\
            .get_schedule(window_length=window_length)
        result = []

        self.assertEqual(actual_result, result)

    def test_negative_window(self):
        data = [{'start': '10:30', 'stop': '10:50'}, {'start': '14:40', 'stop': '15:50'}]
        working_hours = TimeSpan("09:00", "21:00")
        window_length = -1
        actual_result = ScheduleCreating(working_hours) \
            .timespans_from_list(data) \
            .get_schedule(window_length=window_length)
        result = []

        self.assertEqual(actual_result, result)

    def test_no_data(self):
        data = []
        working_hours = TimeSpan("09:00", "21:00")
        window_length = 240
        actual_result = ScheduleCreating(working_hours) \
            .timespans_from_list(data)
        print(actual_result.schedule)
        actual_result = actual_result.get_schedule(window_length=window_length)
        result = [{'start': '09:00', 'stop': '13:00'}, {'start': '13:00', 'stop': '17:00'},
                  {'start': '17:00', 'stop': '21:00'}]

        self.assertEqual(actual_result, result)

    def test_invalid_working_hours(self):
        data = []
        working_hours = TimeSpan("11:00", "09:00")
        window_length = 240
        actual_result = ScheduleCreating(working_hours) \
            .timespans_from_list(data) \
            .get_schedule(window_length=window_length)
        result = []

        self.assertEqual(actual_result, result)

if __name__ == '__main__':
    unittest.main()
