import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
import pytest
from aceest_fitness.ACEest_Fitness import FitnessTrackerApp

def test_add_valid_workout():
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    entry = app.add_workout_logic("Push-ups", 30)
    assert entry["workout"] == "Push-ups"
    assert entry["duration"] == 30
    assert len(app.workouts) == 1

def test_add_missing_fields():
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    with pytest.raises(ValueError):
        app.add_workout_logic("", 20)

def test_add_invalid_duration():
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    with pytest.raises(ValueError):
        app.add_workout_logic("Sit-ups", "abc")
