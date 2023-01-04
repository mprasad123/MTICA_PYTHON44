sample_dict ={
    "name": "prabha",
    "age":23,
    "salary":1000000,
    "city": "boyakonda"}
keys = ["name", "salary"]

##
##newDict={}
##for i in keys:
##     newDict=sample_dict[i]
##print(newDict)
##
##
##newDict={  i:sample_dict[i]  for i in keys   }
##print(newDict)
      
res = dict()
for k in keys:
    res.update({k : sample_dict[k]})
print(res)
