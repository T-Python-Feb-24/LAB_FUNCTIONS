
def string(x):
    string=""
    for i in range(x,0,-1):
        for m in range(i,0,-1):
            string +=f"{str(i-m)}" 
        string += "\n"
    return string
        
result=string(5)
print(result)