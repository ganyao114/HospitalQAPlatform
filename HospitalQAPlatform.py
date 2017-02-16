from flask import Flask

from app import creat_app


if __name__ == '__main__':
    creat_app('development').run()
