init:
    pip install -r requirements.txt

test:
    pip install -r test_requirements.txt
    py.test tests

.PHONY: init test