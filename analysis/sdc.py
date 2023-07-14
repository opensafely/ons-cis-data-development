"""Statistical Disclosure Control (SDC) functions.

For more information, see:
https://docs.opensafely.org/releasing-files/
"""
import functools


def redact_le(value, threshold):
    return 0 if value <= threshold else value


redact_le_seven = functools.partial(redact_le, threshold=7)


def round_to_nearest(value, multiple):
    return int(multiple * round(value / multiple, 0))


round_to_nearest_five = functools.partial(round_to_nearest, multiple=5)
