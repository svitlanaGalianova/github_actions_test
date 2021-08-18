import os
secret = os.environ.get('SECRET_TEST')


def hello_world2():
    return secret
