import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Координаты Агротехнического университета имени С. Сейфуллина (г. Астана)
campus_center = [51.187487, 71.408831]  # Центр кампуса, Астана

# Список зданий кампуса с их координатами и названиями (предположительные координаты)
buildings = [
    {"name": "Библиотека", "latitude": 51.1871, "longitude": 71.4093},
    {"name": "Главное здание", "latitude": 51.1871, "longitude": 71.4990},
    {"name": "Аудитория", "latitude": 51.1873, "longitude": 71.4091},
    {"name": "Кафетерий", "latitude": 51.1879, "longitude": 71.4097},
    {"name": "Казахский национальный университет искусств", "latitude": 51.1883, "longitude": 71.4089}
]

# Создаем карту с центром на координатах университета
m = folium.Map(location=campus_center, zoom_start=17, control_scale=True)

# Добавляем кластер маркеров
marker_cluster = MarkerCluster().add_to(m)

# Добавляем маркеры для каждого здания на карту
for building in buildings:
    folium.Marker(
        location=[building["latitude"], building["longitude"]],
        popup=building["name"]
    ).add_to(marker_cluster)

# Отображаем карту в Streamlit
st.title("Карта Агротехнического университета")
st.write("На этой карте отображены здания университета.")
folium_static(m)

# Сохраняем карту и создаем кнопку для скачивания
map_path = "agro_technical_university_map.html"
m.save(map_path)

with open(map_path, "rb") as f:
    st.download_button(
        label="Скачать карту как HTML",
        data=f,
        file_name="agro_technical_university_map.html",
        mime="application/octet-stream"
    )
