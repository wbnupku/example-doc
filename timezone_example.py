import datetime
import pytz


def get_timezone_hour_diff(tz_str):
    import pytz
    tz = pytz.timezone(tz_str)
    delta = tz.utcoffset(datetime.datetime.now())
    return delta.seconds // 3600


def convert_timestamp(dt, tz_str):
    tz = pytz.timezone(tz_str)
    return tz.localize(dt).timestamp()