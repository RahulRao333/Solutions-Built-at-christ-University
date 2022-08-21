def words_split():
    
    sen=input("Enter the sentence")
    l=[]
    for i in range(len(sen)):
        if sen[i].isdigit()==True:
            l.append(sen[i])
    
    l1=list(sen)
    
    string=""
    for i in range(len(l1)):
        if l1[i].isdigit()==False:
            string=string+l1[i]
    data=string.split(" ")
    
    d=dict()
    for i in range(len(l)):
        d.update({l[i]:data[i]})
    d=sorted(d.items(),key=lambda x:x[0])
    j=1
    for i in range(len(d)):
        print(d[i][j],end=" ")

       


words_split()
