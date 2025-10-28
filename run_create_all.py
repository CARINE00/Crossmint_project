import subprocess

print("▶️ Creating POLYANETS first...")
subprocess.run(["python", "Polyanets/post_polyanets.py"], check=True)

print("▶️ Creating SOLOONS after...")
subprocess.run(["python", "Soloons/post_soloons.py"], check=True)

print("▶️ Creating COMETHS last...")
subprocess.run(["python", "Comeths/post_comeths.py"], check=True)

print("Completed successfully!")
