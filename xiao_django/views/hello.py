#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: pacman
@time: 2017/11/23 17:10
"""

from django.http import HttpResponse

def say_sth(request):
    return HttpResponse('good! good! good!')

def main():
    print('do sth')


if __name__ == '__main__':
    main()