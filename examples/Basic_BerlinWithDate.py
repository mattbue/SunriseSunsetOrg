# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from SunriseSunsetOrg import SunriseSunsetOrg

Berlin_Latitude  = 52.5069386
Berlin_Longitude = 13.2599274
Date             = datetime.strptime('2023-06-01', '%Y-%m-%d')

print('Requesting sun data for Berlin for first of June 2023...')

sso = SunriseSunsetOrg(Berlin_Latitude, Berlin_Longitude, Date)

print('Error-Code : ' + str(sso.ErrorCode))
print('----------------------------------------------------')
print('Date                        : ' + str(sso.Date))
print('Sunrise                     : ' + str(sso.Sunrise))
print('Sunset                      : ' + str(sso.Sunset))
print('Solar Noon                  : ' + str(sso.SolarNoon))
print('Day Length                  : ' + str(sso.DayLength))
print('Civil Twilight Begin        : ' + str(sso.CivilTwilightBegin))
print('Civil Twilight End          : ' + str(sso.CivilTwilightEnd))
print('Nautical Twilight Begin     : ' + str(sso.NauticalTwilightBegin))
print('Nautical Twilight End       : ' + str(sso.NauticalTwilightEnd))
print('Astronomical Twilight Begin : ' + str(sso.AstronomicalTwilightBegin))
print('Astronomical Twilight End   : ' + str(sso.AstronomicalTwilightEnd))
