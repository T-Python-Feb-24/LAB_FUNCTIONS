string="Hey"
string2=":)"
string3="Pls"

def strings(x:str):

 for i in range(5, 0, -1): # 
    for m in range(i,0,-1 ):
        print(x,end=' ')
    print('\r')
    

strings(string)
strings(string2)
strings(string3)