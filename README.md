# rciam-map-ip-to-country
A Python-based tool for mapping ips to countries and store the respective login information to a DB.
## Prerequisites
If you want to use MaxMind GeoIP Databases(free version), MaxMind provides a PPA for recent version of Ubuntu. To add the PPA to your APT sources, run:
```
sudo add-apt-repository ppa:maxmind/ppa
```
Then install the packages by running:
```
sudo apt update
sudo apt install libgeoip1 libgeoip-dev geoip-bin
```

## Installation
```
git clone https://github.com/rciam/rciam-map-ip-to-country.git
cd rciam-map-ip-to-country
cp config.py.example config.py
vi config.py
```

Create a Python virtualenv, install dependencies, and run the script
```
virtualenv -p python3 .venv
source .venv/bin/activate
(venv) pip3 install -r requirements.txt
(venv) python3 -m Utils.install
(venv) python3 ipToCountry.py
🍺
```

## License
Licensed under the Apache 2.0 license, for details see LICENSE.



