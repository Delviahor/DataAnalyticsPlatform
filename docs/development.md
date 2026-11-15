# Development Guide – DataAnalyticsPlatform

## 1. Introduction

This guide describes the procedures required to configure the development environment, install dependencies, run the application, and execute automated tests for DataAnalyticsPlatform.

## 2. Prerequisites

The following tools and requirements are needed to work with the project:

- Windows 10 or a higher version.
- Python 3.14.
- Git.
- Visual Studio Code or another Python-compatible editor.
- PowerShell or an equivalent terminal.

## 3. Getting the Project

Clone the repository:

```bash
git clone https://github.com/Delviahor/DataAnalyticsPlatform
```

Navigate to the project directory:

```bash
cd DataAnalyticsPlatform
```

## 4. Creating the Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
python -m venv .venv
```

Activate the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Once activated, the terminal should display the `(.venv)` indicator.

## 5. Installing Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## 6. Project Structure

The source code is located in `app/`.

The data processing modules are organized within:

```text
app/data/
```

Test and demonstration datasets are stored in:

```text
datasets/
```

Automated tests are located in:

```text
tests/
```

## 7. Running the Project

The current entry point is:

```bash
python -m app.main
```

This module allows users to run the current demonstration of the processing and inspection of the sample dataset.

## 8. Running the Tests

Run the entire test suite:

```bash
python -m pytest -v
```

Run tests for a specific module:

```bash
python -m pytest tests/test_analytics.py -v
```

Run integration tests:

```bash
python -m pytest tests/test_integration.py -v
```

Measure code coverage:

```bash
python -m pytest --cov=app --cov-branch --cov-report=term-missing
```

## 9. Code Quality and Style

The project uses Ruff for static analysis and code style enforcement.

Check the code:

```bash
ruff check .
```

Apply automatic fixes when appropriate:

```bash
ruff check . --fix
```

Automatic fixes must be reviewed before being incorporated into the repository.

## 10. Version Control

The project uses Git to manage changes.

Check the repository status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Description of the change"
```

Push changes to the remote repository:

```bash
git push origin main
```

Commit messages should clearly and concisely describe the changes made.

## 11. Development Conventions

The following conventions have been established:

- Maintain a clear separation of responsibilities between modules.
- Use descriptive names for functions and variables.
- Implement validation for inputs and parameters.
- Avoid modifying original DataFrames when operations are expected to be non-destructive.
- Include unit tests for new features.
- Update integration tests whenever interfaces between modules change.
- Keep documentation up to date.
- Do not introduce dependencies without justifying their necessity.



## 12. Development Environment Evolution

As the project progresses, new tools and procedures will be introduced according to the requirements of each stage.

Future stages include:

- FastAPI and Streamlit for the web application.
- PostgreSQL for data persistence.
- Scikit-learn for Machine Learning.
- Docker for containerization.
- Deployment, security, and monitoring tools.

These technologies are not part of the current execution requirements for Stage 3.