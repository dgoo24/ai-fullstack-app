import streamlit as st
import requests

st.set_page_config(
    page_title="AI Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 KI-gestütztes Analyse-Dashboard")
st.markdown("Dieses Dashboard kommuniziert mit einem entkoppelten **FastAPI-Backend** zur statistischen Auswertung und Anomalieerkennung.")

st.sidebar.header("Eingabeparameter")
input_data = st.sidebar.text_input("Geben Sie Zahlen ein (kommagetrennt):", "12.5, 45.0, 67.8, 22.1, 89.4, 33.2")
threshold = st.sidebar.slider("Schwellenwert für Anomalien:", min_value=10.0, max_value=100.0, value=50.0)

if st.sidebar.button("Daten analysieren"):
    try:
        # Konvertierung der Eingabe in eine Liste von Floats
        values = [float(x.strip()) for x in input_data.split(",") if x.strip()]
        
        payload = {
            "values": values,
            "threshold": threshold
        }
        
        # Anfrage an das FastAPI-Backend senden
        response = requests.post("http://127.0.0.1:8000/api/v1/analyze", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            metrics = result["metrics"]
            anomalies = result["anomaly_detection"]
            
            st.success("Analyse erfolgreich durchgeführt!")
            
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Anzahl Datenpunkte", metrics["count"])
            col2.metric("Mittelwert (Mean)", metrics["mean"])
            col3.metric("Standardabweichung", metrics["std_dev"])
            col4.metric("Maximum", metrics["max"])
            
            st.subheader("Ergebnisse der Anomalieerkennung")
            st.write(f"Definierter Schwellenwert: **{anomalies['threshold']}**")
            st.write(f"Anzahlerkannte Anomalien: **{anomalies['anomalies_detected']}**")
            
            if anomalies["values_above_threshold"]:
                st.warning(f"Gefundene Werte über dem Schwellenwert: {anomalies['values_above_threshold']}")
            else:
                st.info("Keine Anomalien im aktuellen Datensatz gefunden.")
                
        else:
            st.error(f"Fehler vom Server: {response.json().get('detail', 'Unbekannter Fehler')}")
            
    except ValueError:
        st.error("Bitte geben Sie nur gültige, durch Kommas getrennte Zahlen ein.")
    except requests.exceptions.ConnectionError:
        st.error("Verbindungsfehler: Das FastAPI-Backend ist nicht erreichbar. Stellen Sie sicher, dass Uvicorn läuft.")