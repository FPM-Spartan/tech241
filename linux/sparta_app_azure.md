# Sparta App

Sparta test app

Need to install Node js and nginx

nginx runs on port 3000

2 features:
* a front page (no database)
* posts page (shows data retrieved from the database)

Two stages:

* run it manually
* once it works manually, automate it incrementally with BASH scripts (automate one VM, then the other, then the connection of the two)

**Requirements to run the app:**

* Linux VM,  version Ubuntu 18.04 LTS
* Update and upgrade
* Web server to display the pages, nginx (dependency)
* right version of node js installed, version 12.x (anything version 12) 
* app folder
  * be able to cd into this and run 2 commands:
    * npm install (node package manager)
    * node app.js **OR** npm start
    * 


 (dependency (the app **depends** on this being specific to run)) 

 ## Getting the app onto the VM

 for all methods:

 * unzip folder
 * don't have app folder inside of app folder

 ### Method 1: git clone

 * create a gitrepo - tech241-sparta-app
 * create a folder "tech241-sparta-app" on your local machine
 * copy app folder to your local repo
 * sync with your remote repo on GitHub
 * SSH into your VM and then git clone

### Method 2: scp OR rsync

* will need the path to your private key
* path to folder
* adminuser@[ip address of vm]


## Installing the Sparta app

* get right version of nodejs
* install nodejs
* install pm2
* cd into app folder
* install npm in app folder
* start the app
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

sudo apt install nodejs -y
sudo npm install pm2 -g
npm install
npm start OR node app.js
```

Go to azure and add an inbound security rule - destination port ranges = port 3000 (where our app is running), TCP, Allow#

NB: Use Ctrl C to exit out of an app. Don't use ctrl Z to exit out of the app in terminal.

## Creating the  DB VM

Create the VM first.

Reqs to run DB VM:

* Linux VM - Ubuntu 18.04 LTS
* update and upgrade
* Install mongo db  - version 3.2.x (non relational db, stores info as documents)
  * download key for right version
  * source list -> specify mongodb version

Steps:
* update and upgrade (again, careful with upgrade!)
* get the right version of mongodb
* install mongodb
 
```
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -

echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
```
  * update again **(Important to run updates often in scripts)**

* Configure mongo db to accept connections from app VM (by default it is set up to noly accept connections fromm itself, we have to go in and change this)
```
sudo nano /etc/mongod.conf
 ```
find port that mongodb is using
  * change bindip to 0.0.0.0 (**NOTE: this is a security issue, only okay for testing. In production, DO NOT DO THIS, specify the IP you want**)
  * make sure mongod is enabled
```
sudo systemctl restart mongod #(to make sure mongo db always restarts on run)
sudo system ctl enable mongod
```

## Connecting the two VMs

set up a persistent environment variable in the app vm so that the vm can look up a value.

In app VM: 

```
export DB_HOST=mongodb://<IP-ADDRESS>:27017/posts (get the public IP of the database VM)
```


In Azure portal, add inbound security rule to db vm.
* add 27017, using TCP, Allow


# Automating

## Automating running the app

**TEST MANUALLY FIRST**

One method of getting the app to run in the baackground and not keep the terminal engaged:
```
nohup node app.js >/dev/null 2>&1
```

nohup = no hangup. Basically commanding the terminal to not hangup at the end of the script.

Every time you run a script, you specify a shebang bin/bash. This tells linux you want to run the script using a bash shell. Linux is good at separating and running shells. Running a script is running a shell within your shell. When the script finishes, it does not need that shell any more and so hangs up the shell. So if you do not put nohup at the end then it will hang up all the user processes run in the script.

THE PROBLEM WITH USING NOHUP TO RUN APPS IN BACKGROUND? 

You cannot run multiple nohup commands, port 3000 was already occupied. One process to one port. WE would have to find some way to kill that process first before we can run it again, which can cause problems. We would have to find out the process ID and kill that, it can get complicated.

This works to get the app into the background, but why is it not ideal? Why is pm2 version better?

* in a production scenario, pm2 is better becauase it gives you the extra information in the table which would be better for monnitoring?

```
pm2 start 'npm start'
```

use "pm2 stop all" to stop pm2, because even if you exit out of the terminal, the app will still run.

## Automating setting up the DB VM

edit bindip in mongod.conf:
```
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf

Dangerous method:  sed -i 's/^bindip=.*/bindip=0.0.0.0/' /etc/mongod.conf
```

If that IP appears at multiple places in the file, it will be overwritten at all of them.

## Automating the connection of both VMs

In your provision.sh in the app VM, you need to add the env var command from the manual process, after installing pm2 and before cd into app folder and npm install.

```
export DB_HOST=mongodb://<IP-ADDRESS>:27017/posts (get the public IP of the database VM)
```

---

## TROUBLESHOOTING
Sometimes trying to get the app to run is nightmare.

**IF NPM INSTALL FAILS / NODE_MODULES IS NOT CREATED IN THE APP FOLDER, YOU NEED TO CHANGE THE PERMISSIONS OF THE APP FOLDER WITH CHMOD**

I gave rwx permissions to all groups and it worked. This does not adhere to the principle of least permissions, but it did help with getting minimum viable product.

If the connection is taking too long/ not showing up in web browser, make sure the inbound port rules are correctly saved, particularly they are CUSTOM and not MONGODB in the third drop down.

Why is mongodb failing to be enabled on new VM? ---- **YOU NEED TO CHECK EVERY SINGLE LINE IN THE SCRIPT ESPECIALLY IF YOU HAVE COPIED AND PASTED FROM NANO INTO VS CODE AND BACK AGAIN. THIS IS BECAUSE SOMETIMES NANO MIGHT NOT COPY AN ENTIRE LINE IF IT GOES OFF THE EDGE OF THE SCREEN. CHECK AND DOUBLE CHECK THIS!**

---

## Reverse Proxy

Reverse proxy is how you can get rid of the port 3000 part of the url. This is good because it makes the url cleaner and also prevents the port from being displayed, which can be a security concern.

1. Get into the following file in nano:
  ```
  sudo nano /etc/nginx/sites-available/default
  ```
2. change the line:
```
try_files $uri $uri/ =404;
```
to the following:
```
proxy_pass http://localhost:3000;
```
3. Save and exit nano, then test it with:
   ```
   sudo nginx -t
   ```
4. restart nginx
5. paste app vm ip address into web browser without the :3000 to test if it has worked.

---
## Adding an image to the sparta app from Blob

1. SSH into your Azure VM
2. Install Azure CLI on your Azure VM - this will give you access to the az command.
3. Login to Azure
4. Download a cat picture (jpg) of your choice to your VM - name is newcat.jpg 
5. Upload the cat picture to Azure blob storage (Hint: You will first need a storage account + container) - in blob storage the same file should be called uploadedcat.jpg
6. Set access permissions so it can be viewed by the public
7. Modify the file index.ejs (found in views folder inside the app folder) - add an <img> tag to the HTML so display the uploadedcat.jpg image on the Sparta front page.
8. Run the app (no database) to check your blob image displays on the Sparta test app's front page.

### Documentation of the process

I used curl to download the image directly from a URL onto the VM.

I found I had to change permission for some files and directories in the app folder so that I could add new files and edit existing ones.

I almost undid all of my work by running my bash script again which would have almost certainly have overwritten these changes!

### Screenshot

![Alt text](images/sparta_app_blob_image.png)

