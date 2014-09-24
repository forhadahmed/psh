![psh](http://www.forhadahmed.net/github/psh-logo.png)

Python pre-processor for inline bash commands

* bash is great for system scripting! 
* python is great for programming ease!

**psh** is an attempt to combine the two...

-

Bash offers a shorthand way of getting output from commands (using backticks):
```bash    
#!/usr/bin/bash

FILES=`ls -al`
```
However, doing any processing on that output in bash is hugely cumbersome...
`psh` is a preprocessor for allowing similar inline bash commands in python:
```python
#!/usr/bin/psh
    
files = `ls -al`
    
if "Hello.txt" in files:
    print `cat Hello.txt`
else:
   `echo "Hello, World!" > Hello.txt`
```    
Much like Perl backticks! This is purely for convenience - it replaces bash commands inside backticks with
`os.popen(...).read()` and `exec()`'s the resultant code.  The output of bash 
commands can be stored in python and manipulated by all of python's magic!

#### Python variables bash commands

* `psh` allows for executing dynamic bash commands with python variables in them
* Use `${}` to embed python variables: [give a good example]

#### Installation / Usage

* Place `psh` in /usr/bin
* Run your python scripts with embedded bash commands:
  * `psh myscript`
  * Add `#!/usr/bin/psh` to any script and run it directly: `./myscript`

#### Notes

* Can't use `import` to import psh files
* Don't use backticks for nesting bash commands - use `$()`
* Bash commands in backticks can span multiple lines
* Each bash command executes in its own shell (variables assignments within bash are not persistent)
* *Needs more testing* !
