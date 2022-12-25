import streamlit as st
from pyluach import dates, parshios
from pymeeus.Sun import Sun, Epoch, Angle
from datetime import datetime, timedelta
import pytz

today_hebrew = dates.HebrewDate.today()

def main():
    print(morid(today_hebrew))
    print(brucha(today_hebrew))
    print(special(today_hebrew))

def morid(today_hebrew):

    #Hatal from misif 1 paisach 15 Nisan to misif Shemini Atzeres 22 Tishrei else HaGeshem
    peasach = dates.HebrewDate(today_hebrew.year, 1, 15)
    shemini_atzeres = dates.HebrewDate(today_hebrew.year, 7, 22)

    if (peasach <= today_hebrew <= dates.HebrewDate(today_hebrew.year, 6, 29)) \
        or (dates.HebrewDate(today_hebrew.year, 7, 1) <= today_hebrew < shemini_atzeres):
        return 'HaTal'
    else:
        return 'HaGeshem'

def brucha(today_hebrew):
    today_greg = today_hebrew.to_greg().to_pydate()
    now_gregorian = datetime.combine(today_greg, datetime.utcnow().astimezone(tz=pytz.timezone('America/New_York')).time())

    #get todays hebrew date, look up next peasach, convert to gregorian, subtract 1 day for erev, look up sunset in NYC in utc time
    pl1 = Epoch(dates.HebrewDate(today_hebrew.year, 1, 15).to_greg().to_pydate() + timedelta(days=-1)).rise_set(Angle(40, 43, 50.1960), Angle(-73, 56, 6.8712), 0)[1].get_full_date()

    #convert utc into datetime, adjust to nyc timezone, add 72 minutes to get erev peasach in gregorian datetime
    peasach_ללה72 = datetime(pl1[0], pl1[1], pl1[2], pl1[3], pl1[4], int(round(pl1[5], 0))) + timedelta(hours=-4, minutes=72)

    #get todays hebrew date, get today gregorian year, look up autumn equinox in utc time
    y, m, d, h, mi, sec = Sun.get_equinox_solstice(today_greg.year, target="autumn").get_full_date()

    #convert utc into datime, adjust to nyc timezone, add 73 days to get vsein_tal switch in gregorian date
    vsein_tal = (datetime(y, m, d, h, mi, int(round(sec, 0))) + timedelta(days=73, hours=-4)).date()

    #look up vsein_tal shkiah
    pl = Epoch(vsein_tal).rise_set(Angle(40, 43, 50.1960), Angle(-73, 56, 6.8712), 0)[1].get_full_date()
    #output vsein_tal shkiah datetime, adjust to nyc timezone, add 72 minutes to get vsein_tal laylah time
    vsein_tal_ללה72 = datetime(pl[0], pl[1], pl[2], pl[3], pl[4], int(round(pl[5], 0))) + timedelta(hours=-5,minutes=72)

    if peasach_ללה72.timestamp() < now_gregorian.timestamp() < vsein_tal_ללה72.timestamp(): #and erev_peasach.timestamp() > dates.timestamp(today_gregorian):
        return 'Brucha'
    else:
        return 'Tal UMatar Lebrucha'

def special(today_hebrew):

    parsha = parshios.getparsha_string(today_hebrew, hebrew=0)
    holiday = today_hebrew.holiday(hebrew=0)
    h_date = today_hebrew.hebrew_date_string()
    return h_date, parsha, holiday

if __name__ == "__main__":
    main()
