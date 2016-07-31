__author__ = 'kevinorr'

import itertools

"""
This is my solution to Googles Challenge Q1 about the magician and his cards with dates - OMG I can't remember it now
but that's what happens when you drink too much of Spain's San Miguel beer - hicup.....

There's some constraints - again can't remember - but we basically want a date returned in format: month/day/year
or the string 'Ambiguous' if we can't determine a date.

For example,
2, 30, 3 could be 2/3/30 or 3/2/30 so it's ambiguous whereas 19, 19, 03 could only ne 3/19/19

Warning - no checks for inputs blahdy blah blah - not required for the challenge

Anyway, this passed the verify tests - not pretty though - hey I'm learning...

"""

def answer(x, y, z):

    # a representation of a typical year - one of the constraints is no leap year
    monthDays = {
        '1': range(1, 32),
        '2': range(1, 29),
        '3': range(1, 32),
        '4': range(1, 31),
        '5': range(1, 32),
        '6': range(1, 31),
        '7': range(1, 32),
        '8': range(1, 32),
        '9': range(1, 31),
        '10': range(1, 32),
        '11': range(1, 31),
        '12': range(1, 32)
    }

    candidateSet = set([(month, day, year)
                                    for (month, day, year) in itertools.permutations([x, y, z])
                                    if str(month) in monthDays and day in monthDays[str(month)]])

    candidateLen = len(candidateSet)

    if candidateLen > 1:
        return 'Ambiguous'
    elif candidateLen == 1:
        (MM, DD, YY) = list(candidateSet)[0]
        return '{}/{}/{}'.format(format(MM,'02d'), format(DD, '02d'), format(YY, '02d'))



if __name__ == "__main__":

    assert '03/19/19' == answer(19, 19, 03)
    assert 'Ambiguous' == answer(02, 30, 3)
    assert '02/14/29' == answer(29, 14, 2)
    assert '01/01/99' == answer(1, 1, 99)


