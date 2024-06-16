targets: prerequisites
	multiliney
	pyinstaller

setup: requirements.txt
	pip install -r requirements.txt

install:
	pyinstaller --onefile src/main.py --name=hakam
	mv ./dist/hakam /bin/

clean:
	find * -type d -name '__pycache__' -exec rm -rf {} +
	find * -type f -name '*~' -exec rm -f {} +
