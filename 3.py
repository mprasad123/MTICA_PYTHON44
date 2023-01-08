import sys

print("Coming through stdout")

save_stdout = sys.stdout
fo =open(r"C:\Users\User\Desktop\pythonpractice\day9\abc1.txt", "w")
sys.stdout=fo
print("this line goes to abc1.txt")
print(input())
sys.stdout = save_stdout
fo.close()
