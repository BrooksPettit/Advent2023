PYTHON := venv/bin/python3
PIP := venv/bin/pip3
PYTEST := venv/bin/pytest

$(PYTHON):
	python3 -m venv venv

$(PYTEST): $(PYTHON) requirements.txt
	$(PIP) install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv

.PHONY: test
test: $(PYTEST)
	$(PYTEST)
