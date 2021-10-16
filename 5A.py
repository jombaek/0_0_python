class Hello_world:
    def __init__(self):
        self.message = 'Hello world!'

    def get_hello_world(self):
        return self.message

    def set_new_hello_world(self, new_hello_world):
        self.message = new_hello_world

hello = Hello_world()
print(hello.get_hello_world())

hello.set_new_hello_world('zbc')
print(hello.get_hello_world())

hello.set_new_hello_world('Python')
print(hello.get_hello_world())
