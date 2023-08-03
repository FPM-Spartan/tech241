# Linux Research Tasks

## Researching managing file ownership

Managing file ownership is important because it helps with security and accountability. Different users and groups can be assigned different ownerships and file permissions and this allows admins to monitor who has access and responsibility. This also prevents unauthorised access and modifications. Managing file ownership is also important for collaborative projects and shared access, as project members can be given the right permissions and ownership to be able to work on shared files.

The command to view ownership is "ls -l"

New files are automatically assigned 666 as permissions. This gives the user, the group, and others read write permissions. The ownership is set to the user who created it.

The owner's permissions are not X by default because it is good practice to adhere to the principle of least permissions. It is intended to prevent accidentally executing non-executable files. Execute permissions should be deliberately assigned.

This only applies to files. Execute permisson is automatically given for directories so that the user can actually navigate through folders.

The command for changing the owner is "chown"

## Researching managing file permissions

Being the owner of a file != having full permissions. As explained in the previous task, permissions are assigned separately to ownership, and following the principle of least permissions is good practice for a number of reasons.

If you give permissions to the User entity, it means that the user who owns the file or directory has the specified permissions, such as read, write, or execute, allowing them to access, modify, or execute the file.

If you give permissions to the Group entity, it means that all users who belong to the group associated with the file or directory have the specified permissions. This allows group members to access, modify, or execute the file based on their group membership.

If you give permissions to the Other entity, it means that all users who are neither the owner nor part of the group associated with the file or directory have the specified permissions. This allows other users to access, modify, or execute the file, irrespective of their ownership or group membership.

In the given example:

    User permissions are read-only, Group permissions are read and write, Other permissions are read, write and execute. You are logged in as the user which is owner of the file.

You would have read only permissions, because as the user, permissions are set to that.


    -rwxr-xr-- 1 tcboony staff  123 Nov 25 18:36 keeprunning.sh

-rwxr-xr--: This segment represents the file permissions. Breaking it down further:

* The first character (-) indicates that it is a regular file. If it were a directory, the first character would be d.
* The next three characters (rwx) represent the permissions for the owner (tcboony). The owner has read, write, and execute permissions.
* The following three characters (r-x) represent the permissions for the group (staff). The group has read and execute permissions.
* The final three characters (r--) represent the permissions for others. Others have only read permission.

## Researching managing file permissions using numeric values

The command takes the order of **owner**, *group*, **all users**.

The following numbers are used in Linux to change permissions:

0 = No Permission

1 = Execute

2 = Write

4 = Read

Assigning read + write permissions (read = 4, write = 2) would result in the numeric value of 6. This grants the ability to read and modify the file but does not allow execution.

To assign read, write, and execute permissions (read = 4, write = 2, execute = 1), the value would be 7. This provides full access to read, write, and execute the file or directory.

Assigning read and execute permissions (read = 4, execute = 1) would result in the value of 5. This allows the user to read the file and execute it as a program or script.

The mode/permissions representation 644 signifies that the owner has read and write permissions (6), the group has read permissions (4), and others have read permissions (4). This is a common permission setting for files, where the owner has full access, and group and others have read-only access.

Cheat sheet:

0 = --- ()

1 = --x

2 = -w-

3 = -wx

4 = r-

5 = r-x

6 = rw-

7 = rwx



## Researching changing file permissions
1. What command changes file permissions?      *chmod*
2. To change permissions on a file what must the end user be? (2 answers)       *current owner or superuser. In Linux, the superuser is the account with unrestricted access to all commands. it is also called root*
3. Give examples of some different ways/syntaxes to set permissions on a new file (named testfile.txt) to:

    a. Set User to read, Group to read + write + execute, and Other to read and write only. 

    b. Add execute permissions (to all entities)

    c. Take write permissions away from Group

    d. Use numeric values to give read + write access to User, read access to Group, and no access to Other.

#### Q3:

    a. chmod u=r,g=rwx,o=rw testfile.txt

    b. chmod +x testfile.txt

    c. chmod g-w testfile.txt

    d. chmod 640 testfile.txt

