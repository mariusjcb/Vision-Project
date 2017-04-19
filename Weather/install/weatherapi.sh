# set env colors
TERM=xterm-color
GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
CLICOLOR=1
LSCOLORS=ExFxCxDxBxegedabagacad

COLOR_NC='\e[0m' # No Color
COLOR_LIGHT_BLUE='\e[1;34m'
COLOR_LIGHT_GREEN='\e[1;32m'
COLOR_LIGHT_RED='\e[1;31m'
COLOR_YELLOW='\e[1;33m'

# install dependencies
if ! (hash python) >/dev/null; then
    echo -e "Installing python...\n";
    (yes | pkg install python) >/dev/null 2>/dev/null;
    (sudo yes | python -m ensurepip) >/dev/null 2>/dev/null;
fi

if ! (python -c "import requests") >/dev/null 2>/dev/null; then
    echo -e "Fetching requests python module...\n"
    (sudo yes | pip install requests) >/dev/null 2>/dev/null;
fi;

# install WeatherAPI module
# replace existing module by default: yes
REPLACE="y"

# if module exists
# ask user if want to replace
if (python -c "import WeatherAPI") >/dev/null 2>/dev/null; then
    echo -e "Python module \"WeatherAPI\" already exists."
    read -p "You want to REPLACE? (y/n): " REPLACE </dev/tty; echo ""
fi;

# replace / install weatherapi module
if [ $REPLACE == "y" ]; then
    echo "Installing the new WeatherAPI python module..."
    (cd ./include/ && sudo yes | python setup.py install) >/dev/null 2>/dev/null
    echo -e "\n${COLOR_LIGHT_BLUE}Weather API: Installation finished${COLOR_NC}" #| fmt -c -w $cols
    sleep 0.5
else
    echo -e "\n${COLOR_YELLOW}Weather API: No changes${COLOR_NC}" #| fmt -c -w $cols
fi;

# remove residual directories
(cd ./include/; sudo rm -R ./WeatherAPI.egg-info; sudo rm -R ./dist; sudo rm -R ./build) >/dev/null 2>/dev/null

# reset var to default yes
REPLACE="y"

# if weather command exists
# ask user if want to replace
if (hash weather) >/dev/null 2>/dev/null; then
    echo -e "\nThe 'weather' command already exists."
    read -p "You want to REPLACE? (y/n): " REPLACE </dev/tty
fi;

# replace / install weather command
if [ $REPLACE == "y" ]; then
    sudo cp ./weather.py /usr/local/bin/weather
    sudo chmod a+x /usr/local/bin/weather

    echo -e "\n${COLOR_LIGHT_GREEN}Weather Command Installed${COLOR_NC}" #| fmt -c -w $cols
    echo -e "${COLOR_LIGHT_GREEN}Now you can use '${COLOR_LIGHT_RED}weather -help${COLOR_LIGHT_GREEN}' in your shell${COLOR_NC}\n" #| fmt -c -w $cols

    sleep 1.25
else
    echo -e "\n${COLOR_LIGHT_GREEN}We are done.\nCommand was not changed${COLOR_NC}" #| fmt -c -w $cols
fi;