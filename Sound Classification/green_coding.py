#Codecarbon modules
from codecarbon import EmissionsTracker

#tracker object iniatilised
tracker = EmissionsTracker()

#to track Co2 Emission (Online Mode)
def start_tracker():
    tracker.start()

#To flush logs/checkpoints in emissions.csv based on Developer/User need
def flush_data():
    tracker.flush()

#Stop tracker for Co2 Emission
def pause_tracker():
    emissions: float = tracker.stop()
    print(f"Emissions: {emissions} kg")