# pythonTutorial
A repo created to assist my brother in learning Python while he does a Udemy class. 

## First Steps 
1. Using GitBash, change directory into where you'd like to clone this repo. 
 - `cd homeEnvironment`
2. Now you need to clone the repo by typing the following:
 - `git clone https://github.com/mcole22266/pythonTutorial`
3. Now change directory into that directory
 - `cd homeEnvironment`
4. When you've finished create a file called `hello.py` and have it print 'Hello World'
 - if done successfully, you should be able to do and see the following:

```bash
$ python hello.py
hello world

```
5. Now, tell git who you are:
 - git config --global user.email "you@example.com"
 - git config --global user.name "Your Name"
6. Lastly, push the file up by doing the following:
 - Add the file that you've made changes to to the staging area:
 	- `git add hello.py`
 - Commit your changes with an anotated message:
 	- `git commit -m 'My first commit'`
 - When complete, push your changes up to the repo:
 	- `git push`
