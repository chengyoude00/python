def f():
    print 'call f()...'
    # ���庯��g:
    def g():
        print 'call g()...'
    # ���غ���g:
    return g
