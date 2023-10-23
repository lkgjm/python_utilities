#!/usr/bin/env python3
""" parse parameters"""


def create_actual_params(params):
    """ return parameters with forward slashes"""
    return '\\(\\"'+'\\",\\"'.join(map(str, params))+'\\"\\)' if params else '\\(\\)'
