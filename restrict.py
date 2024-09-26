from requests import get

response = get(f'http://ip-api.com/json/').json()

#print(response)

country = response['country']
#country = 'Canada'

if country == 'United States':
    print(f'Welcome In! We love {country}')
else:
    print(f'Redirect to another page {country}')