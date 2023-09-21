test:
	pip install -r requirements.txt
	sh scripts/install_font_dependencies.sh 
	sh scripts/check_data.sh
	sh scripts/run_energies_test.sh  
	sh scripts/run_sep_test.sh
	sh scripts/check_test.sh

