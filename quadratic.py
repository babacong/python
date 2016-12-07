#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        raise TypeError('a,b,c只能是数字')  
    elif a==0:
        raise TypeError('a不能为0')
    elif b**2-4*a*c<0:
        raise TypeError('b^2-4ac小于零，无解') 
    else:
        return (-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)   	