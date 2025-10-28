import time
import requests

CANDIDATE_ID = "1e9d9841-dee3-4fa6-a823-0060a5129044"
BASE_URL = "https://challenge.crossmint.io/api/polyanets"
MAP_SIZE = 11  

def delete_polyanet(row, column):
    payload = {
        "row": row, 
        "column": column, 
        "candidateId": CANDIDATE_ID
    }
    response = requests.delete(BASE_URL, json=payload)
    print(f"DELETE ({row},{column}) -> {response.status_code}")
    time.sleep(0.5)
    return response

def delete_cross():
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            if r == c or r + c == MAP_SIZE - 1:
                delete_polyanet(r, c)

if __name__ == "__main__":
    delete_cross()