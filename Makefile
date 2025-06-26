.PHONY: help install run clean venv activate

PYTHON=python3
VENV_DIR=venv
ACTIVATE=. $(VENV_DIR)/bin/activate

help:
	@echo "Makefile commands:"
	@echo "  make install     - Create venv and install dependencies"
	@echo "  make run         - Run the FastAPI app"
	@echo "  make clean       - Remove venv"
	@echo "  make activate    - Show how to activate the venv manually"

install:
	$(PYTHON) -m venv $(VENV_DIR)
	$(ACTIVATE) && pip install --upgrade pip && pip install -r requirements.txt

run:
	$(ACTIVATE) && python run.py

clean:
	rm -rf $(VENV_DIR)

activate:
	@echo "To activate virtualenv, run:"
	@echo "  source $(VENV_DIR)/bin/activate"