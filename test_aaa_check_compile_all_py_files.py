import os


def test():

    files = os.listdir('.')
    for f in files:
        if f.endswith(".py"):
            print("TEST compile:", f)
            cmd = '''python -c "import ast; ast.parse(open('%s').read())"''' % f
            ret = os.system(cmd)
            assert ret == 0
    
    
if __name__ == '__main__':
    test()
