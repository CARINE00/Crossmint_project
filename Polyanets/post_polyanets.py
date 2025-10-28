import requests
import time

CANDIDATE_ID = "1e9d9841-dee3-4fa6-a823-0060a5129044"
BASE_URL = "https://challenge.crossmint.io/api/polyanets"

MAP_SIZE = 11

def create_polyanet(row, column):
    payload = {
        "row": row,
        "column": column,
        "candidateId": CANDIDATE_ID
    }
    response = requests.post(BASE_URL, json=payload)
    print(f"POST({row}, {column}) -> {response.status_code}")
    time.sleep(1.5)  


def create_cross(): 
    for row in range(MAP_SIZE):
        for column in range(MAP_SIZE):
            if row == column or row + column == MAP_SIZE - 1:
                create_polyanet(row, column)

if __name__ == "__main__":
    create_cross()