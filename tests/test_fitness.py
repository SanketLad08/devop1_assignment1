import pytest
import tkinter as tk
from aceest_fitness.ACEest_Fitness import FitnessTrackerApp


@pytest.fixture
def app():
    """Fixture to create and clean up a Tkinter app instance."""
    root = tk.Tk()
    root.withdraw()   # prevent GUI window from showing
    app = FitnessTrackerApp(root)
    yield app
    root.destroy()    # clean up after test


def test_add_valid_workout(app):
    app.workout_entry.insert(0, "Running")
    app.duration_entry.insert(0, "30")
    app.add_workout()
    assert len(app.workouts) == 1
    assert app.workouts[0]["workout"] == "Running"
    assert app.workouts[0]["duration"] == "30"


def test_add_missing_fields(app):
    app.workout_entry.delete(0, tk.END)
    app.duration_entry.delete(0, tk.END)
    app.add_workout()
    assert len(app.workouts) == 0


def test_add_invalid_duration(app):
    app.workout_entry.insert(0, "Cycling")
    app.duration_entry.insert(0, "abc")  # invalid input
    app.add_workout()
    assert len(app.workouts) == 0
