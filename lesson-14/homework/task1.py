from bs4 import BeautifulSoup
with open("weather.html", 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

weather_data = []
rows = soup.find('tbody').find_all('tr')

for row in rows:
    day = row.find_all('td')[0].text
    temperature = int(row.find_all('td')[1].text[:2])
    condition = row.find_all('td')[2].text
    weather_data.append({'day': day, 'temperature': temperature, 'condition': condition})


print("Weather Data:")
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}")


max_temp = max(entry['temperature'] for entry in weather_data)
hottest_days = [entry['day'] for entry in weather_data if entry['temperature'] == max_temp]
print(f"Day(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")


sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == 'Sunny']
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")


avg_temp = sum(entry['temperature'] for entry in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {avg_temp:.2f}°C")