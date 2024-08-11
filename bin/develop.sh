#/bin/bash
cd "$(dirname "$0")"
cd ..

nodemon -e py -x "python3 -m unittest discover"