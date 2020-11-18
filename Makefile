# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
		@pip install -r requirements.txt

install:
		@pip install .

check_code:
		@flake8 scripts/* process/*.py
