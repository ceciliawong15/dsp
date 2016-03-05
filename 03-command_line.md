# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pwd - print working directory
    mkdir - make a new directory ie folder
    exit - exit the shell
    cd - change directory to folder within your current location 
    ls - list folders inside of current folder
    cd /folder/folder - moves you into folders within your current folders
    cd ../ - moves your path one folder ahead
    rmdir - removes a directory given that you are one path above the one you are trying to remove
    pushd - allows you to set a path in memory so that you can return any portion of it later without following a linear fashion
    popd - allows you to move back to your xx original position before your last pushd no matter how far away your cd is from there
    touch filenamehere - allows you to create an empty file in whichever directory you are currently in
    cp file1 file2 - makes a copy of file1, named file2 
    cp file1 /directory1 - makes a copy of a file in a different specified directory
    cp -r folder1 folder 2 - NOT SURE WHAT THIS DOES AS OF CURRENT. I think it copies your most recently created file from             given folder1 into folder2.
    mv oldname newname - move or rather renames file from oldname to newname
    less filename - allows you to see the contents of a file within terminal window. 
            pressing q allows you to quit out of this view.
    cat filename - allows you to see contents of a file within your current terminal window, instead of appearing in a new             one where you would have to do q to X out of it. ie, "streaming a file."
    rm - removes a file from your current directory or can specify a directory and file
    $|$ - takes output from command on left side and pipes it to command on the right 
    $<$ - take and send input from file on right side to the program on the left
    $>$ - take and set input from file on left side to the program on the right
    $>>$ - the >> takes output of the command on the left and appends it to the file on the right
    
    *ctrl-c clears/abandons your current line of code..
    *need to figure out how to grant myself permission to copy a file into an already existing folder(ex21)
    *what's -r and -rf for rm function? 
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


---

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

