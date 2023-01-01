# Tefillas HaTal V'Geshem
    #### Video Demo:  <URL HERE>

## Overview
    
#### A Python program for determining the correct blessings for the current season, time and date. It uses the pyluach and PyMeeus libraries to manipulate and convert Gregorian & Hebrew dates, look up weekly parshiyos and holidays, and calculate sunset times. The program has been written and tested in the Eastern Time zone, so it is important to note that the outputs will not be accurate in other time zones. The program is available online at https://cs50-372911.ue.r.appspot.com/

## Dependencies
#### To use this program, you will need to have the following libraries installed:

>pyluach
>PyMeeus
>pytz

#### You can install these libraries using pip. For example:
"""
pip install pyluach
pip install PyMeeus
pip install pytz
"""

## Usage
#### The main entry point for this program is the parsha() function, which returns Hebrew date as a string and any parsha occasions (e.g. holidays, Shabbos). This function takes an optional datetime object as an argument, which defaults to the current time in the Eastern Time zone.

#### For example:
'''
from datetime import datetime

print(parsha())
print(parsha(datetime(2023, 1, 1)))
'''

#### The morid() function returns the correct blessing to say for morid haTal or morid haGeshem based on the current date. It also takes an optional datetime object as an argument.

For example:
'''
print(morid())
print(morid(datetime(2023, 1, 1)))
'''

#### The tal_matar() function returns the correct blessing to say for Tal u'Matar based on the current date. It also takes an optional datetime object as an argument.
#### For example:

'''
print(tal_matar())
print(tal_matar(datetime(2023, 1, 1)))
'''

## Customization
#### You can customize the behavior of the program by modifying the 'Dtx' class. This class contains several utility functions for manipulating dates and times based on the Eastern Time zone, including:

- he_date(self, gr_d=None): Returns the current date in the Hebrew calendar, adjusted for sunset.
- sunset(self, gr_d=None): Returns the datetime of sunset on the given date.
- pesach(self, gr_d=None): Returns the datetime of Pesach for the current year.
- pesach_ch(self, gr_d=None): Returns the dateime of chol hamo'ed Pesach for the current year.
- shmini(self, gr_d=None): Returns the date of Shmini Atzeres for the current year.
- tekufas_Tishrei(self, gr_d=None): Returns the sunset datetime of tekufas Tishrei.

## References

#### https://pypi.org/project/pyluach/
#### https://pypi.org/project/PyMeeus/
#### https://halachipedia.com/index.php?title=Barech_Aleinu
#### https://en.wikipedia.org/wiki/Tishrei
#### https://outorah.org/p/22451/
#### https://www.lookstein.org/professional-dev/misc/veten-tal-u-matar/
