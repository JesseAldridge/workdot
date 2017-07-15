
Workdot monitors a directory full of text files and renders them with graphviz whenever they change.

Requires Graphviz:  http://www.graphviz.org/Download..php

```
cd ~ 
git clone git@github.com:JesseAldridge/workdot.git
cd workdot
ln -s ~/workdot/workdot.py /usr/local/bin/workdot
mkdir ~/my_test_workdots
cd ~/my_test_workdots
echo "- test 1\n  - test 2\n- foo*\n" > test1.txt
echo "- another file" > test2.txt
open ~/my_test_workdots
workdot ~/my_test_workdots
```

Edit the text files in `~/my_test_workdots` and see what happens.
