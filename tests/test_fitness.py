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
