# Entkoppelte AI Full-Stack Webanwendung (FastAPI & Streamlit)

Eine modulare, produktionsnahe Full-Stack-Architektur zur automatisierten statistischen Datenanalyse und Anomalieerkennung. Das Projekt demonstriert die strikte Trennung von Backend-Logik (REST-API) und Frontend-Benutzeroberfläche (Analytics Dashboard).

---

## 🏗️ Architektur & Tech-Stack

Das System ist in zwei unabhängige, lose gekoppelte Komponenten unterteilt:

- **Backend:** `FastAPI` (Python) für performantes Routing, strenge Datenvalidierung via `Pydantic` und mathematische Berechnungen mit `NumPy` und `Pandas`. Inklusive automatisierter Swagger-Dokumentation.
- **Frontend:** `Streamlit` als interaktives Analytics-Dashboard, das asynchron über HTTP-Requests (`requests`) mit dem Backend kommuniziert.
- **Entwicklungsumgebung:** Python virtual environment (`venv`), Git für die Versionskontrolle.

---

## 📂 Projektstruktur

```text
ai-fullstack-app/
│
├── backend/
│   └── main.py          # FastAPI-Anwendung, Endpunkte & Datenvalidierung
├── frontend/
│   └── app.py           # Streamlit-Benutzeroberfläche & API-Client
├── data/                # Ablage für Datensätze (optional)
├── .gitignore           # Ignorierte Dateien (venv, Cache, Datenbanken)
├── requirements.txt     # Projektabhängigkeiten
└── README.md            # Projektdokumentation
```

# ⚙️ Installation & Lokale Ausführung

## 1. Repository klonen und virtuelle Umgebung aktivieren

```powershell
python -m venv venv
.\venv\Scripts\activate
```

## 2. Abhängigkeiten installieren
```powershell
pip install -r requirements.txt
```

## 3. Backend starten (FastAPI)
Öffnen Sie ein Terminal und starten Sie den Uvicorn-Server mit Auto-Reload:
```powershell
uvicorn backend.main:app --reload
```

## 4. Frontend starten (Streamlit)
Öffnen Sie ein zweites Terminal, aktivieren Sie die Umgebung und starten Sie das Dashboard:
```powershell
.\venv\Scripts\activate
streamlit run frontend/app.py
``` 

# 🔌  API-Endpunkte

GET /: Statusprüfung des Backends.

POST /api/v1/analyze: Nimmt numerische Rohdaten und einen Schwellenwert entgegen, berechnet statistische Kernmetriken (Mittelwert, Standardabweichung, Min/Max) und identifiziert Anomalien.

JSON
{
  "values": [12.5, 45.0, 67.8, 22.1, 89.4],
  "threshold": 50.0
}