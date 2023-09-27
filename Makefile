install:
	sh scripts/check_pip.sh
	sh scripts/install_font_dependencies.sh 

test:
	sh scripts/check_data.sh
	sh scripts/run_sep_test.sh
	sh scripts/run_energies_test.sh  
	sh scripts/check_test.sh
	
clean:
	rm figs/*

uninstall_latex_dependencies:
	sh scripts/uninstall_font_dependencies.sh
