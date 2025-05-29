# CI/CD Pipeline - Part 1

**Name:** Nikhila Koneru  
**NUID:** 002032245

## About This Project

This is my solution for the CI/CD Pipeline Assignment Part 1. I've implemented the Boyer Moore majority voting algorithm in Python, written tests using pytest, and set up automatic testing with GitHub Actions.

## What's Included

- `solution.py` - The Boyer Moore algorithm that finds the majority element in a list
- `test_solution.py` - Test cases to make sure the algorithm works correctly
- `requirements.txt` - Python packages needed (just pytest)
- `.github/workflows/main.yml` - GitHub Actions configuration for automatic testing

## How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
pytest test_solution.py
```

## How It Works

The Boyer Moore algorithm finds which element appears more than half the time in a list. It's efficient because it only needs to go through the list twice and uses minimal memory.

The solution handles:
- Normal lists with majority elements
- Empty lists (raises an error)
- Lists with mixed types (raises an error)

## Automated Testing

Every time code is pushed or a pull request is created, GitHub Actions automatically:
1. Sets up Python 3.11
2. Installs dependencies
3. Runs all the tests
