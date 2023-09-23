#!/usr/bin/env python3


def create_actual_params(params):
    return '\\(\\"'+'\\",\\"'.join(map(str, params))+'\\"\\)' if params else '\\(\\)'


if __name__ == '__main__':
    amount = 1234.50
    ccy = 'EUR'
    id = 'werk  23 '
    inputParam = [amount, ccy, '', id]
    # inputParam = []
    print(create_actual_params(inputParam))