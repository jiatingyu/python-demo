#!/usr/bin/env python3   #让这个文件可以直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-  #文件编码设置

'这是一段注释'

def greet(name):
    return f"Hello, {name}!"


PI = 3.14159

__name = 'ziyu'

age = 30

def __getname():
    return __name


def area(radius):
    return PI * radius ** 2

__all__ = ['greet', 'PI','age']