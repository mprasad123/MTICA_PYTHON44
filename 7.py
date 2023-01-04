employees = ['manu', 'prasad', 'manasa']
defaults= {"designation":  'Developer', "salary": 80000}

data =dict.fromkeys(employees, defaults)
print(data)

print(data["manasa"])
