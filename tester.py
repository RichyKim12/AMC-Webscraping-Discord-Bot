

    

hashmap = {'USD': [('CAD', 1.3), ('GBP', 0.71), ('JPY', 109.0)], 'GBP': [('JPY', 155.0)]}
def dfs(country, target,val, val_list):
    if country == target:
        return val
    adj_list = hashmap.get(country,None)
    if adj_list:
        for tuple in adj_list:
            country, conversion = tuple[0], tuple[1]
            if country == target:
                val_list.append(val*conversion)
                continue
                
            else:
                dfs(country,target, val*conversion, val_list)
    return val_list
            
max_val = -1
target = 'JPY'
for tuple in hashmap['USD']:
    country, val = tuple[0], tuple[1]
    array = dfs(country, target, val, [])
    print(array)
    

list = [1,2,3,4]
print(list[-1])
