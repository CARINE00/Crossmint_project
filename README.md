# Crossmint Megaverse Challenge
This project contains scripts developed for the Crossmint Challenge, organized by entity:

 -  Polyanets 🪐

 -  Soloons 🌕 

 - Comeths ☄️ 

``` Each module includes scripts for creating (post_) and removing (delete_) entities. ```

## Project Structure ##

```CROSSMINT_PROJECT_/
│
├── Polyanets/
│ ├── post_polyanets.py
│ └── delete_polyanets.py
│
├── Soloons/
│ ├── post_soloons.py
│ └── delete_soloons.py
│
├── Comeths/
│ ├── post_comeths.py
│ └── delete_comeths.py
│
├── run_create_all.py # Executes all creation scripts in the correct order
├── run_delete_all.py # Executes all deletion scripts in reverse order
├── requirements.txt
└── README.md ```

## Execution 🚀 ##

Create all entities (in the correct order)
``` python run_create_all.py ```

Delete all entities (reverse order)
``` python run_create_all.py ```

## Technologies Used
 - Python 3.11+
 - Requests (for REST API calls)
 - Time (for API rate control)