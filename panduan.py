#! /usr/bin/env python3
# -*- coding:utf-8 -*-

height=input('请输入身高，以米为单位：')
weight=input('请输入体重，以千克为单位：')

BMI=float(weight)/float(height)**2

print('您的BMI值为：%.2f'%BMI)
print('您的体重：')
if BMI<18.5:
    print('过轻')
elif BMI>=18.5 and BMI<25:
	print('正常')
elif BMI>=25 and BMI<28:
	print('过重')
elif BMI>=28 and BMI<32:
	print('肥胖')
else:
	print('严重肥胖')