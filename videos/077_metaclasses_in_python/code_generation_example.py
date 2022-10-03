def _make_init(annotations):
    lines = [
        'def __init__(self, {}):'.format(
            ', '.join(f'{arg}: {annot.__qualname__}'
                      for arg, annot in annotations.items())),
    ]

    for arg, annot in annotations.items():
        lines += [
            f'   self.{arg} = {arg}',
        ]

    return '\n'.join(lines)


class DataClassMeta(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        if annotations := namespace.get('__annotations__'):
            init_code = _make_init(annotations)
            exec(init_code, globals(), namespace)
        return super().__new__(cls, name, bases, namespace, **kwargs)


class DataClass(metaclass=DataClassMeta):
    pass


class MyFields(DataClass):
    x: int
    y: str


def main():
    print(MyFields.__annotations__)
    print(_make_init({'x': int, 'y': str}))
    # print(help(MyFields))
    m = MyFields(2, 3)


if __name__ == '__main__':
    main()
