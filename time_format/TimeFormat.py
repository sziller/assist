"""Basic time formatting tool
by Sziller"""

import time


def timestamp(formatted: bool or float = True):
    """=== Function name: timestamp ====================================================================================
    Script returns an actual timestamp.
    :param formatted: bool - if true timestamp gets reformatted: YYYYMMDD-hhmmss. Also switches return type!!!
    :return: string or float depending on <formatted> switch.
    ============================================================================================== by Sziller ==="""
    systime = time.time()
    if formatted:
        return format_timestamp_raw(systime)
    else:
        return systime


def format_timestamp_raw(timestamp_raw: float):
    """=== Function name: format_timestamp_raw =========================================================================
    ============================================================================================== by Sziller ==="""
    det_systime = time.gmtime(timestamp_raw)
    as_year = time.strftime("%Y", det_systime)  # Actual String year
    as_month = time.strftime("%m", det_systime)  # Actual String month
    as_day = time.strftime("%d", det_systime)  # Actual String day
    as_hour = time.strftime("%H", det_systime)  # Actual String hour
    as_min = time.strftime("%M", det_systime)  # Actual String min
    as_sec = time.strftime("%S", det_systime)  # Actual String sec
    return as_year + as_month + as_day + "-" + as_hour + as_min + as_sec
