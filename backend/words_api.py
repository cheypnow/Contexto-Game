from datetime import datetime

words = [
    'teenager',
    'desire',
    'navy',
    'love',
    'error',
    'supermarket',
    'media',
    'technology',
    'girl',
    'disaster',
    'literature',
    'medicine',
    'promotion',
    'ability',
    'arise',
    'morale'
    'dilute',
    'enhance',
    'country',
    'drawing',
    'excitement',
    'painting',
    'insurance',
    'disk',
    'response',
    'church',
    'winner',
    'factory'
]


def get_today_word():
    day_of_year = datetime.now().timetuple().tm_yday
    return words[day_of_year % len(words)]
