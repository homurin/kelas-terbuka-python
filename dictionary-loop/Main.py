laptops = {
    'cpu_name': 'amd ryzen 3 3200U',
    'gpu_name': 'radeon vega 3',
    'ram': 8,
    'disk_storage': 512
}

print('get dict value from keys:')

for key in laptops.keys():
    print(laptops.get(key))

print('get dict value from values')

for laptop in laptops.values():
    print(laptop)

print('get dict key and laptop using items')

for key, laptop in laptops.items():
    print(f'{key} : {laptop}')
