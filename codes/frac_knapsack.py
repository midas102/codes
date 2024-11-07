def frac():
    weights = list(map(int,input("enter the weights:").split()))
    values = list(map(int,input("enter the values:").split()))
    capacity = int(input("enter the capacity:"))
    res = 0
    if len(weights) != len(values):
        print("error")
        return 
    for pair in sorted(zip(weights,values),key = lambda x:x[1]/x[0], reverse = True):
        if capacity <=0:
            break
        if pair[0]>capacity:
            res += int(capacity *(pair[1]/pair[0]))
            capacity = 0
        elif pair[0]<=capacity:
            res += pair[1]
            capacity -=pair[0]
    print(f"the value is :{res}")
if __name__ == "__main__":
    frac()
