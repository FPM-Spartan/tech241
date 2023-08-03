# Plan

Virtual Machines in Azure
Two tier architecture
Running the sparta test app

## 1. Diagram of Two Tier Architecture

In software development recently, trends have pointed towards having apps made up of smaller apps. These are called microservices.

For example, an online business could have its payment system, inventory management, shopping cart all created separately.

These can be connected to each other via a main app.

Loose coupling architecture.


The Sparta App we deployed was deployed on **TWO TIER ARCHITECTURE**, since we have a VM for the app and a VM for the database. 
In the previous example, the payment method could be made using this two tier architecture. There are differing opinions on what counts as a "tier", whether something should be classed as one or two tier etc.

## 2. VM Diagram

![Alt text](azure/images/vm-diagram.JPG)

Virtual machine is a machine within a machine.

Cloud VM - VNET is a house, Subnet is a room within the house, the VM is the computer in that room.

We access the VM with our SSH Key pair. Public Key is padlock, private key is key.

our VM output is viewable at the public IP address.

This passes through two layers of security, which are also both linked together.

## 3. Creating a VM

For this test app, I followed this process twice, making only minor changes.

I will not click create now because I have already made the VMs to save myself time and Sparta money.


## 4. Explaining the commands

In DevOps, we will always manually run each command to make sure it works.

I have already done this to save time

## 5. Run the scripts

## 6. Show it worked

## 7. Blockers and Business value

IF NPM INSTALL FAILS / NODE_MODULES IS NOT CREATED IN THE APP FOLDER, YOU NEED TO CHANGE THE PERMISSIONS OF THE APP FOLDER WITH CHMOD*

I gave rwx permissions to all groups and it worked. This does not adhere to the principle of least permissions, but it did help with getting minimum viable product.

If the connection is taking too long/ not showing up in web browser, make sure the inbound port rules are correctly saved, particularly they are CUSTOM and not MONGODB in the third drop down.

Check and double check commands that you have copied and pasted between terminal windows because you might not have copied all of it.


This method of app deployment is really beneficial for businesses

1. smaller dedicated micro-apps theoretically will have a faster load time than one monolothic app. Faster load times are good for businesses for many common sense reasons.
2. Being able to automate processes such as this can help to free up manpower to focus on new or more important tasks.