# Notes on Scripting

A script is a piece of code that automates a task.
The main benefits are: save time, eliminate human error.

Scripting is different to programming in many ways:

* Scripts are done in ONE FILE. Programmes can be huge projects with many files and folders.
* Similarly, scripting has a limited scope. It is targeted  on a limited task or action. Programming typically has a much more comprehensive scope.
  *     Photoshop analogy: Scripting would be a better way of resizing thousands of photos compared with manually doing each one in photoshop. It saves time and elminates human error.
* Scripts are (or should be) easy to read, whereas a program can get VERY complex!
* Scripts are very rigid/specific. Programmes, given their complexity, are flexible.
* Scripts are written in high level language. Programmes can be written in high or low level languages.
  * (**NB**: program languages are on a high - low spectrum. The lower a language, the closer to machine code it is. The higher, the closer to human writing it is.)

### Why use python for scripts?

Firstly, Python is **EASY** to use, and as a high level language, it makes creating scripts much more simplified.

Second, Python is the largest language in the world. It has a vast amount of **LIBRARIES** that scripters can download, import, and make use of.

    * __a library is a collection of modules, which are a collection of functions__

Third, and simnilar to the last one, python has a **LARGE COMMUNITY** of users who can contribute libraries for people to download. These libraries are FREE because Python is **OPEN SOURCE**. This also means that a lot of the code we might need as DevOps engineers is likely already out there! DevOps aren't as focussed on creating lots of code, we can often times just take existing code and tweak to fit our needs.

Finally, Python is good for scripting because of it's **LANGUAGE INTEROPERABILITY**. This means that it works well with other languages, and across multiple platforms and systems.


### Scripting and DevOps

We do a LOT of automation. WE make the release of software as efficient as possible.
Configuration (especially with the Cloud). ->IaC -> config management, orchestration (more on those later)

Here are just some examples of way we use scripts in DevOps:

* Python script to query a database 
* Python script to execute a shell command or script 
* Query logs for alerts 
* Python script to take a backup 
* Python script for K8 containers 
* Python script to fetch I.P's of an autoscaling group 
* Lambda function to stop instances on a weekend 
* Python script for ETL jobs 
* Find the expiry date of an SSL certificate 
* Develop CLI applications using Python 
* Automating CRUD 
* Custom scripts for config management

### Core Python Modules

There are **SEVEN** core modules in Python.

1. sys (system)
2. os (operating system)
   1. good for working with files and folders
3. subprocess
   1. lets the working file interact with other files. Runs an external file when executed. Directory can be specified if not in same directory.
4. math (lets us do cool maths stuff)
5. random (lets us do stuff with RNG)
6. json (**SUPER USEFUL**) 
   1. lets us interact with json, which is a high level language that interacts with APIs and other languages.
7. datetime (**SUPER USEFUL**)
    1. work with date and time

## Parse JSON

JSON is a high level human readable language. It is mostly used to transport data.

Stands for JavaScript Object Notation.

Notation (how its written) objects (key value pairs) uses JavaScript as its skeleton.

example use: when a server is sending data to a webpage.

As DevOps engineers, we should know how to automate a lot of JSON repetitive tasks since we will encounter it a lot.

JSON works with key value pairs, like python dictionaries do.

JSON written with curly brackets, but you don't need to assign a name like you do with python dictionaries.

```json
{
  "name": "test",
  "ip": "192.168.23.45",
  "project": "DevOps",
  "website": "spartaglobal.com"
}
```
### What is parsing?

Parsing is turning a string into a data structure and vice verse.

It's a good idea to create a script to parse for us as it's quite a repetitive task with lots of room for human error.

-- INSERT CODE FROM parse json and parse remote json--

--insert check json code--

-- Insert some code from yaml to json--