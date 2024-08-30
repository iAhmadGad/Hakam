setup: requirements.txt
	pip install -r requirements.txt

build:
	pyinstaller --onefile src/hakam/main.py --name=hakam

install:
	mv dist/hakam /usr/bin/hakam

clean:
	find * -type d -name '__pycache__' -exec rm -rf {} +
	find * -type f -name '*~' -exec rm -f {} +
