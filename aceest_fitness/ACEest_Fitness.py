import tkinter as tk
from tkinter import messagebox


class FitnessTrackerApp:
    def __init__(self, master=None, enable_gui=True):
        """
        :param master: Tkinter root (only needed for GUI mode)
        :param enable_gui: If False, disables messagebox popups (for testing/CI)
        """
        self.master = master
        self.enable_gui = enable_gui
        self.workouts = []

        if master:  # Only build GUI if a root window is provided
            master.title("ACEestFitness and Gym")

            # Labels and Entries for adding workouts
            self.workout_label = tk.Label(master, text="Workout:")
            self.workout_label.grid(row=0, column=0, padx=5, pady=5)
            self.workout_entry = tk.Entry(master)
            self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

            self.duration_label = tk.Label(master, text="Duration (minutes):")
            self.duration_label.grid(row=1, column=0, padx=5, pady=5)
            self.duration_entry = tk.Entry(master)
            self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

            # Buttons
            self.add_button = tk.Button(master, text="Add Workout", command=self.add_workout)
            self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

            self.view_button = tk.Button(master, text="View Workouts", command=self.view_workouts)
            self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    # ---------------------------
    # GUI methods (use messagebox)
    # ---------------------------
    def add_workout(self):
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

        try:
            entry = self.add_workout_logic(workout, duration_str)
            if self.enable_gui:
                messagebox.showinfo("Success", f"'{entry['workout']}' added successfully!")
            self.workout_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
        except ValueError as e:
            if self.enable_gui:
                messagebox.showerror("Error", str(e))

    def view_workouts(self):
        if not self.workouts:
            if self.enable_gui:
                messagebox.showinfo("Workouts", "No workouts logged yet.")
            return

        workout_list = "Logged Workouts:\n"
        for i, entry in enumerate(self.workouts):
            workout_list += f"{i+1}. {entry['workout']} - {entry['duration']} minutes\n"

        if self.enable_gui:
            messagebox.showinfo("Workouts", workout_list)

    # ---------------------------
    # Logic-only methods (safe for tests)
    # ---------------------------
    def add_workout_logic(self, workout, duration):
        if not workout or not duration:
            raise ValueError("Workout and duration required")
        try:
            duration = int(duration)
        except ValueError:
            raise ValueError("Duration must be a number")

        entry = {"workout": workout, "duration": duration}
        self.workouts.append(entry)
        return entry


# Run GUI only when executing this file directly
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root, enable_gui=True)
    root.mainloop()
