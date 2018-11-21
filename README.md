# pythonTutorial
A repo created to assist my brother in learning Python while he does a Udemy class. 

## First Steps 
1. Using GitBash, change directory into where you'd like to clone this repo. 
 - `cd homeEnvironment`
2. Now you need to clone the repo by typing the following:
 - `git clone https://github.com/mcole22266/pythonTutorial`
3. Now change directory into that directory
 - `cd pythonTutorial`
4. When you've finished create a file called `hello_yourname.py` and have it print 'Hello World'
 - if done successfully, you should be able to do and see the following:

```bash
$ python hello_yourname.py
Hello World

```
5. Now, tell git who you are:
 - git config --global user.email "you@example.com"
 - git config --global user.name "Your Name"
6. Lastly, push the file up by doing the following:
 - Add the file that you've made changes to to the staging area:
 	- `git add hello_yourname.py`
 - Commit your changes with an annotated message which can be used as reference in the 
 future:
 	- `git commit -m 'My first commit'`
 - When complete, push your changes up to the repo:
 	- `git push`

## Extension Help:
What you're currently reading was created by making a Markdown file. Markdown is a 
language that is essentially shorthand for writing html documents that is, unlike 
html, still readable in code form. For example, the first two paragraphs of this 
document actually looks like this in code form:

```markdown
# pythonTutorial
A repo created to assist my brother in learning Python while he does a Udemy class. 

## First Steps 
1. Using GitBash, change directory into where you'd like to clone this repo. 
 - `cd homeEnvironment`
2. Now you need to clone the repo by typing the following:
 - `git clone https://github.com/mcole22266/pythonTutorial`
3. Now change directory into that directory
 - `cd homeEnvironment`
4. When you've finished create a file called `hello_yourname.py` and have it print 'Hello World'
 - if done successfully, you should be able to do and see the following:
```

GitHub is designed in such a way that, if it sees a `README.md` file within a directory, it 
will compile it into a document - which is exactly how you're reading this. However, since 
you've cloned this repository onto your local machine, you'll want to be able to read 
easier than referencing my GitHub page each time. There are several Markdown Viewers you 
can find but I've found an extension in Google Chrome to be quite simple. To enable it, 
do the following:

1. Go to https://chrome.google.com/webstore/category/extensions
2. Type `Markdown Viewer` in the search bar
    - Likely the first one but ensure the author is `simov.github.io`
3. Add the Extension
4. After it is enabled, you should see an 'm' in your toolbar. 
    - Right click on the 'm' and click on 'Manage Extensions'
    - You should see "Allow access to file URLs" - select that box

You should be all set now! Since you've cloned this document onto your local machine, you 
can test it out by opening this `README.md` file using Google Chrome (it may ask which 
application you want to open markdown with). 
