![pysh](http://www.forhadahmed.net/github/pysh-logo.png)

Python pre-processor for inline bash commands

* bash is great for system scripting! 
* python is great for programming ease!

**pysh** is an attempt to combine the two for convenience  

Bash offers a shorthand way of getting output from commands (using backticks):
    
    $FILES=`ls -al`

pysh is a preprocessor for allowing similar inline bash commands in python:

    files=`ls -al`
    print "Number of files: %d" % len(files.split())
    
This is purely for convenience - it replaces commands inside backticks with
`os.popen(...).read()` and `exec()`'s the resultant code.  The results
can be stored in a python variable.
