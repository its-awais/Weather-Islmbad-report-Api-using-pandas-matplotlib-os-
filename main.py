from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import requests
import pandas as pd
import os
today = datetime.now()
weaks_ago = today - timedelta(days=7)
start_date = weaks_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=33.684422&longitude=73.047882&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
date = response.json()
print(date)


#__________________________ for pandas

daily_data = date['daily']
df = pd.DataFrame({
   'date' : daily_data['time'],
   'temperature_2m_max': daily_data['temperature_2m_max'],
   'temperature_2m_min': daily_data['temperature_2m_min']
})
df['date'] = pd.to_datetime(df['date'])


#----------------------------- for matplotlib for plotting

plt.figure(figsize=(10,6))
plt.plot(df['date'], df['temperature_2m_max'], marker='o', label= 'max temperature')
plt.plot(df['date'], df['temperature_2m_min'],marker='o',label='min temperature')


# adding label and title

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Islmabad temperature for last 7 days')
plt.legend()

# rotate label by x so it shows unique style
plt.xticks(rotation=45)
plt.tight_layout()

# saving graph as image and shows graph
#last command is for showing graph 
plt.savefig('temperature_plot.png')
plt.show()


#------------------------------ now we will save data in csv file

if not os.path.exists('data'):
      os.makedirs('data')

df.to_csv('data/weather_islamabad.csv', index=False)
print("Data saved to 'data/weather_islamabad.csv'")