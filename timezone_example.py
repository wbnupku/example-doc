import datetime

def get_timezone_hour_diff(tz_str):
    import pytz
    tz = pytz.timezone(tz_str)
    delta = tz.utcoffset(datetime.datetime.now())
    return delta.seconds // 3600