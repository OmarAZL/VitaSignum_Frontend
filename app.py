import streamlit as st
import requests as req
import json

st.title("VitaSignum")

BACKEND_URL = "http://localhost:52211/api/get_json"
REFRESH_INTERVAL_SECONDS = 1

placeholder = st.empty()

while True:
    try:
        response = req.get(BACKEND_URL)
        if response.status_code == 200:
            data = response.json()
            with placeholder.container():
                st.json(data)
                load = json.loads(json.dumps(data))
                temp1 = load["temp1"]
                temp2 = load["temp2_obj"]
                hours = load["timestamp_ms"] / 3600000
                st.write(f"Temperatura 1: :blue[{temp1}]")
                st.write(f"Temperatura 2: :blue[{temp2}]")
                st.write(f"Tiempo encendido: :blue[{round(hours, 3)}] horas")
        else:
            st.error(f"Error al obtener datos: Código {response.status_code}")
            st.text(f"Reintentando en {REFRESH_INTERVAL_SECONDS} segundos")
    except req.exceptions.RequestException as e:
        with placeholder.container():
            st.error(f"Error de conexión: {e}")
            st.text(f"Reintentando en {REFRESH_INTERVAL_SECONDS} segundos")


