# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
* pwd: show current working directory path
* mkdir: creating a directory
* rmdir: deleting a directory
* touch –a file: creating a file using `touch` command
* rm Filename: deleting a file
* mv filename1.ext filename2.ext renaming a file
* ls -a: listing hidden files
* cp [file] [dir]: copying a file from one directory to another

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
* ls:	Short listing
* ls -l:	Long listing
* ls -a:	Listing including hidden files
* ls -lh	:Long listing with Human readable file sizes
* ls -lah: Displays long list, including hidden files with a human readable file size
* ls -t	Displays newest files first (based on timestamp)
* ls -Glp: Displays a long list, excluding groupd names and including directories with /  
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
* -r	Displays files in reverse order.
* -R	Displays subdirectories as well.
* -t	Displays newest files first. (based on timestamp)
* -u	Displays files by the file access time.
* -x	Displays files as rows across the screen.
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
Xargs is used when the output of a command is expected to be one or more space/newline seperated results. This is useful in several cases, particularly in order to avoid *Argument list too long* errors.
 

