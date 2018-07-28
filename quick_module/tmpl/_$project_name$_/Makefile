development:
	pip install --upgrade pip
	pip --no-cache-dir install -r requirements.development


runtests:
	python -m unittest discover


coverage:
	find . -name "__pycache__" -or -name "*.pyc" | grep -v '.tox' | grep -v '.penv' | xargs rm -rf
	coverage erase && coverage run -m unittest discover && coverage html && coverage report


servereport:
	cd .htmlcov && python -m SimpleHTTPServer 8000


watch:
	watchmedo shell-command -p '*.py' -i '*_flymake.py;*.pyc;*.penv*' -c 'make coverage' -W -R
