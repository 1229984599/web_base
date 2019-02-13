from contextlib import contextmanager


@contextmanager
def te():
    print('aaa')
    yield


def check_recipients(recipient):
    if not isinstance(recipient, list):
        return list(recipient)
    return recipient

a = '342535'
print(check_recipients(a))
