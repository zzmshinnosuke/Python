#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on 2021-12-30 16:15:13
# @Author: zzm


def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
