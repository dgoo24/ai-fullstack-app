from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI(
    title="AI & Data Processing API",
    description="Backend-Dienst für automatisierte Datenanalyse und KI-Modellsimulation",
    version="1.0.0"
)

# Pydantic-Modell für eingehende Datenvalidierung
class DataInput(BaseModel):
    values: list[float]
    threshold: float = 50.0

@app.get("/")
def read_root():
    return {"status": "online", "message": "FastAPI Backend ist bereit für das Portfolio."}

@app.post("/api/v1/analyze")
def analyze_data(payload: DataInput):
    """
    Führt eine statistische Analyse und Anomalieerkennung auf den Eingabedaten durch.
    """
    try:
        data = np.array(payload.values)
        if len(data) == 0:
            raise HTTPException(status_code=400, detail="Der Datensatz darf nicht leer sein.")
        
        # Statistische Kennzahlen berechnen
        mean_val = float(np.mean(data))
        std_val = float(np.std(data))
        anomalies = [val for val in data if val > payload.threshold]

        return {
            "status": "success",
            "metrics": {
                "count": len(data),
                "mean": round(mean_val, 2),
                "std_dev": round(std_val, 2),
                "max": float(np.max(data)),
                "min": float(np.min(data))
            },
            "anomaly_detection": {
                "threshold": payload.threshold,
                "anomalies_detected": len(anomalies),
                "values_above_threshold": anomalies
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))