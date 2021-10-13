from flask import Flask
from time import gmtime, time

app = Flask(__name__)


@app.route('/')
def home():
    return {
        'data': "Hello Flask!"
    }


@app.route('/current_datetime')
def current_time():
    # (tm_year=2021, tm_mon=10, tm_mday=13, tm_hour=17, tm_min=21, tm_sec=4, tm_wday=2, tm_yday=286, tm_isdst=0)
    message = ''
    date = gmtime(time())
    if date[3] > 0 and date[3] < 12:
        return {
            'current_datetime': f'{date[2]}/{date[1]}/{date[0]} {date[3]}:{date[4]}:{date[5]} AM',
            'message': 'Bom dia!'
        }
    if date[3] > 12:
        return {
            'current_datetime': f'{date[2]}/{date[1]}/{date[0]} {date[3]-3}:{date[4]}:{date[5]} PM',
            'message': 'Boa tarde!'
        }


print(current_time())
