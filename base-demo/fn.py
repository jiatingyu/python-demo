# def log():
#     print('日记记录。。。')
#
#
# def hello(world):
#     print('hello' + world)
#
#
# def exec():
#     log()
#     hello('world')
#
# exec()
#
def log(fn):
    def wrapper(world):
        print('日记记录。。。')
        return fn(world)
    return wrapper
@log
def hello(world):
    print('hello' + world)


hello('world!!')


