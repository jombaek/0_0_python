public_props = (name for name in dir(str()) if not name.startswith('_'))
private_props = (name for name in dir(str()) if name.startswith('_'))

for name in public_props:
    print(name)

for name in private_props:
    print(name)
