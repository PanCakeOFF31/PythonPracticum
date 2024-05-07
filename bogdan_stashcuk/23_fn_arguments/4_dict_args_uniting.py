def get_posts_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs.get(144))
    print(kwargs.get('weight'))


big_string = ("asdas naklvsnljksanldk v"
              "asknslajkdvnkljsavnlksjd nsvdkjva"
              )
print(big_string)

get_posts_info(weight=144, height=45, gender="White human")


def combining(*args, age, **kwargs):
    print(args)
    print(kwargs)
    print(age)


combining(10, 20, name='maxim', age=100, weight=300)


def combining_other(age, *args, **kwargs):
    print(args)
    print(kwargs)
    print(age)


combining_other(10, 20, name='maxim', weight=300)

# def reversed_combining(**kwargs, *args):
#     print(args)
#     print(kwargs)
