from calendar import monthrange, isleap
from datetime import datetime

from dateutil.relativedelta import relativedelta


def days_between(d1, d2):
    return abs(d2 - d1).days


def days_in_month(year, month):
    return monthrange(year, month)


def diff_yymmdd(date1, date2, dateformat='%Y-%m-%d'):
    return relativedelta(datetime.strptime(date1, dateformat),
                         datetime.strptime(date2, dateformat))


def custom_diff(date1, date2):
    dates = [
        datetime.strptime(date1, '%Y-%m-%d'),
        datetime.strptime(date2, '%Y-%m-%d')
    ]
    first = min(dates)
    last = max(dates)

    years = last.year - first.year

    if last.month >= first.month:
        months = last.month - first.month
    else:
        months = 12 - first.month + last.month
        years -= 1

    if last.day >= first.day:
        days = last.day - first.day
    elif isleap(first.year) and first.day == 29 and last.month == 2 and last.day == 28:
        days = 0
    else:
        daycalc_month = first.month
        if last.month == first.month:
            daycalc_month = daycalc_month - 1 if last.month > 1 else 12
        days = monthrange(first.year, daycalc_month)[1] - first.day + last.day
        months -= 1
        if months < 0:
            months = 11
            years -= 1

    return '{0} years, {1} months, {2} days'.format(years, months, days)


def diff_days(begin_date, days_to_add):
    beg_dt = datetime.strptime(begin_date, '%Y-%m-%d')
    end_dt = beg_dt + relativedelta(days=days_to_add)
    yymmdd = relativedelta(end_dt, beg_dt)
    return '{0} {1} {2} {3}'.format(end_dt.strftime('%Y-%m-%d'), yymmdd.years, yymmdd.months, yymmdd.days)
