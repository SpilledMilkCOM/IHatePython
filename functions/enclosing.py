message = 'global'

def enclosing():
    message = 'enclosing'


    def local():
        # global message
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

def main():
    print('global message:', message)
    enclosing()
    print('global message:', message)

if __name__ == "__main__":
    main()
