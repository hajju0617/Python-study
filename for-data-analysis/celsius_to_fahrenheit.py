temperature_celsius = [25.6, 27.8, 30.5, 22.3, 28.9, 31.2, 24.7]
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
temperature_fahrenheit = list(map(celsius_to_fahrenheit, temperature_celsius))

print('섭씨 온도 데이터 : ', temperature_celsius)
print('화씨 온도 데이터 : ', temperature_fahrenheit)