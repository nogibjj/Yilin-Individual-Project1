install:
    pip install -r requirements.txt

format:
    black src/ tests/

lint:
    ruff src/ tests/

test:
    pytest --nbval notebook/my_analysis.ipynb
    pytest tests/test_script.py
    pytest tests/test_lib.py

all: install format lint test
