test:
	sh scripts/check_data.sh
	sh scripts/run_energies_test.sh  
	sh scripts/run_sep_test.sh

install_modules:
	pip freeze > requirements.txt