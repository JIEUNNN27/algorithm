# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
t = int(input())
lst31 = ["01", "03", "05", "07", "08", "10", "12"]
lst30 = ["04", "06", "09", "11"]
for i in range(t):
    data = input()
    m = data[4:6]
    d = int(data[6:])
    if m == "02" and d<=28:
        print(f"#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}")
    elif m in lst31 and d<=31:
        print(f"#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}")
    elif m in lst30 and d<30:
        print(f"#{i+1} {data[:4]}/{data[4:6]}/{data[6:]}")
    else:
        print(f"#{i+1} -1")