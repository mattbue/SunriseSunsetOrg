from ./../SunriseSunsetOrgData import SunriseSunsetOrgData

Berlin_Latitude  = 52.5069386
Berlin_Longitude = 13.2599274

print('Requesting todays sun data for Berlin...')

ssod = SunriseSunsetOrgData(Berlin_Latitude, Berlin_Longitude)

print('Error-Code : ' + str(ssod.ErrorCode))
print('----------------------------------------------------')
print('Date                        : ' + str(ssod.Date))
print('Sunrise                     : ' + str(ssod.Sunrise))
print('Sunset                      : ' + str(ssod.Sunset))
print('Solar Noon                  : ' + str(ssod.SolarNoon))
print('Day Length                  : ' + str(ssod.DayLength))
print('Civil Twilight Begin        : ' + str(ssod.CivilTwilightBegin))
print('Civil Twilight End          : ' + str(ssod.CivilTwilightEnd))
print('Nautical Twilight Begin     : ' + str(ssod.NauticalTwilightBegin))
print('Nautical Twilight End       : ' + str(ssod.NauticalTwilightEnd))
print('Astronomical Twilight Begin : ' + str(ssod.AstronomicalTwilightBegin))
print('Astronomical Twilight End   : ' + str(ssod.AstronomicalTwilightEnd))
