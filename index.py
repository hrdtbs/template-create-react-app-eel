# coding: utf-8
import eel
import sys


@eel.expose
def hello():
    print('hello')


if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({
            'port': 3000
        }, options={
            'port': 8888,
            'host': 'localhost',
        })
    else:
        eel.init('build')
        eel.start('index.html')
