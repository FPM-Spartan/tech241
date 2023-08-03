#!/bin/bash

#  Create global env var to allow connection to db vm
export DB_HOST=mongodb://20.90.164.54:27017/posts # Change the IP address to db vm.
printenv DB_HOST
#  Go to app directory
cd app
# Install npm
npm install -y

# manually seed database
echo "Clearing and seeding database..."
node seeds/seed.js

# Start npm
pm2 start 'npm start'