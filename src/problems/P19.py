#!/usr/bin/env python3
"""Counting Sundays"""
SUNDAY = 6


class Date(object):
    """Handles comparison of two dates in format DD/MM/YYYY"""
    def __init__(self, day, month, year):
        assert day in range(1, 32)
        assert month in range(1, 13)
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __eq__(self, other):
        return ((self.year == other.year) and
                (self.month == other.month) and
                (self.day == other.day))

    def __gt__(self, other):
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __str__(self):
        return "{0}/{1}/{2}".format(self.day, self.month, self.year)

class FirstOfMonths(object):
    """
    Allows iteration through the first date of each month between start_date
    and end_date.
    Days are numbered 0-6 corresponding to Monday-Sunday respectively.
    """
    def __init__(self, start_date, end_date):
        # we know that 1 Jan 1900 was a monday
        self.date = Date(1, 1, 1900)
        self.day_num = 0
        self.months = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
                       10: 31, 11: 30, 12: 31}
        # cache leap_year so that we only have to check for a leap year every
        # year, rather than every month
        self.leap_year = self.is_leap_year
        self.start_date = start_date
        self.end_date = end_date
        self.get_starting_day()

    def __iter__(self):
        """
        Allow iteration through the first days of each month between
        start_date and end_date. Yields the day number.
        """
        while self.date < self.end_date:
            yield self.day_num
            self.increment_month()

    def __str__(self):
        return str(self.date)

    def get_starting_day(self):
        """
        Find which day we are starting on. self.date will be incremented
        to self.start_date.
        """
        while self.date < self.start_date:
            self.increment_month()

    def increment_month(self):
        """
        Increments self.date and self.day_num to the first day of the next
        month.
        """
        self.day_num = (self.day_num + self.days_in_month(self.date.month)) % 7
        if self.date.month < 12:
            self.date.month += 1
        else:
            self.date.year += 1
            self.date.month = 1
            self.leap_year = self.is_leap_year

    def days_in_month(self, month):
        """
        Return the days in each month. For February, check if current year is
        a leap year.
        """
        if month == 2:
            if self.leap_year:
                return 29
            return 28
        return self.months[month]

    @property
    def is_leap_year(self):
        """
        Find out if we're in a leap-year
        """
        # leap years only occur on years divisible by 4
        if self.date.year % 4 == 0:
            if self.date.year % 100 == 0:
                if self.date.year % 400 == 0:
                    # century divisible by 400 is leap year
                    return True
                # century not divisible by 4 is not a leap year
                return False
            # divisible by 4 but not a century so it is a leap year
            return True
        # not divisible by 4 so not a leap year
        return False


if __name__ == '__main__':
    start_date = Date(1, 1, 1901)
    end_date = Date(31, 12, 2000)
    sunday_count = 0

    # iterate through each first-of-month day, incrementing sunday_count
    # if the day is a sunday
    firstofmonths = FirstOfMonths(start_date, end_date)
    for day in firstofmonths:
        assert firstofmonths.date < end_date
        if day == SUNDAY:
            sunday_count += 1

    print(sunday_count)

