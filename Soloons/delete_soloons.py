import requests
import time

CANDIDATE_ID = "1e9d9841-dee3-4fa6-a823-0060a5129044"
BASE_URL = "https://challenge.crossmint.io/api/soloons"

# Mesmas coordenadas usadas na criação (a cor não é necessária para deletar)
SOLOONS = [
    (2, 3), (2, 7),
    (3, 4), (3, 6),
    (4, 5),
    (6, 5),
    (7, 4), (7, 6),
    (8, 3), (8, 7),
]

def delete_soloon(row: int, column: int):
    payload = {
        "row": row,
        "column": column,
        "candidateId": CANDIDATE_ID
    }
    response = requests.delete(BASE_URL, json=payload)
    print(f"DELETE ({row}, {column}) -> {response.status_code}")
    time.sleep(1.5)

def delete_soloons():
    for row, column in SOLOONS:
        delete_soloon(row, column)

if __name__ == "__main__":
    delete_soloons()
