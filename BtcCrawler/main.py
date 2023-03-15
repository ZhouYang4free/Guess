import requests

url = 'https://www.binance.com/en/markets'
response = requests.get(url)

html = response.text
print(html)
