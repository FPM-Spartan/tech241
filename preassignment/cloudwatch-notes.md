# Cloudwatch Notes

## Intro
Cloudwatch provides monitoring and alerting on AWS Cloud.

Benefits: payg pricing, easy usage.

### Course Overview:

* Intro to AWS
* Understanding Monitoring and Alerting Services on AWS
* Deep Dive AWS CloudWatch Alarms and Dashboards
* Monitoring & Alerting for:
  * AWS EC2 Instances
  * AWS EBS (Elastic Block Store)
  * AWS RDS (Relational DB Service)
  * AWS ELB (Elastic Load Balancer)
  * AWS **Billing and Costs**

### ILOs:

* Understand Cloud Computing and AWS
* Understand monitoring and alerting services on AWS
* Deep knowledge on CloudWatch Alarms
* Monitoring and Alerting AWS Services

### Requirements:

* AWS Account
---
## AWS Intro

Cloud Computing allows for building sophisticated and scalable applications.

Hardware virtualisation is at the core of cloud computing.

Companies are switching to Cloud for many reasons. These include avoiding up front infrastructure costs. Get apps up and running faster.

**IaaS:** online services that abstract user from infrastructure details

**PaaS:** offers developer env to app developers. Toolkits and standards for dev. Eg: Beanstalk, Azure websites.

**SaaS:** On demand software, pay per user basis. Eg Office 365.

### Why AWS?

* Secure
* Compliant
* Hybrid compatible
* Convert CapEx to OpEx
* Lower Total costs
* No need to guess capacity
* Scalable and Flexible
* Culture of innovation: experiment often and fail without risk

### Who is Using AWS?

* Instagram
* Linkedin
* dropbox
* tumblr
* airbnb

* Unilever
* Lamborghini
* TATA motors
* Lionsgate (dev and test, sharepoint and SAP,more dev and test work, faster )

### Services Provided by AWS

* Enterprise
  * virtual desktops
  * sharing and collab
* Platforms
  * Analytics
  * App services
  * Deployment and management
  * Mobile services
* Admin and Security
  * identity management
  * access control
  * usage and resource tracking
  * service catalog
  * key storage and management
  * monitoring and logs
* Core Services
  * Compute
  * Storage
  * CDN (Content Delivery Networks)
  * Databases
  * Networking
* Infrastructure
  * Regions
  * Availability Zones
  * Points of Presence

**Products:**

Compute:
* EC2
* Lightsail
* EBS
* Container registry
* Container service
* VPC
* Batch
* Lambda
* Autoscaling

Storage:
* S3
* EBS
* Elastic File System
* Glacier
* Storage Gateway
* Snowball
  * petabyte
  * edge petabyte (on-board compute)
  * exabyte

Database:
* Aurora (MySQL clone)
* RDS
* Dynamo (NoSQL)
* ElastiCache
* Redshift
* Database Migration Service
  
Migration:
* Database Migration Service
* RDS
* Dynamo
* ElastiCashe
* Redshift

Networking & Content Delivery:
* VPC
* CloudFront
* Route 53
* Direct Connect
* Elastic Load Balancing

Dev Tools:
* CodeDeploy
* Code Pipeline (Cont Del)
* Code Commit (Git Repos)
* X-Ray
* CLI
  
Management Tools:
* CloudWatch
* EC2 Systems Manager
* CloudFormation

Security, ID, and Compliance:
* Identity and Access Management
* Certificate Manager
* Inspector

AI:
* Lex
* Polly
* Rekognition
* Machine Learning

Mobile:
* Mobile hub
* API gateway
* Cognito
* Mobile SDK (software dev kit)

App Services:
* Step functions
* API Gateway
* Elastic Transcoder

Messaging:
* SQS
* SNS
* Pinpoint
* SES

Business Productivity:
* WorkDocs
* WorkMail

Desktop/App Streaming:
* WorkSpaces
* AppStream2.0

Internet of Things:
* Greengrass
* IoT Button
* Lumberyard (game dev service)

### Pricing Philosophy:

Lower infrastructure costs -> Reduced prices -> More customers -> More AWS Usage -> More Infrastructure -> Economies of Scale -> Lower Infrastructure Costs -> etc etc

---
## Monitoring and Alerting in AWS

Monitoring = continuous view of the health of services and infrastructure and apps. Necessary for providingtop quality services. Keeps track of service performance and historic monitoring data. Used to derive actionable intelligence and take action.

Monitoring alone may not be sufficient. Historical data = Reactive approach

Alerting is also needed so admins can be alerted about issues.

Eg: If EC2 instance is down, alerting can trigger deployment of new instance.

**What services can we use?:**

Most important = **CloudWatch.**

Monitors ekey metrics of services such as EC2, ELB, EBS.

SNS and SES are used for alerts. Simple Notification and Simple Email Services.

### What can we Monitor?

* AWS Resource Health
  * CPU Utilisation
* Billing
  * Alert if monthly bill exceeds budget
* Metrics
  * Logs

## CloudWatch Deep Dive

* Use cases
* Integration with other AWS services
* Features

**Use Cases:**
* Monitoring AWS Infrastructure
  * Just select the metrics you want for the resources you want.
* Monitoring applications and service via custom metrics
* Monitoring log files
  * aggregate from various sources into a single consolidated view
* Monitor and react to alarms


CloudWatch alarm states:
* OK
* Alarm
* Insufficient Data (just started, metric not available, not enough data for metric)

**Dashboards:** Used to monitor several metrics at once. Accessorisable. Can build multiple dashboards. Data can be pulled from multiple AWS services/regions to create global view.

### Creating Dashboard

In CloudWatch>Dashboard:
* Create Dashboard
* Name
* Select widgets to add.
* Search for metric to add.

### Creating Alarms
CloudWatch Dashboard:
* Alarms.
* You can view what metrics have reached which of the three states.
* Create Alarm
* Select Metric
* For max, select maximum and then interval.
* Name and description.
* Define Action.
  * Choose state
  * Choose notification topic.
  * Can add more notifications, as well as Autoscaling and EC2 Actions.

### Creating Custom Metrics

Need to create IAM first

Can use PERL scripts to get data for custom metrics from our EC2 Instances, and send that to CloudWatch.

You can select custom metrics once they are set up from your CloudWatch dashboard.

## RDS Monitoring

**Key metrics:**

* CPU utilisation
* Freeable memory
* Read IOPS/Write IOPS
* Database Connections
* Free Storage Space
* Read Latency/Write Latency

Monitor these closely:
* resource utilisation
* system errors
* accidental termination
* cluster health
* maintenance windows
* query logs
* rds metrics
* instance level metrics
* rds resource modification

## ELB Monitoring

**Key Metrics:**
* Backend connection errors
* Latency
* Surge queue length
* Spill over count
* HTTP responses
* Request count
* Healthy host count
* Unhealthy host count

## Billing and Costs Monitoring

PAYG Billing requires caution and close monitoring.

Monitoring billing can develop insights into usage.This can help us to optimise our cloud resource usage and costs.

Make sure you tick the options to receive billing alerts and reports.