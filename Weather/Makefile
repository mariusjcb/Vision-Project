# install dependencies
SHELL:=/usr/bin/bash

install-weatherapi-module:
	@echo "Weather installation started..." \

	# install pkg
	@if ! (hash pkg) >/dev/null 2>/dev/null; then \
		echo -e "Initialising PKG...\n"; \
		yes | pkg >/dev/null 2>/dev/null; \
		yes | pkg update >/dev/null 2>/dev/null; \
		yes | pkg upgrade >/dev/null 2>/dev/null; \
	fi \

	# install sudo
	@if ! (hash sudo) >/dev/null; then \
			echo -e "Installing sudo...\n"; \
			yes | pkg install sudo >/dev/null 2>/dev/null; \
	fi

	# start module installing...
	@sudo chmod 777 ./install/weatherapi.sh
	@yes | ./install/weatherapi.sh
	@sudo chmod 755 ./install/weatherapi.sh