sample_dict ={
    "name": "prabha",
    "age":23,
    "salary":1000000,
    "city": "boyakonda"}


sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
