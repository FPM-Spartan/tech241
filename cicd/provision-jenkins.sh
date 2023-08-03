#!/bin/bash

# Script to provision a fresh vm with Jenkins (Ubuntu 18.04 LTS; openjdk-17)

# update
sudo apt update -y

# manually import jenkins repo key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA

# add repo to apt source list
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# update again
sudo apt update

# upgrade
sudo apt upgrade -y

#  install java
sudo apt install openjdk-17-jre -y

# install jenkins
sudo apt install jenkins -y

# restart jenkins
sudo systemctl restart jenkins

# enable jenkins
sudo systemctl enable jenkins


