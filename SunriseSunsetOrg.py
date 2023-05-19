import json
import requests
from dateutil import parser
from dateutil import tz
from datetime import timedelta
from datetime import datetime

class SunriseSunsetOrg:

  FORMAT_ISO8601 = 0
  FORMAT_DEFAULT = 1
  
  ERROR_CODE_REQUEST_FAILED             = 1000
  ERROR_CODE_RESPONSE_IS_NONE           = 1001
  ERROR_CODE_RESPONSE_STATUS_CODE_WRONG = 1002
  
  ERROR_CODE_LOADING_JSON_STRING_FAILED = 1100
  ERROR_CODE_JSON_DATA_IS_NONE          = 1101
  ERROR_CODE_JSON_DATA_HAS_NO_STATUS    = 1102
  ERROR_CODE_JSON_DATA_STATUS_IS_NOT_OK = 1103
  ERROR_CODE_JSON_DATA_HAS_NO_RESULTS   = 1104
  
  ERROR_CODE_JSON_DATA_HAS_NO_SUNRISE  = 1200
  ERROR_CODE_PARSING_SUNRISE_FAILED    = 1201
  ERROR_CODE_SUNRISE_IS_NONE           = 1202
  ERROR_CODE_SUNRISE_DATATYPE_IS_WRONG = 1203
  
  ERROR_CODE_JSON_DATA_HAS_NO_SUNSET  = 1300
  ERROR_CODE_PARSING_SUNSET_FAILED    = 1301
  ERROR_CODE_SUNSET_IS_NONE           = 1302
  ERROR_CODE_SUNSET_DATATYPE_IS_WRONG = 1303
  
  ERROR_CODE_JSON_DATA_HAS_NO_SOLAR_NOON  = 1400
  ERROR_CODE_PARSING_SOLAR_NOON_FAILED    = 1401
  ERROR_CODE_SOLAR_NOON_IS_NONE           = 1402
  ERROR_CODE_SOLAR_NOON_DATATYPE_IS_WRONG = 1403
  
  ERROR_CODE_JSON_DATA_HAS_NO_DAY_LENGTH  = 1500
  ERROR_CODE_PARSING_DAY_LENGTH_FAILED    = 1501
  ERROR_CODE_DAY_LENGTH_IS_NONE           = 1502
  ERROR_CODE_DAY_LENGTH_DATATYPE_IS_WRONG = 1503
  
  ERROR_CODE_JSON_DATA_HAS_NO_CIVIL_TWILIGHT_BEGIN  = 1600
  ERROR_CODE_PARSING_CIVIL_TWILIGHT_BEGIN_FAILED    = 1601
  ERROR_CODE_CIVIL_TWILIGHT_BEGIN_IS_NONE           = 1602
  ERROR_CODE_CIVIL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG = 1603
  
  ERROR_CODE_JSON_DATA_HAS_NO_CIVIL_TWILIGHT_END  = 1700
  ERROR_CODE_PARSING_CIVIL_TWILIGHT_END_FAILED    = 1701
  ERROR_CODE_CIVIL_TWILIGHT_END_IS_NONE           = 1702
  ERROR_CODE_CIVIL_TWILIGHT_END_DATATYPE_IS_WRONG = 1703
  
  ERROR_CODE_JSON_DATA_HAS_NO_NAUTICAL_TWILIGHT_BEGIN  = 1800
  ERROR_CODE_PARSING_NAUTICAL_TWILIGHT_BEGIN_FAILED    = 1801
  ERROR_CODE_NAUTICAL_TWILIGHT_BEGIN_IS_NONE           = 1802
  ERROR_CODE_NAUTICAL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG = 1803
  
  ERROR_CODE_JSON_DATA_HAS_NO_NAUTICAL_TWILIGHT_END  = 1900
  ERROR_CODE_PARSING_NAUTICAL_TWILIGHT_END_FAILED    = 1901
  ERROR_CODE_NAUTICAL_TWILIGHT_END_IS_NONE           = 1902
  ERROR_CODE_NAUTICAL_TWILIGHT_END_DATATYPE_IS_WRONG = 1903
  
  ERROR_CODE_JSON_DATA_HAS_NO_ASTRONOMICAL_TWILIGHT_BEGIN  = 2000
  ERROR_CODE_PARSING_ASTRONOMICAL_TWILIGHT_BEGIN_FAILED    = 2001
  ERROR_CODE_ASTRONOMICAL_TWILIGHT_BEGIN_IS_NONE           = 2002
  ERROR_CODE_ASTRONOMICAL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG = 2003
  
  ERROR_CODE_JSON_DATA_HAS_NO_ASTRONOMICAL_TWILIGHT_END  = 2100
  ERROR_CODE_PARSING_ASTRONOMICAL_TWILIGHT_END_FAILED    = 2101
  ERROR_CODE_ASTRONOMICAL_TWILIGHT_END_IS_NONE           = 2102
  ERROR_CODE_ASTRONOMICAL_TWILIGHT_END_DATATYPE_IS_WRONG = 2103
  
  Url             = None
  ResponseContent = None
  JsonData        = None
  
  ErrorCode = None
  
  Date                      = None
  Sunrise                   = None
  Sunset                    = None
  SolarNoon                 = None
  DayLength                 = None
  CivilTwilightBegin        = None
  CivilTwilightEnd          = None
  NauticalTwilightBegin     = None
  NauticalTwilightEnd       = None
  AstronomicalTwilightBegin = None
  AstronomicalTwilightEnd   = None
    
  def __init__(self, Latitude, Longitude, Date = None):
       
    # Generate URL
    url = 'https://api.sunrise-sunset.org/json?'
    url += 'lat=' + str(Latitude)
    url += '&lng=' + str(Longitude)
    
    if Date != None:
      url += '&date=' + Date.strftime('%Y-%m-%d')
    
    url += '&formatted=' + str(self.FORMAT_ISO8601)
      
    self.Url = url
    
    # Request
    try:
      response = requests.get(url)
    except:
      # Request failed
      self.ErrorCode = self.ERROR_CODE_REQUEST_FAILED
      return
      
      
    
    json_data                = None
    content_status_ok        = False
    content_contains_results = None
    
    # Check if response is ok
    if response == None:
      self.ErrorCode = self.ERROR_CODE_RESPONSE_IS_NONE
      return
      
      
    # Check if response status code is 200
    if response.status_code != 200:
      self.ErrorCode = self.ERROR_CODE_RESPONSE_STATUS_CODE_WRONG
      return
      
      
    # Read response content to json data
    self.ResponseContent = response.content

    try:
      json_data = json.loads(response.content)
      self.JsonData = json_data
    except:
      self.ErrorCode = self.ERROR_CODE_LOADING_JSON_STRING_FAILED
      return
    
    
    # Check if json data is none
    if json_data == None:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_IS_NONE
      return
      
      
    # Check if json data contains status
    if not 'status' in json_data:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_STATUS
      return
        
    
    # Check if status in json data
    if json_data['status'] != 'OK':
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_STATUS_IS_NOT_OK
      return
    
    # Check if json data contains results
    if not 'results' in json_data:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_RESULTS
      return
    
    
    
    
    # Check if json data contains sunrise
    if not 'sunrise' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_SUNRISE
      return
    
    # Read sunrise data and parse it to datetime
    try:
      sunrise = parser.parse(json_data['results']['sunrise'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_SUNRISE_FAILED
      return
    
    # Check if sunrise isn't None and is from type datetime
    if sunrise == None:
      self.ErrorCode = self.ERROR_CODE_SUNRISE_IS_NONE
      return
    
    if isinstance(sunrise, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_SUNRISE_DATATYPE_IS_WRONG
      return
    
    # Mark sunrise datetime as utc
    self.Sunrise = sunrise.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains sunset
    if not 'sunset' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_SUNSET
      return
    
    # Read sunset data and parse it to datetime
    try:
      sunset = parser.parse(json_data['results']['sunset'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_SUNSET_FAILED
      return
    
    # Check if sunset is None
    if sunset == None:
      self.ErrorCode = self.ERROR_CODE_SUNSET_IS_NONE
      return
    
    # Check if sunset is from type datetime
    if isinstance(sunset, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_SUNSET_DATATYPE_IS_WRONG
      return
    
    # Mark sunset datetime as utc
    self.Sunset = sunset.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains solar noon
    if not 'solar_noon' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_SOLAR_NOON
      return
    
    # Read solar noon data and parse it to datetime
    try:
      solar_noon = parser.parse(json_data['results']['solar_noon'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_SOLAR_NOON_FAILED
      return
    
    # Check if solar noon is None
    if solar_noon == None:
      self.ErrorCode = self.ERROR_CODE_SOLAR_NOON_IS_NONE
      return
    
    # Check if solar noon is from type datetime
    if isinstance(solar_noon, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_SOLAR_NOON_DATATYPE_IS_WRONG
      return
    
    # Mark solar noon datetime as utc
    self.SolarNoon = solar_noon.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains day length
    if not 'day_length' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_DAY_LENGTH
      return
    
    # Read day length data and parse it to timedelta
    try:
      day_length = timedelta(seconds=int(json_data['results']['day_length']))
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_DAY_LENGTH_FAILED
      return
    
    # Check if day length is None
    if day_length == None:
      self.ErrorCode = self.ERROR_CODE_DAY_LENGTH_IS_NONE
      return
    
    # Check if day_length is from type timedelta
    if isinstance(day_length, timedelta) == False:
      self.ErrorCode = self.ERROR_CODE_DAY_LENGTH_DATATYPE_IS_WRONG
      return
    
    self.DayLength = day_length
    
    
    
    
    # Check if json data contains civil twilight begin
    if not 'civil_twilight_begin' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_CIVIL_TWILIGHT_BEGIN
      return
    
    # Read civil twilight begin data and parse it to datetime
    try:
      civil_twilight_begin = parser.parse(json_data['results']['civil_twilight_begin'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_CIVIL_TWILIGHT_BEGIN_FAILED
      return
    
    # Check if civil twilight begin is None
    if civil_twilight_begin == None:
      self.ErrorCode = self.ERROR_CODE_CIVIL_TWILIGHT_BEGIN_IS_NONE
      return
    
    # Check if civil twilight begin is from type datetime
    if isinstance(civil_twilight_begin, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_CIVIL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG
      return
    
    # Mark civil twilight begin datetime as utc
    self.CivilTwilightBegin = civil_twilight_begin.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains civil twilight end
    if not 'civil_twilight_end' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_CIVIL_TWILIGHT_END
      return
    
    # Read civil twilight end data and parse it to datetime
    try:
      civil_twilight_end = parser.parse(json_data['results']['civil_twilight_end'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_CIVIL_TWILIGHT_END_FAILED
      return
    
    # Check if civil twilight end is None
    if civil_twilight_end == None:
      self.ErrorCode = self.ERROR_CODE_CIVIL_TWILIGHT_END_IS_NONE
      return
    
    # Check if civil twilight end is from type datetime
    if isinstance(civil_twilight_end, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_CIVIL_TWILIGHT_END_DATATYPE_IS_WRONG
      return
    
    # Mark civil twilight end datetime as utc
    self.CivilTwilightEnd = civil_twilight_end.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains nautical twilight begin
    if not 'nautical_twilight_begin' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_NAUTICAL_TWILIGHT_BEGIN
      return
    
    # Read nautical twilight begin data and parse it to datetime
    try:
      nautical_twilight_begin = parser.parse(json_data['results']['nautical_twilight_begin'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_NAUTICAL_TWILIGHT_BEGIN_FAILED
      return
    
    # Check if nautical twilight begin is None
    if nautical_twilight_begin == None:
      self.ErrorCode = self.ERROR_CODE_NAUTICAL_TWILIGHT_BEGIN_IS_NONE
      return
    
    # Check if nautical twilight begin is from type datetime
    if isinstance(nautical_twilight_begin, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_NAUTICAL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG
      return
    
    # Mark nautical twilight begin datetime as utc
    self.NauticalTwilightBegin = nautical_twilight_begin.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains nautical twilight end
    if not 'nautical_twilight_end' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_NAUTICAL_TWILIGHT_END
      return
    
    # Read nautical twilight end data and parse it to datetime
    try:
      nautical_twilight_end = parser.parse(json_data['results']['nautical_twilight_end'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_NAUTICAL_TWILIGHT_END_FAILED
      return
    
    # Check if nautical twilight end is None
    if nautical_twilight_end == None:
      self.ErrorCode = self.ERROR_CODE_NAUTICAL_TWILIGHT_END_IS_NONE
      return
    
    # Check if nautical twilight end is from type datetime
    if isinstance(nautical_twilight_end, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_NAUTICAL_TWILIGHT_END_DATATYPE_IS_WRONG
      return
    
    # Mark nautical twilight end datetime as utc
    self.NauticalTwilightEnd = nautical_twilight_end.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains astronomical twilight begin
    if not 'astronomical_twilight_begin' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_ASTRONOMICAL_TWILIGHT_BEGIN
      return
    
    # Read astronomical twilight begin data and parse it to datetime
    try:
      astronomical_twilight_begin = parser.parse(json_data['results']['astronomical_twilight_begin'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_ASTRONOMICAL_TWILIGHT_BEGIN_FAILED
      return
    
    # Check if astronomical twilight begin is None
    if astronomical_twilight_begin == None:
      self.ErrorCode = self.ERROR_CODE_ASTRONOMICAL_TWILIGHT_BEGIN_IS_NONE
      return
    
    # Check if astronomical twilight begin is from type datetime
    if isinstance(astronomical_twilight_begin, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_ASTRONOMICAL_TWILIGHT_BEGIN_DATATYPE_IS_WRONG
      return
    
    # Mark astronomical twilight begin datetime as utc
    self.AstronomicalTwilightBegin = astronomical_twilight_begin.replace(tzinfo=tz.tzutc())
    
    
    
    
    # Check if json data contains astronomical twilight end
    if not 'astronomical_twilight_end' in json_data['results']:
      self.ErrorCode = self.ERROR_CODE_JSON_DATA_HAS_NO_ASTRONOMICAL_TWILIGHT_END
      return
    
    # Read astronomical twilight end data and parse it to datetime
    try:
      astronomical_twilight_end = parser.parse(json_data['results']['astronomical_twilight_end'])
    except:
      self.ErrorCode = self.ERROR_CODE_PARSING_ASTRONOMICAL_TWILIGHT_END_FAILED
      return
    
    # Check if astronomical twilight end is None
    if astronomical_twilight_end == None:
      self.ErrorCode = self.ERROR_CODE_ASTRONOMICAL_TWILIGHT_END_IS_NONE
      return
    
    # Check if astronomical twilight end is from type datetime
    if isinstance(astronomical_twilight_end, datetime) == False:
      self.ErrorCode = self.ERROR_CODE_ASTRONOMICAL_TWILIGHT_END_DATATYPE_IS_WRONG
      return
    
    # Mark astronomical twilight end datetime as utc
    self.AstronomicalTwilightEnd = astronomical_twilight_end.replace(tzinfo=tz.tzutc())
    
    
    
    self.Date = self.Sunrise.date()
