# Infrastructure as Code Notes
---
## Intro

During CI/CD week, we automated integration and deployment. But we still manually set up our VMs to deploy to. IaC is where we will automate this part.

## IaC
Infrastructure as Code is the codeification of everything.

Eg: We used a bash script to provision a single vm/instance. How would we do this on a hundred? Use a playbook with Ansible. 

IaC covers two main areas:
1. Configuration Management
2. Orchestration

Config management: Chef, Puppet, Ansible

Orchestration: AWS CloudFormation, Terraform

Terraform is cloud independent. Scripts can be run in any cloud. 

Terraform (orchestration) makes the infrastructure, Ansible (config management) sets up the commands

Terraform will create the VMs for us. Ansible will provision them for us.

## Configuration Management with Ansible
### Overview
Ansible is a config management tool used heavily in DevOps and DevSecOps.

Why use Ansible? It's simple, lightweight, and it's **agentless** (The agent nodes that Ansible communicates with do not need to have Ansible installed).

### Architecture

![Alt text](images/ansible-diagram-01.png)

Master node: Ansible controller (in our case, this is on AWS EC2 instance, but can be hybrid or on prem)

Agent node: we use Ubuntu 18.04 LTS. We can have as many agents as we like. Our project requires a node for the app and a node for the database. Ansible uses a method of communication to securely connect to agent nodes. We will be using SSH. Ansible **pings** the agent nodes. The ping has to get through the SSH.

Default directory structure: Inventory of hosts (eg: ip of the db vm and ip of the app vm, and **location of the pem file**), and playbooks.

Playbooks: sets of instructions 

## Orchestration with Terraform

## Overview

### What is Terraform?

An IaC tool that lets you define your cloud resources (and on-prem) in human readable code.


### Why use Terraform?

You can use a consistent workflow to provision, manage, and track infrastructure throughout its lifecycle.

You can use it to automate changes to your infrastructure. Terraform abstracts the underlying logic of creating resources, so you are writing the config files in a way that describes how you want your infrastructure's end state to be.

You can submit your Terraform config files to a VCS (GitHub) and use Terraform Cloud to manage Terraform workflows across teams. This means that your team can all collaborate on Terraform.

### Benefits?

**Cloud Independent.** Terraform can talk to all cloud providers. Allows you to use the same tools and processes regardless of what cloud provider you are using. Write scripts only once and reuse them in different clouds. Save a business time and money.

**Reusability.** Infrastructure can be defined in a modular way, which can then be used again in a new deployment. Helps to reduce duplication and manage infrastructure at scale.

**Version History.** This is automatically maintained and allows for rollbacks if mistakes or errors occur. Allows for quick failure/disaster recovery.

**Collaborative**. As mentioned, Terraform can be used collaboratively using version control.

**Consistent.** Terraform's use of high level config language means you specify with consistency and predictability.

### Who is using it?

**Almost every Sparta client uses Terraform. Most of the largest companies in the world also use it.**

Reportedly, at least 1941 companies use it, including:

* Uber.
* Udemy.
* Instacart.
* LaunchDarkly.
* Slack.
* Robinhood.
* Twitch.
* Delivery Hero.
---