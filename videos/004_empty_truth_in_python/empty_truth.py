def do_something(options=None):
    if not options:
        options = {'option1': 1}
    print(options)


if __name__ == '__main__':
    x = iter([])

    do_something(options={})
