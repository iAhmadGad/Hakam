targets: prerequisites
	pyinstaller

setup: requirements.txt
	pip install -r requirements.txt

install:
	pyinstaller --onefile src/main.py --name=hakam
	mv ./dist/hakam /bin/

clean:
	rm -rf */__pycache__
