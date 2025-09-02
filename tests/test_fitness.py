import pytest
from unittest import mock
from aceest_fitness.ACEest_Fitness import FitnessTrackerApp


class DummyWidget:
    """Generic dummy widget for Tkinter (safe in headless tests)."""
    def __init__(self, *args, **kwargs):
        self.value = ""

    # Simulate Entry widget behavior
    def insert(self, index, text):
        self.value = str(text)

    def delete(self, start, end=None):
        self.value = ""

    def get(self):
        return self.value

    # Layout methods (do nothing)
    def grid(self, *args, **kwargs): return None
    def pack(self, *args, **kwargs): return None
    def place(self, *args, **kwargs): return None


@pytest.fixture
def app():
    """Fixture: FitnessTrackerApp with Tkinter fully mocked."""
    with mock.patch("tkinter.Tk") as MockTk, \
         mock.patch("tkinter.Entry", new=DummyWidget), \
         mock.patch("tkinter.Label", new=DummyWidget), \
         mock.patch("tkinter.Button", new=DummyWidget), \
         mock.patch("tkinter.Frame", new=DummyWidget), \
         mock.patch("tkinter.Listbox", new=DummyWidget), \
         mock.patch("tkinter.Scrollbar", new=DummyWidget):

        mock_root = mock.MagicMock()
        MockTk.return_value = mock_root

        # Prevent window/title calls from crashing
        mock_root.title = lambda *a, **k: None
        mock_root.withdraw = lambda *a, **k: None
        mock_root.destroy = lambda *a, **k: None

        app = FitnessTrackerApp(mock_root)
        yield app


def test_add_valid_workout(app):
    app.workout_entry.insert(0, "Running")
    app.duration_entry.insert(0, 30)
    app.add_workout()

    assert len(app.workouts) == 1
    assert app.workouts[0]["workout"] == "Running"
    assert app.workouts[0]["duration"] == 30


def test_add_missing_fields(app):
    app.workout_entry.delete(0, "end")
    app.duration_entry.delete(0, "end")
    app.add_workout()

    assert len(app.workouts) == 0


def test_add_invalid_duration(app):
    app.workout_entry.insert(0, "Cycling")
    app.duration_entry.insert(0, "abc")
    app.add_workout()

    assert len(app.workouts) == 0
