import requests

cityName = (input('Input city name: '))
cityName = cityName.lower()

forecastDate = input('Input forecast date (format: yyyy mm dd): ')
outputDate = forecastDate
forecastDate = forecastDate.lstrip()
forecastDate = forecastDate.rstrip()
forecastDate = forecastDate.replace(' ', '/')

url = 'https://www.metaweather.com/'

try:
    woeid = requests.get(url + 'api/location/search/?query=' + cityName).json()
    print('Weather in', woeid[0]['title'], 'on ', outputDate)

    print()

    weather = requests.get(url + 'api/location/' + str(woeid[0]['woeid']) + '/' + forecastDate + '/').json()

    forecast = weather[0]

    for el in forecast:
        print(el, ': ', forecast[el])


except:
    print('Sorry, we cannot provide weather information for this region or for this date' )