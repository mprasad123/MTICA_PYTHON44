def calulateCubic():
    i  =1;
    while True:
        yield  i*i*i
        i +=1


for num in  calulateCubic():
    if num > 10000:
        break
    print(num)
