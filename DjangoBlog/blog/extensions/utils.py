from . import jalali
from django.utils import timezone


def convert_to_persian_digits(str_number:str):
    str_number = str(str_number)
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹‎'
    english_digits = '0123456789'
    for i in range(10):
        str_number = str_number.replace(english_digits[i], persian_digits[i])
        str_number = str_number.replace(arabic_digits[i], persian_digits[i])
    return str_number


def convert_to_jalali(time):
    time = timezone.localtime(time)
    str_time = '{}-{}-{}'.format(time.year, time.month, time.day)
    jyear, jmonth, jday = jalali.Gregorian(str_time).persian_tuple()
    j_months = ['فروردین','اردبیهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    out = '{} {} {} ساعت {:02d}:{:02d}'.format(
        jday,
        j_months[jmonth-1],
        jyear,
        time.hour,
        time.minute
    )
    return convert_to_persian_digits(out)