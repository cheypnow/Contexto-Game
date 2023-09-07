from datetime import datetime

words = [
    'error',
    'supermarket',
    'media',
    'technology',
    'girl',
    'disaster',
    'thing',
    'country',
    'literature',
    'medicine',
    'promotion',
    'ability',
    'excitement',
    'painting',
    'insurance',
    'disk',
    'response',
    'church',
    'drawing',
    'winner',
    'factory'
    'teenager',
    'desire',
    'navy',
    'love',
    'arise',
    'morale'
    'dilute',
    'admission',
    'enhance'
]


def get_today_word():
    day_of_year = datetime.now().timetuple().tm_yday
    return words[day_of_year % len(words)]
