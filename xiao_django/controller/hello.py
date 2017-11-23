#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: pacman
@time: 2017/11/23 17:10
"""

from django.http import HttpResponse
from django.shortcuts import render


def say_sth(request):
    context = {}
    context['hello'] = 'good again with template'
    return render(request, 'hello.html', context)


def say_sth1(request):
    return HttpResponse('good! good! good!')


def main():
    print('do sth')


if __name__ == '__main__':
    main()
