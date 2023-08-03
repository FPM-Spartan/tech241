# Notes on GIT - Week 2 Tuesday

## Version control

Version control is a system that allows the tracking of changes made to a project.
Version control as a concept has been around for a long time, as it simply refers to the process of controlling changes made to something.

With electronic files, it is possible to manually control versions by copying files into differnt folders, but this is a pain.
It is also largely impractical to manage with big projects, and impossible if multiple people are working on the same project.

This is where Version Control Systems (VCS) come in. These allow the computer to keep track of the changes made.

Version databases, the traditional model of VCS, are largely inefficient, because when changes are made to a project, everything is saved again.
In effect, this means unchanged files are needlessly duplicated. With large projects and large file sizes, this can eat through resources, memory, storage space etc very quickly.

This can be demonstrated in Diagram 01.

##### Diagram 01
![diagram showing old version control](/images/oldvcs.png)

This is where GIT comes in. In GIT, files in a project that are not changed for a new version are not saved again. They remain the same.
Git is incremental and iterative, like Agile.

Diagram 02 shows how Git controls versions.

##### Diagram 02
![Diagram showing Git](/images/gitvcs.png)

Each new version created by Git is called a Snapshot.

Git language for a snapshot is called a **Commit**.




git init

git status

git add .

git commit -m ""