# Script Name        : fileinfo.py
# Author                 : Not sure where I got this form
# Created                : 28th November 2011
# Last Modified      : 
# Version                : 1.0
# Modifications      :

# Description            : Show file information for a given file

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
score = int(raw_input('输入分数:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
 
print '%d 属于 %s' % (score,grade)