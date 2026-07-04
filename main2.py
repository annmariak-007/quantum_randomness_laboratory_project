import runpy

print("=" * 50)
print("Quantum Randomness Laboratory")
print("=" * 50)

print("\n1. Generating Quantum Random Numbers...\n")
runpy.run_path("qrng.py", run_name="__main__")

print("\n2. Performing Statistical Analysis...\n")
runpy.run_path("statistics.py", run_name="__main__")

print("\n3. Displaying Histogram...\n")
runpy.run_path("histogram.py", run_name="__main__")

print("\n4. Comparing Classical and Quantum Randomness...\n")
runpy.run_path("comparison.py", run_name="__main__")

print("\n✅ Project completed successfully!")
