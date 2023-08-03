#!/bin/bash

# Update
sudo apt update
echo ""
echo ""
echo "-----U P D A T E D-----"
echo ""
echo ""
# Upgrade
sudo apt upgrade -y
echo ""
echo ""
echo "-----U P G R A D E D-----"
echo ""
echo ""
# Install nginx (NOTE, nginx starts automatically after install)
sudo apt install nginx -y
echo ""
echo ""
echo "-----N G I N X   I N S T A L L E D-----"
echo ""
echo ""
# Enable nginx
sudo systemctl enable nginx
echo ""
echo ""
echo "-----N G I N X   E N A B L E D-----"
echo ""
echo ""
# Configure reverse proxy
sudo apt install sed -y
sudo sed -i 's|try_files $uri $uri/ =404;|proxy_pass http://localhost:3000;|' /etc/nginx/sites-available/default
echo ""
echo ""
echo "-----R E V E R S E   P R O X Y   C O N F I G U R E D-----"
echo ""
echo ""
#restart nginx again
sudo systemctl restart nginx
# Enable nginx
sudo systemctl enable nginx
echo ""
echo ""
echo "-----N G I N X   R E S T A R T E D   A N D   E N A B L E D-----"
echo ""
echo ""
#  Get app folder
sudo git clone https://github.com/FPM-Spartan/tech241-sparta-app.git app
echo ""
echo ""
echo "----- A P P   F O L D E R   C L O N E D-----"
echo ""
echo ""
# Install correct version (dependency) of nodejs
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt install nodejs -y
echo ""
echo ""
echo "-----N O D E J S   I N S T A L L E D-----"
echo ""
echo ""
# Install pm2
sudo npm install pm2 -g
echo ""
echo ""
echo "-----P M 2   I N S T A L L E D-----"
echo ""
echo ""
# give app folder correct permissions
sudo chmod  777 app
echo ""
echo ""
echo "-----A P P   F O L D E R   P E R M I S S I O N S   C H A N G E D-----"
ls -l
echo ""
echo ""
#  Create env var to allow connection to db vm
export DB_HOST=mongodb://20.90.164.54:27017/posts # Change the IP address to whatever the Database VM public IP is on Azure. For AWS 
echo ""
echo ""
echo "----- E N V   V A R   C R E A T E D   F O R   D B   H O S T-----"
printenv DB_HOST
echo ""
echo ""
#  Go to app directory
cd app
pwd
echo ""
echo ""
echo "-----C U R R E N T   D I R E C T O R Y   C O R R E C T-----"
echo ""
echo ""
# Install npm
npm install -y
echo ""
echo ""
echo "-----N P M   I N S T A L L E D-----"
echo ""
echo ""
# manually seed database
echo "Clearing and seeding database..."
node seeds/seed.js
echo ""
echo "-----D A T A B A S E   S E E D E D-----"
# kill previous app backgrund process
pm2 kill 
# Start npm
#nohup node app.js >/dev/null 2>&1 #(OLD VERSION)
pm2 start 'npm start'
echo ""
echo ""
echo "-----A P P   S T A R T E D-----"
echo ""
echo "-----E N D-----"
