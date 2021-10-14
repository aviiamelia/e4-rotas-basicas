from flask import Flask
from datetime import datetime

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
    now = datetime.now()  # current date and time
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    if int(time[:2]) > 0 and int(time[:2]) < 12:
        return {
            'current_datetime': f'{date_time[:10]} {date_time[12:20]} AM',
            'message': 'Bom dia!'
        }
    elif int(time[:2]) > 12:
        return {
            'current_datetime': f'{date_time[:10]} {date_time[12:20]} PM',
            'message': 'Boa tarde!'
        }
    elif int(time[:2]) >= 18:
        return {
            'current_datetime': f'{date_time[:10]} {date_time[12:20]} PM',
            'message': 'Boa noite!'
        }


current_time()
