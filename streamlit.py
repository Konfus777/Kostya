!pip install folium

import folium
from folium.plugins import MarkerCluster
from google.colab import files

# Координаты Агротехнического университета имени С. Сейфуллина (г. Астана) 
campus_center = [51.187487, 71.408831] # Центр кампуса, Астана
 # Создаем карту с центром на координатах университета
m = folium.Map (location=campus_center, zoom_start=17, control_scale=True)
# Список зданий кампуса с их координатами и названиями (предположительные координаты)
buildings = [
  {"name":"Библиотека","latitude": 51.1871, "longitude": 71.4093},
  {"name": "Главное здание" ,"latitude": 51.1871, "longitude": 71.4990},
  {"name": "Аудитория", "latitude": 51.1873, "longitude": 71.4091},
  {"name":"Кафетерий","latitude": 51.1879, "longitude": 71.4097},
  {"name": "Казахский национальный университет искусста", "latitude": 51.1883,"longitude": 71.4089}
]

marker_cluster = MarkerCluster().add_to(m)

# Corrected the loop variable name from 'building' to 'biulding'
for biulding in buildings:
    folium.Marker(
        location=[biulding["latitude"], biulding["longitude"]], # Accessing data using the correct variable name
        popup=biulding["name"], # Accessing data using the correct variable name
    ).add_to(marker_cluster)

m.save("agro_technical_university_map_with_buildings.html")
files.download("agro_technical_university_map_with_buildings.html")
