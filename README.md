# SunriseSunsetOrgData
This is some code for getting sun data from the API of [sunrise-sunset.org](https://sunrise-sunset.org/).

# Intension
I was working on some house automation for which it was necessary to know when sun will rise and when it will set. Therefore I searched for an online service providing these data. Finally I found [sunrise-sunset.org](https://sunrise-sunset.org/) from where all relevant data can be requested.

# Dependencies
The code is using the packages
- <code>json</code>
- <code>requests</code>
- <code>dateutil</code>
- <code>datetime</code>

In case they aren't installed on your system here are the commands:  
<code>python3 -m pip install requests</code>  
<code>python3 -m pip install python-dateutil</code>  

This code was develloped on Debian 11.6 with the following versions:
- Python 3.9.2
- json 2.0.9
- requests 2.25.1
- dateutil 2.8.2

# Usage
Using the code is very simple. Just create a new instance of SunriseSunsetOrgData by providing the coordinate of the place the data shall be requested for.
By default the data is requested for 'today'. In case you need data for another day just append the desired date.  
You can find some examples in the code.

# Keep in mind
- Since data is requested online from the server of sunrise-sunset.org an internet connection is required.
- All times are returned as UTC. Time zones and daylight saving times aren't considered.
- For debugging the class contains a property 'ErrorCode'. In case no error occured this property contains 'None'. In your code before accessing the sun data you can double check if 'ErrorCode' is really 'None'

# Disclaimer
Before publishing this code I spoke to [sunrise-sunset.org](https://sunrise-sunset.org/) to get the agreement for publishing this code and to refer to their website.
Please keep in mind that I don't assume any liability, not for the code and not for the data given by [sunrise-sunset.org](https://sunrise-sunset.org/).
