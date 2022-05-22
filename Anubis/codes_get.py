import re
from datetime import datetime


def get_code_automatic(self, person_type):
    date = datetime.today()

    if person_type == 'SystemUser':
        code = 'US'
        number = '%06d' % int(get_number(self))
    else:
        code = 'XX'
        number = 0

    year = str(date.year)
    month = str('%02d' % date.month)

    mount_code = code + '-' + year + '-' + month + '-' + number

    return mount_code


def get_number(self):
    date = datetime.today()

    provider = self

    if provider is None:
        year = str(date.year)
    else:
        match_year = re.search(re.compile("(\d{4})"), provider.code)
        year = match_year.group(0)

    if provider is None:
        number = 1
    else:
        if str(date.year) == year:
            match_number = re.search(re.compile("(\d{6})"), provider.code)
            number = int(match_number.group(0)) + 1
        else:
            number = 1

    return number
