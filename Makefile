# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
		@pip install -r requirements.txt

install:
		@pip install .

check_code:
		@flake8 scripts/* process/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr mlproject-*.dist-info
	@rm -fr mlproject.egg-info
