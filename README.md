ACEest Fitness Tracker

Overview
The ACEest Fitness Tracker is a Python desktop application built using Tkinter. It allows users to log workouts with duration and review them in a simple interface.
The project demonstrates:
-> Core Python and Tkinter development
-> Automated testing with Pytest
-> Containerization with Docker
-> CI/CD pipeline using GitHub Actions


Features
-> Add workouts with duration (in minutes)
-> Input validation for missing or invalid entries
-> View logged workouts in a list format
->Separation of business logic for easier testing
->Dockerized application for portability
->Automated testing integrated in CI/CD pipeline



Project Structure
devop1_assignment1/
│── aceest_fitness/
│   └── ACEest_Fitness.py     # Main application code
│── tests/
│   └── test_fitness.py       # Pytest unit tests
│── requirements.txt          # Dependencies
│── Dockerfile                # Docker image definition
│── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions pipeline
│── README.md                 # Project documentation



Setup and Usage

Run Locally

Clone the repository:
git clone https://github.com/<your-username>/devop1_assignment1.git
cd devop1_assignment1

Install dependencies:
pip install -r requirements.txt

Run the application:
python aceest_fitness/ACEest_Fitness.py


Run with Docker

Build the Docker image:
docker build -t aceest-fitness .

Run the application:
docker run --rm aceest-fitness


Run tests inside the container:
docker run --rm aceest-fitness pytest -v



Testing

Unit tests are written with Pytest and cover:
->Adding a valid workout
->Handling missing input fields
->Handling invalid duration values

Run tests locally:
pytest -v


CI/CD Pipeline

The GitHub Actions workflow (.github/workflows/ci.yml) is configured to:
->Build the Docker image automatically
->Run Pytest unit tests inside the Docker container
->Ensure code stability before merging changes
