import subprocess

print("🧹 Deleting COMETHS first...")
subprocess.run(["python", "Comeths/delete_comeths.py"], check=True)

print("🧹 Deleting SOLOONS after...")
subprocess.run(["python", "Soloons/delete_soloons.py"], check=True)

print("🧹 Deleting POLYANETS last...")
subprocess.run(["python", "Polyanets/delete_polyanets.py"], check=True)

print("Everything deleted successfully!")