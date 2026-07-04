import subprocess
import sys

files = [
    "qrng.py",
    "histogram.py",
    "statistics.py",
    "comparison.py"
]

for file in files:
    print(f"\nRunning {file}...\n")
    subprocess.run([sys.executable, file], check=True)
