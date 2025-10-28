import requests
import time

CANDIDATE_ID = "1e9d9841-dee3-4fa6-a823-0060a5129044"
BASE_URL = "https://challenge.crossmint.io/api/comeths"

# Preencha com as coordenadas e direções do seu objetivo
# direction deve ser: "up", "down", "left", "right"
COMETHS = [
    
    (2, 5),
    (5, 2),
]

def create_cometh(row: int, column: int, direction: str):
    payload = {
        "row": row,
        "column": column,
        "direction": direction,
        "candidateId": CANDIDATE_ID
    }
    response = requests.post(BASE_URL, json=payload)
    print(f"DELETE({row}, {column}) -> {response.status_code}")
    time.sleep(1.2)  

def create_comeths():
    for row, column in COMETHS:
        create_cometh(row, column)

if __name__ == "__main__":
    create_comeths()
