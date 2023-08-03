#!/bin/bash

# update
sudo apt update -y
# to upgrade
sudo apt upgrade -y
# Download the key for the right version of mongodb
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
# Source list
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
# Update again
sudo apt update -y
# Install mongodb
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
# Edit bindip in mongod.conf to allow connections from anybody
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf
# Restart mongod to ensure the changes have gone through
sudo systemctl restart mongod
# Enable mongod (starts the system process for mongodb on startup of the VM)
sudo systemctl enable mongod

