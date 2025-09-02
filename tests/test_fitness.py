import pytest
from unittest import mock

# Patch all tkinter imports so they don’t create real GUI
with mock.patch.dict("sys.modules", {
    "tkinter": mock.MagicMock(),
    "tkinter.messagebox": mock.MagicMock(),
}):
    from aceest_fitness.ACEest_Fitness import FitnessTrackerApp


@pytest.fixture
def app():
    """Fixture: FitnessTrackerApp in logic-only mode (no GUI)."""
    return FitnessTrackerApp(master=None, enable_gui=False)


def test_add_valid_workout(app):
    entry = app.add_workout_logic("Running", 30)
    assert len(app.workouts) == 1
    assert entry["workout"] == "Running"
    assert entry["duration"] == 30


def test_add_missing_fields(app):
    with pytest.raises(ValueError, match="Workout and duration required"):
        app.add_workout_logic("", "")


def test_add_invalid_duration(app):
    with pytest.raises(ValueError, match="Duration must be a number"):
        app.add_workout_logic("Cycling", "abc")
