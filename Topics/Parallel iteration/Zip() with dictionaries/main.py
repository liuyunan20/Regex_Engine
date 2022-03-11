# please do not modify the following code
_d_list = [keyword.split(':') for keyword in input().split(', ')]
domestic_animal = {key: value for key, value in _d_list}
_w_list = [keyword.split(':') for keyword in input().split(', ')]
wild_animal = {key: value for key, value in _w_list}

# your code here
zipped = zip(domestic_animal.items(), wild_animal.items())
for (d_key, d_value), (w_key, w_value) in zipped:
    print(f"The domestic animal's {d_key} is '{d_value}'.")
    print(f"The wild animal's {w_key} is '{w_value}'.")
