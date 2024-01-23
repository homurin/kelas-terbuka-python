distro = {
    'name': 'Arch Linux',
    'package_manager': 'pacman',
    'based_on': 'independen',
    'release_cycle': 'rolling'
}

# shallow copy a dictionary

ubuntu = distro.copy()

# this is will not affected distro

ubuntu.update({'name': 'ubuntu'})
ubuntu.update({'package_manager': 'apt'})
ubuntu.update({'based_on': 'debian'})
ubuntu.update({'release_cycle': 'LTS'})

# pop get and remove data from dict based on dict key

distro.update({'category': ['desktop']})

# now category is removed from distro dict
# category will stored in category variable

category = distro.pop('category')
print(category)

# popitem is same as pop() but will get from last key

release_cycle = ubuntu.popitem()

# new release_cycle is removed and stored at release_cycle

print(release_cycle)

print(distro)
print(ubuntu)
