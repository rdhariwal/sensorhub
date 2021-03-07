.DEFAULT_GOAL := help

help:	## Show this help.
	@echo "$$banner_ascii"
	@echo "------------------------------------------------------------------------------"
	@echo "------------------------------------------------------------------------------"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
	@echo "------------------------------------------------------------------------------"

start:	## Start server on port 80
	@echo "starting http server on http://localhost"
	@echo "hit ctrl + c to stop"
	python3 server.py
