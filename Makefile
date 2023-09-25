test:
	sh scripts/check_pip.sh
	sh scripts/install_font_dependencies.sh 
	sh scripts/check_data.sh
	sh scripts/run_energies_test.sh  
	sh scripts/run_sep_test.sh
	sh scripts/check_test.sh

clean:
	sh scripts/uninstall_font_dependencies.sh 
	rm figs/*
