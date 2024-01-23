laptops = {
    'laptop_name': ['Lenovo v14-ADA', 'Lenovo Legion 5', 'Advan Workplus', 'Acer Aspire 5', 'Asus ROG 5'],
    'cpu_name': ['Amd Ryzen 3-3600', 'Amd Ryzen 5-7200', 'Amd Ryzen 5-7200', 'Intel i5-3800', 'Amd a9']
}

cpus = {
    'cpu_name': ['Amd Ryzen 3-3600', 'Amd Ryzen 5-7200', 'Intel i5-3800', 'Amd a9'],
    'cpu_score': [3600, 7200, 3800, 2100]
}

laptops['cpu_score'] = []

# gw

for index in range(0, len(laptops['cpu_name'])):
    for index_cpu in range(0, len(cpus['cpu_score'])):
        if (laptops['cpu_name'][index] == cpus['cpu_name'][index_cpu]):
            laptops['cpu_score'].append(cpus['cpu_score'][index_cpu])

print(laptops['cpu_score'])

# gpt

laptops['cpu_score'] = [cpus['cpu_score']
                        [cpus['cpu_name'].index(cpu)] for cpu in laptops['cpu_name']]

print(laptops['cpu_score'])

# bing

cpu_score_lookup = dict(zip(cpus['cpu_name'], cpus['cpu_score']))
print(cpu_score_lookup)

laptops['cpu_score'] = [cpu_score_lookup[name] for name in laptops['cpu_name']]
print(laptops['cpu_score'])
print([cpus['cpu_score'][cpus['cpu_name'].index('Amd Ryzen 3-3600')]])
