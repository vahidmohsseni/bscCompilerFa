# Compiler-Project
Compiler Course Project Fall-2019
Thanks to AliReza Heydari


Compile with this Command : antlr4 -Dlanguage=Python2 Project.g4


## Install Antlr
source of installation is [https://github.com/antlr/antlr4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)
### UNIX

0. Install Java (version 1.6 or higher)
1. Download
```
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
```
Or just download in browser from website:
    [https://www.antlr.org/download.html](https://www.antlr.org/download.html)
and put it somewhere rational like `/usr/local/lib`.

2. Add `antlr-4.7.1-complete.jar` to your `CLASSPATH`:
```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
```
It's also a good idea to put this in your `.bash_profile` or whatever your startup script is.

3. Create aliases for the ANTLR Tool, and `TestRig`.
```
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
$ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

### Testing the installation

Either launch org.antlr.v4.Tool directly:

```
$ java org.antlr.v4.Tool
ANTLR Parser Generator Version 4.7.1
-o ___ specify output directory where all output is generated
-lib ___ specify location of .tokens files
...
```

or use -jar option on java:

```
$ java -jar /usr/local/lib/antlr-4.7.1-complete.jar
ANTLR Parser Generator Version 4.7.1
-o ___ specify output directory where all output is generated
-lib ___ specify location of .tokens files
...
```


# Deployment

## generate Lexer and Parser
NOTE: this step is optional!
After installing `antlr4` you should generate lexer and parser codes using `antlr4`.
Use the following command:
```$ antlr4 -Dlanguage=Python2 MiniJava.g4```


## install project requirements
to install the requirements of project use following command:
```pip install -r requirements.txt```

## run
```python Project.py```

in browser:
type address `http://localhost:5000` and upload a file to compile.
