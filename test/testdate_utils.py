import unittest
from datetime import date

from dateutil.relativedelta import relativedelta

from resources import date_utils as dt


class MyTestCase(unittest.TestCase):
    def test_days_1day_diff(self):
        self.assertEqual(1,
                         dt.days_between(date(2023, 9, 22),
                                         date(2023, 9, 23)))
        self.assertEqual(1,
                         dt.days_between(date(2023, 12, 31),
                                         date(2024, 1, 1)))

    def test_days_1year_diff(self):
        self.assertEqual(366,
                         dt.days_between(date(2012, 2, 29),
                                         date(2013, 3, 1)))
        self.assertEqual(365,
                         dt.days_between(date(2012, 3, 1),
                                         date(2013, 3, 1)))
        self.assertEqual(366,
                         dt.days_between(date(2012, 2, 28),
                                         date(2013, 2, 28)))
        self.assertEqual(366,
                         dt.days_between(date(2011, 3, 1),
                                         date(2012, 3, 1)))
        self.assertEqual(365,
                         dt.days_between(date(2011, 2, 28),
                                         date(2012, 2, 28)))

    def test_days_in_month2(self):
        self.assertEqual(29, dt.monthrange(2024, 2)[1])
        self.assertEqual(28, dt.monthrange(2023, 2)[1])

    def test_diff_years_months_days(self):
        self.assertEqual(relativedelta(years=1), dt.diff_yymmdd('2025-2-28', '2024-2-29'))
        self.assertEqual(relativedelta(years=3, months=4, days=5),
                         dt.diff_yymmdd('2026-3-5', '2022-10-31'))
        self.assertEqual(relativedelta(), dt.diff_yymmdd('2025-2-28', '2025-2-28'))
        self.assertEqual(relativedelta(months=-2, days=-19), dt.diff_yymmdd('2022-9-15', '2022-12-4'))
        self.assertEqual(relativedelta(years=10, months=11, days=29),
                         dt.diff_yymmdd('2023-12-24', '2012-12-25'))
        self.assertEqual(relativedelta(months=11, days=30),
                         dt.diff_yymmdd('2013-1-29', '2012-1-30'))

    def test_custom_diff(self):
        self.assertEqual('0 years, 0 months, 0 days', dt.custom_diff('2012-12-12', '2012-12-12'))
        self.assertEqual('0 years, 0 months, 1 days', dt.custom_diff('2012-12-12', '2012-12-13'))
        self.assertEqual('1 years, 0 months, 1 days', dt.custom_diff('2012-12-12', '2013-12-13'))
        self.assertEqual('0 years, 0 months, 30 days', dt.custom_diff('2012-12-12', '2013-1-11'))
        self.assertEqual('0 years, 2 months, 30 days', dt.custom_diff('2012-12-12', '2013-3-11'))
        self.assertEqual('1 years, 0 months, 0 days', dt.custom_diff('2012-2-29', '2013-2-28'))
        self.assertEqual('2 years, 0 months, 25 days', dt.custom_diff('2012-2-29', '2014-3-25'))
        self.assertEqual('10 years, 11 months, 29 days', dt.custom_diff('2012-12-25', '2023-12-24'))
        self.assertEqual('0 years, 11 months, 30 days', dt.custom_diff('2012-1-30', '2013-1-29'))

    def test_diff_days(self):
        self.assertEqual('2021-01-01 1 0 0', dt.diff_days('2020-1-1', 366))
        self.assertEqual('2021-02-28 1 0 0', dt.diff_days('2020-2-28', 366))
        self.assertEqual('2021-02-28 1 0 0', dt.diff_days('2020-2-29', 365))
        self.assertEqual('2021-03-01 1 0 0', dt.diff_days('2020-3-1', 365))
        self.assertEqual('2021-03-31 1 1 2', dt.diff_days('2020-2-29', 396))


if __name__ == '__main__':
    unittest.main()
