import requests
import time

CANDIDATE_ID = "1e9d9841-dee3-4fa6-a823-0060a5129044"
BASE_URL = "https://challenge.crossmint.io/api/soloons"

# Preencha com as coordenadas e cores do seu objetivo
# Exemplo (ajuste conforme seu goal):
SOLOONS = [
    (2, 3, "blue"),
    (2, 7, "red"),
    (3, 4, "purple"),
    (3, 6, "white"),
    (4, 5, "blue"),
    (6, 5, "red"),
    (7, 4, "purple"),
    (7, 6, "white"),
    (8, 3, "blue"),
    (8, 7, "red"),
]

def create_soloon(row: int, column: int, color: str):
    payload = {
        "row": row,
        "column": column,
        "color": color,
        "candidateId": CANDIDATE_ID
    }
    response = requests.post(BASE_URL, json=payload)
    print(f"POST ({row}, {column}) [{color}] -> {response.status_code}")
    time.sleep(1.5) 

def create_soloons():
    for row, column, color in SOLOONS:
        create_soloon(row, column, color)

if __name__ == "__main__":
    create_soloons()
