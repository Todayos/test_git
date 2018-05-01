# encoding:utf-8
def have_arg(arg):
    def func(pre_func):
        def func_inner():
            if arg == 'good':
                print("出去玩")
            if arg == "bad":
                print("不出去玩")
            return pre_func()

        return func_inner

    return func


@have_arg('good')
def func1():
    print('天气好')


@have_arg('bad')
def func2():
    print("天气不好")


func1()
func2()
