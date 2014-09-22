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
    
if "Hello.py" in files:
    print "Hello!"
else:
   `touch Hello.py`
```    
Much like Perl backticks! This is purely for convenience - it replaces bash commands inside backticks with
`os.popen(...).read()` and `exec()`'s the resultant code.  The output of bash 
commands can be stored in python and manipulated by all of python's magic!

#### Installation / Usage

* Place `psh` in /usr/bin
* Run your python scripts with embedded bash commands:
  * `psh myscript`
  * Add `#!/usr/bin/psh` to any script and run it directly: `./myscript`


#### Notes

* Only fixed bash commands can be executed - cannot use python variables inside bash commands (TODO)
* Don't use backticks for nesting commands - use `$()`
* Bash commands in backticks can span multiple lines
* Each bash command executes in its own shell (variables assignments within bash are not persistent)
* *Needs more testing* !
