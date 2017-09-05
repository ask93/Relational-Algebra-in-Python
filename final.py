dic={'clas':'class.txt','marks':'marks.txt','tasm':'wtevr'}
l=1
schema={'clas':['rollno','name','surname','dob','mob','yob','street','city','state'],'marks':['rollno','subject','date','month','marks']}
it=''      
def run():
    flag=1
    while flag==1:
        a=raw_input('Enter your relational algebra expression\n')
        seperate(a)
        global it
        print 'The new table name is ',it
        global dic
        global schema
        table=read2(dic[it])
        for i in table:
            if i==[]:
                break
            s=''
            for j in i:
                s=s+'  '
                s=s+j
            print s
                
        

        print 'press 0 to quit and 1 to continue'
        q=input()
        if q==0:
            flag=0
            break
        run()
    raw_input()


def read(a1):
    import csv
    #a='ak1.txt'
    #a=s2[0]
    a=a1
    s = list(csv.reader(open(a, 'rb'), delimiter='\t'))
    table1=[[],[],[]]
    #print s
    #print len(s),len(s[0])
    for i in range(100):
        table1.append([])
    #print s
    j=0
    k=0
    for i in range(len(s[0])):
        for j in range(len(s)):
            #print len(s[j])
            #print j,i,s[j][i]
            #print i,j
            if s[j]==[]:
                break
            #print j,i,s[j][i]
        
            table1[i].append(s[j][i])
            if k!=0 and k==j+1:
                break
            
            if j<len(s):
                if s[j+1][i]=='':
                    k=j+1
                    break
            
    #print table1
    return table1

def read2(a1):
    import csv
    #a='ak1.txt'
    #a=s2[0]
    a=a1
    s = list(csv.reader(open(a, 'rb'), delimiter='\t'))
    table1=[[],[],[]]
    #print s
    #print len(s),len(s[0])
    for i in range(100):
        table1.append([])
    #print s
    return s


    
def write(o,a):
    j=0
    lol=[[],[],[],[],[]]
    import csv
    with open(a, 'w') as f:
    
        w = csv.writer(f, dialect = 'excel-tab')
        w.writerows(o)


#a='select ((a!=wwwd) or (a!=fjgkfj and b=sdjso and gg!=ujkh) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
def get(a):
    if "project" in a:
        pro(a)
    elif "naturaljoin" in a:
        nat(a)
    elif "aggregate" in a:
        agg(a)
    elif " join " in a:
        differentiate2(a)
    elif "union" in a:
        union(a)
    elif "intersection" in a:
        inter(a)
    elif "minus" in a:
        minus(a)
    else:
        differentiate(a)

def nat(a):
    #print a
    flag=0
    for i in range(len(a)):
        
        if a[i]=='[':
            
            
            flag=0
            for j in range(i+1,len(a)):
                
                if a[j]==']':
                    flag=1
                    
                    break
            if flag==1:
                
                v=[]
                v=a[i+1:j].split(',')
                global dic
                global schema
                help(dic[v[0]],dic[v[1]],schema[v[0]],schema[v[1]])
                break


def differentiate(a):
    c=0
    f=1
    for i in range(len(a)):
        if a[i]=='(':
            f=1
            for j in range(i+1,len(a[i+1:])):
                if a[j]=='(':
                    f=1
                    break
                    
                elif a[j]==')':
                    f=0
                    break
                    
            if f==0:
                if " and " in a[i:j]:
                    #print 'orand'
                    c=1
                    orand(a)
                    break
                elif " or " in a[i:j]:
                    #print 'andor'
                    c=1
                    andor(a)
                    break
                else:
                    f=1
    if c==0:
        orand(a)
        
           


def orand(a):
    #a='select ((a!=wwwd) or (a!=fjgkfj and b=sdjso and gg!=ujkh) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    #a='select ((a=wwwd) or (a=fjgkfj) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    tab=''
    tab=tabname(a)
    #print a
    #print a,'tab     :',tab
    b=a.split(" or ")
    #print b
    h=[]
    h1=[]
    for m in range(len(b)):
        for i in range(len(b[m])):
            if b[m][i]=="(":
                k=0
                for j in range(i+1,len(b[m])):
                    if b[m][j]=="(":
                        k=1
                    if b[m][j]==")" and k==0:
                        k=1
                        if " and " in b[m][i:j]:
                           # print b[m][i:j]
                            h.append(b[m][i+1:j])
                        else:
                           # print b[m][i+1:j-1] 
                            h1.append(b[m][i+1:j])

    """o=""
    for i in range(len(a)-1):
        if a[i]=="[":
            st=i
            for j in range(i+1,len(a)):
                if a[j]=="]":
                    en=j
                    o=a[i+1:j]

    print o"""





    #print "h:  "
    #print h
    #print "h1:  "
    #print h1
    orlist=[]
    w=[]
    count=0
    count1=0
    for i in h1:
        if "!=" in i:
            orlist.append(i.split("!="))
            orlist[count].append(1)
            count=count+1
        elif "<=" in i:
            orlist.append(i.split("<="))
            orlist[count].append(2)
            count=count+1
        elif ">=" in i:
            orlist.append(i.split(">="))
            orlist[count].append(3)
            count=count+1
        elif "<" in i:
            orlist.append(i.split("<"))
            orlist[count].append(4)
            count=count+1
        elif ">" in i:
            orlist.append(i.split(">"))
            orlist[count].append(5)
            count=count+1



        else:
            orlist.append(i.split("="))
            orlist[count].append(0)
            count=count+1
    #print "orlist:   "
    #print orlist
    for i in range(len(h)):
        w.append(h[i].split(" and "))
    #print "w  :"  
    #print w
    andlist=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(w)):
        count1=0
        for j in range(len(w[i])):
            if "!=" in w[i][j]:
                andlist[i].append(w[i][j].split("!="))
                andlist[i][count1].append(1)
                count1=count1+1
            elif "<=" in w[i][j]:
                andlist[i].append(w[i][j].split("<="))
                andlist[i][count1].append(2)
                count1=count1+1
            elif ">=" in w[i][j]:
                andlist[i].append(w[i][j].split(">="))
                andlist[i][count1].append(3)
                count1=count1+1
            elif "<" in w[i][j]:
                andlist[i].append(w[i][j].split("<"))
                andlist[i][count1].append(4)
                count1=count1+1
            elif ">" in w[i][j]:
                andlist[i].append(w[i][j].split(">"))
                andlist[i][count1].append(5)
                count1=count1+1
            
            else:
                andlist[i].append(w[i][j].split("="))
                andlist[i][count1].append(0)
                count1=count1+1
    #print "andlist:    "
    #print andlist
    fname=''
    #student=[['avinash','appu','sourabh','dilip'],['8050594923','8971408649','8998987898','8967563432'],['udupi','kota','udupi','karkala']]
    #for i in s:
    #    if i==tab:
    #        fname=s[i]
    
    fname=dic[tab]        
    student=read(fname)
    ##print student
    #student=table1
    #print student
    #global clas
    stu=schema[tab]
    #stu=["name","phone","city"]
    orrand(student,orlist,stu,andlist)


def orrand(s=[[]],o=[[]],st=[],a=[[[]]]):
    student=s
    andlist=a
    stu=st
    orlist=o
    col=[]
    val=[]
    sn=[]
    result=[[],[],[],[]]
    for i in range(50):
        result.append([])

    p=0
    if orlist!=[]:
        for i in orlist:
            col.append(stu.index((i[0])))
            sn.append(i[2])
            val.append(i[1])
    ##print col
    ##print sn
    ##print val

    col1=[[],[],[],[],[]]
    val1=[[],[],[],[],[]]
    sn1=[[],[],[],[],[]]

    """for i in range(len(andlist)):
        for j in range(len(i)):
            for k in range(len(k)):
    """
    for i in andlist:
        if i!=[[]]:
            for j in i:
                col1[andlist.index(i)].append(stu.index(j[0]))
                val1[andlist.index(i)].append(j[1])
                sn1[andlist.index(i)].append(j[2])

    #print 'col',col1
    #print 'val',val1
    #print 'sign',sn1

    for i in range(len(student[0])):
        t=0
        for j in range(len(col)):
            if sn[j]==0:
                if student[col[j]][i]==val[j]:
                    t=1
                    break
            elif sn[j]==2:
                if int(student[col[j]][i])<=int(val[j]):
                    t=1
                    break
            elif sn[j]==3:
                if int(student[col[j]][i])>=int(val[j]):
                    t=1
                    break
            elif sn[j]==4:
                
                if int(student[col[j]][i])<int(val[j]):
                    t=1
                    break
            elif sn[j]==5:
                if int(student[col[j]][i])>int(val[j]):
                    t=1
                    break
                
            else:
                if student[col[j]][i]!=val[j]:
                    t=1
                    break
            
        if t==1:
            for k in range(len(student)):
                #print k,i
                if student[k]==[]:
                    break
                result[p].append(student[k][i])
            p=p+1
            #print p
        else:
            
            for x in range(len(col1)):
                t=1
                if sn1[x]!=[]:
                    for y in range(len(col1[x])):
                        if sn1[x][y]!=[]:
                            if sn1[x][y]==0:
                                
                                if not student[col1[x][y]][i]==val1[x][y]:
                                    #print 'not',student[col1[x][y]][i],val1[x][y]
                                    t=0
                                    break
                                #print  "sn   ",sn,student[col1[x][y]][i],val1[x][y]

                            elif sn1[x][y]==2:
                                if not int(student[col1[x][y]][i])<=int(val1[x][y]):
                                
                                    t=0
                                    break
                            elif sn1[x][y]==3:
                                if not int(student[col1[x][y]][i])>=int(val1[x][y]):
                                
                                    t=0
                                    break
                            elif sn1[x][y]==4:
                                #print 'aye'
                                if not int(student[col1[x][y]][i])<int(val1[x][y]):
                                    ##print student[col1[x][y]][i],val1[x][y]
                                    t=0
                                    break
                            elif sn1[x][y]==5:
                                if not int(student[col1[x][y]][i])>int(val1[x][y]):
                                
                                    t=0
                                    break

                            else:
                                if student[col1[x][y]][i]==val1[x][y]:
                                
                                    t=0
                                    break
                               # print "sn ",sn1[x][y],"    ",student[col1[x][y]][i],val1[x][y]
                    if t==1:
                        for b in range(len(student)):
                            if student[b]==[]:
                                break
                            result[p].append(student[b][i])                
                        p=p+1
                        break
                       # print p
                        #break
               # if t==1:
                #    break
                
                
    ##print 'result  ',result
    global l
    stri=str(l)
    global dic
    global schema
    strin=stri+'.txt'
    dic[stri]=strin
    schema[stri]=stu
    ##print schema
    write(result,strin)
    #l=l+1
    
    
    
        
        







def andor(a):
    #a='select ((a!=wwwd) or (a!=fjgkfj and b=sdjso and gg!=ujkh) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    #a='select ((a=wwwd) or (a=fjgkfj) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    tab=''
    tab=tabname(a)

    b=a.split(" and ")
    #print b
    h=[]
    h1=[]
    for m in range(len(b)):
        for i in range(len(b[m])):
            if b[m][i]=="(":
                k=0
                for j in range(i+1,len(b[m])):
                    if b[m][j]=="(":
                        k=1
                    if b[m][j]==")" and k==0:
                        k=1
                        if " or " in b[m][i:j]:
                           # print b[m][i:j]
                            h.append(b[m][i+1:j])
                        else:
                           # print b[m][i+1:j-1] 
                            h1.append(b[m][i+1:j])

    o=""
    for i in range(len(a)):
        if a[i]=="[":
            st=i
            for j in range(i+1,len(a)):
                if a[j]=="]":
                    en=j
                    o=a[i+1:j-1]

    #print o





    #print "h:  "
    #print h
    #print "h1:  "
    #print h1
    andlist=[]
    w=[]
    count=0
    count1=0
    for i in h1:
        if "!=" in i:
            andlist.append(i.split("!="))
            andlist[count].append(1)
            count=count+1
        elif "<=" in i:
            andlist.append(i.split("<="))
            andlist[count].append(2)
            count=count+1
        elif ">=" in i:
            andlist.append(i.split(">="))
            andlist[count].append(3)
            count=count+1
        elif "<" in i:
            andlist.append(i.split("<"))
            andlist[count].append(4)
            count=count+1
        elif ">" in i:
            andlist.append(i.split(">"))
            andlist[count].append(4)
            count=count+1
        else:
            andlist.append(i.split("="))
            andlist[count].append(0)
            count=count+1

                            


    #print "andlist:   "
    #print andlist
    for i in range(len(h)):
        w.append(h[i].split(" or "))
    #print "w  :"  
    #print w
    orlist=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(w)):
        count1=0
        for j in range(len(w[i])):
            if "!=" in w[i][j]:
                orlist[i].append(w[i][j].split("!="))
                orlist[i][count1].append(1)
                count1=count1+1
            elif "<=" in w[i][j]:
                orlist[i].append(w[i][j].split("<="))
                orlist[i][count1].append(2)
                count1=count1+1
            elif ">=" in w[i][j]:
                orlist[i].append(w[i][j].split(">="))
                orlist[i][count1].append(3)
                count1=count1+1
            elif "<" in w[i][j]:
                orlist[i].append(w[i][j].split("<"))
                orlist[i][count1].append(4)
                count1=count1+1
            elif ">" in w[i][j]:
                orlist[i].append(w[i][j].split(">"))
                orlist[i][count1].append(5)
                count1=count1+1
                
            else:
                orlist[i].append(w[i][j].split("="))
                orlist[i][count1].append(0)
                count1=count1+1
    #print "orlist:    "
    #print orlist
    fname=''
    #student=[['avinash','appu','sourabh','dilip'],['8050594923','8971408649','8998987898','8967563432'],['udupi','kota','udupi','karkala']]
    
    fname=dic[tab]
            
    student=read(fname)
    
    #print student

    #student=[['avinash','appu','sourabh','dilip'],['8050594923','8971408649','8998987898','8967563432'],['udupi','kota','udupi','karkala']]
    stu=schema[tab]
    anddor(student,andlist,stu,orlist)


def anddor(s=[],a=[[]],st=[],o=[[[]]]):
    student=s
    stu=st
    andlist=a
    orlist=o
    col=[]
    val=[]
    sn=[]
    result=[[],[],[],[]]
    for i in range(40):
        result.append([])

    p=0
    if andlist!=[[]]:
        
        for i in andlist:
            col.append(stu.index((i[0])))
            sn.append(i[2])
            val.append(i[1])
    ##print col
    ##print sn
    ##print val

    col1=[[],[],[],[],[]]
    val1=[[],[],[],[],[]]
    sn1=[[],[],[],[],[]]

    """for i in range(len(andlist)):
        for j in range(len(i)):
            for k in range(len(k)):
    """
    for i in orlist:
        if i!=[[]]:
            for j in i:
                col1[orlist.index(i)].append(stu.index(j[0]))
                val1[orlist.index(i)].append(j[1])
                sn1[orlist.index(i)].append(j[2])

    ##print col1
    ##print val1
    ##print sn1

    for i in range(len(student[0])):
        t=0
        for j in range(len(col)):
            if sn[j]==0:
                if student[col[j]][i]!=val[j]:
                    t=1
                    break
            elif sn[j]==2:
                if not int(student[col[j]][i])<=int(val[j]):
                    t=1
                    break
            elif sn[j]==3:
                if not int(student[col[j]][i])>=int(val[j]):
                    t=1
                    break
            elif sn[j]==4:
                if not int(student[col[j]][i])<int(val[j]):
                    t=1
                    break
            elif sn[j]==5:
                if not int(student[col[j]][i])>int(val[j]):
                    t=1
                    break
            
                    
            else:
                if student[col[j]][i]==val[j]:
                    t=1
                    break
            
        
        if t==0:
            #print student[0][i]
            for x in range(len(col1)):
                
               
                if sn1[x]!=[]:
                    t=1
                    for y in range(len(col1[x])):
                        if sn1[x][y]!=[]:
                            if sn1[x][y]==0:
                                if student[col1[x][y]][i]==int(val1[x][y]):
                                
                                    t=0
                                    break
                            elif sn1[x][y]==2:
                                if int(student[col1[x][y]][i])<=int(val1[x][y]):
                                    t=0
                                    break
                            elif sn1[x][y]==3:
                                if int(student[col1[x][y]][i])>=int(val1[x][y]):
                                    t=0
                                    break
                            elif sn1[x][y]==4:
                                if int(student[col1[x][y]][i])<int(val1[x][y]):
                                    t=0
                                    break
                            elif sn1[x][y]==5:
                                if int(student[col1[x][y]][i])>int(val1[x][y]):
                                    t=0
                                    break
                                
                                
                                #print  "sn   ",sn,student[col1[x][y]][i],val1[x][y]
                            else:
                                if student[col1[x][y]][i]!=val1[x][y]:
                                
                                    t=0
                                    break
                               # print "sn ",sn1[x][y],"    ",student[col1[x][y]][i],val1[x][y]
                if t==0:
                    for b in range(len(student)):
                        if student[b]==[]:
                            break
                        result[p].append(student[b][i])                
                    p=p+1
                    break
                       # print p
                        #break
               # if t==1:
                #    break
                
                
    ##print result
    global l
    stri=str(l)
    strin=stri+'.txt'
    global dic
    global schema
    dic[stri]=strin
    schema[stri]=stu
    ##print schema
    write(result,strin)
    #l=l+1



def tabname(a):
    o=""
    flag=0
    for i in range(len(a)):
        if a[i]=="[":
            for j in range(i+1,len(a)):
                if a[j]=='[':
                    break
                if a[j]=="]":
                    flag=1
                    o=a[i+1:j]
                    break
            if flag==1:
                break

    return o


#a='project (rollno,name,surname,dob,mob,yob) from [clas]'
#a='project (a1,a2,a3,a4) from [tab2]'
def pro(a):
    f=''
    for i in range(len(a)):
        if a[i]=='(':
            for j in range(i+1,len(a)):
                if a[j]=='(':
                    break
                if a[j]==')':
                    f=a[i+1:j]
                    c=f.split(',')
                    break
                    
    #print c
    t=''
    tab=[]
    schm=[]
    for i in range(len(a)):
        if a[i]=='[':
            for j in range(i+1,len(a)):
                if a[j]==']':
                    t=a[i+1:j]
                    #print t
                    break
        if t!='':
            break
    global schema
    global dic
    #print dic
    #print schema
    tab=dic[t]
    #print tab
    schm=schema[t]
    
    #print tab
    #print schm
    col=[]
    global l
    s=`l`
    #l=l+1
    fil=s+'.txt'
    dic[s]=fil
    schema[s]=[]    
    for i in c:
        schema[s].append(i)
        col.append(schm.index(i))
    #print 'yiyiotgo     ',schema
    #print col
    #print schema[s]
    table=[[],[],[],[],[],[],[],[]]
    solution=[[],[],[],[],[],[],[],[]]
    for i in range(30):
        solution.append([])
        table.append([])
    table=read(tab)
    
    p=0
    for i in range(len(col)):
        for j in range(len(table[0])):
            solution[p].append(table[col[i]][j])
        p=p+1
    #print 'solution:    ',solution
    #print schema
    write2(solution,dic[s])
                            
                        
                    
        
def write2(o,a):
    j=0
    lol=[[],[],[],[],[]]
    for i in range(60):
        lol.append([])
    #print len(o)
        
    for i in range(len(o[0])):
        
        for j in range(len(o)):
            if o[j]!=[]:
     #           print j,i
                lol[i].append(o[j][i])
            #print j,i

    #print lol
    import csv
    with open(a, 'w') as f:
    
        w = csv.writer(f, dialect = 'excel-tab')
        w.writerows(lol)




        


        
        




            
  



def seperate(a):
    #global a
    #print r
    sig=0
    k=0
    v=0
    check=0
    flag=0
    global it
    t=[]
    p=[]
    global l
    if '{' in a:
        for i in range(len(a)):
                if a[i]=='{':
                        for j in range(i+1,len(a)):
                                if a[j]=='{':
                                    k=i
                                    v=j
                                    break
                                if a[j]=='}' :
                                    #print a[i:j]
                                    #print k,v
                                    if k<v and "select" in a[k:v] and "crossjoin" in a[i:j]:
                                        #print 'send',a[k:j+1] 
                                        fun(a[k:j+1])
                                        check=1
                                        p=a[:k]
                                        p=p+' ['
                                        p=p+`l`
                                        p=p+']'
                                        #print p,l
                                        l=l+1
                                        p=p+a[j:-1]
                                        #print 'wtf   ',p
                                        
                                        
                                    t=a[i+1:j]
                                    #print 't is  ',t,l
                                    if check==0:
                                        get(t)
                                        p=a[:i]
                                        p=p+' ['
                                        #print `l`
                                        #g=l
                                        #g=g+1
                                        p=p+`l`
                                        #g=g+1
                                        p=p+']'
                                        it=`l`
                                        l=l+1
                                        p=p+a[j:-1]
                                        #print 'p is  ',p
                                    if '{' in p:
                                        #print 'p    ',p,l
                                        seperate(p)
                                        #print l,p
                                        flag=1
                                        break
                                    if '<-' in p:
                                        b=''
                                        #print 'scsc',p
                                        global schema
                                        o=p.split('<-')
                                        #print o[0]
                                        
                                        for e in range(len(o[0])):
                                            #print o[0][e]
                                            if o[0][e]=='(':
                                                #print 'dfg'       
                                                for n in range(e+1,len(o[0])):
                                                    if o[0][n]==')':
                                                        sig=1
                                                        flag=1
                                                        #print o[0][e+1:n]
                                                        b=o[0][e+1:n]
                                                        #print 'tttt',b
                                                        break
                                            if flag==1:
                                                break
                                            
                                        #print b
                                        if sig==1:    
                                            ne=b.split(',')
                                            #print 'cxv',ne
                                            k=str(l-1)
                                            #print 'dgfh',schema[k]
                                            #global schema
                                            del schema[k]
                                            schema[k]=[]
                                            for f in range(len(ne)):
                                                schema[k].append(ne[f])
                                            #print schema[k]
                                            #break
                                        if '[' in o[0]:
                                            
                                            for k in range(len(o[0])):
                                                if o[0][k]=='[':
                                                    for n in range(k+1,len(o[0])):
                                                        if o[0][n]==']':
                                                            flag=1
                                                            b=o[0][k+1:n]
                                                            break
                                                global dic
                                                k=str(l-1)
                                                y=schema[k]
                                                del schema[k]
                                                x=dic[k]
                                                del dic[k]
                                                dic[b]=x
                                                it=b
                                                schema[b]=y
                                                #print x
                                                break
                                        #print dic,schema
                                        
                                        
                                                
                        if flag==1:
                            break












def fun(a):
    tables=[]
    tab=[]
    f=''
    l=0
    col=[]
    for i in range(len(a)):
        if a[i]=='{':
            for j in range(i+1,len(a)):
                if a[j]=='{':
                    
                    if "select" in a[i:j]:
                        if 'crossjoin' in a[j:]:
                            l=1
                            
                            #print 'change'
                            #print a[i:j]
                            #print a[j+1:]
                            #print len(a[j+1:])
                            #print a[j]
                            break
                    else:
                        break
                            
            got=0
            if l==1:
                
                for k in range(j+1,len(a)):
                    #print k
                    if a[k]=='[':
                        #print a[k]
                        for l in range(k+1,len(a)):
                            if a[l]==']':
                                  break
                        f=a[k+1:l]
                        break
                tables=f.split(',')
                #print tables
                for m in range(i+1,len(a)):
                    if a[m]=='}':
                        for b in range(m+1,len(a)):
                            if a[b]=='}':
                                got=1
                                break
                        if got==1:
                            break
                #sol=''
                #sol=a[:i]
                #sol=sol+a[b+1:]
                #print 'back'+sol
                #print a[i:j]        
                for k in range(i,j):
                    if a[k]=='(':
                        count=1
                        #print count
                        for l in range(k+1,j):
                            if a[l]=='(':
                                count=count+1
                            if a[l]==')':
                                count=count-1
                                if count==0:
                                    f=a[k:]
                                    #print 'here',f
                                    
                                    differentiate2(f)
                                    break
                                else:
                                    count=count-1
                        if count==1:
                            break


def andor2(a):
    #a='select ((a!=wwwd) or (a!=fjgkfj and b=sdjso and gg!=ujkh) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    #a='select ((a=wwwd) or (a=fjgkfj) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'

    b=a.split(" and ")
    #print b
    h=[]
    h1=[]
    for m in range(len(b)):
        for i in range(len(b[m])):
            if b[m][i]=="(":
                k=0
                for j in range(i+1,len(b[m])):
                    if b[m][j]=="(":
                        k=1
                    if b[m][j]==")" and k==0:
                        k=1
                        if " or " in b[m][i:j]:
                           # print b[m][i:j]
                            h.append(b[m][i+1:j])
                        else:
                           # print b[m][i+1:j-1] 
                            h1.append(b[m][i+1:j])

    o=""
    for i in range(len(a)-1):
        if a[i]=="[":
            st=i
            for j in range(i+1,len(a)):
                if a[j]=="]":
                    en=j
                    o=a[i+1:j]

    #print o





    #print "h:  "
    #print h
    #print "h1:  "
    #print h1
    andlist=[]
    w=[]
    count=0
    count1=0
    for i in h1:
        if "!=" in i:
            andlist.append(i.split("!="))
            andlist[count].append(1)
            count=count+1
        elif "<=" in i:
            andlist.append(i.split("<="))
            andlist[count].append(2)
            count=count+1
        elif ">=" in i:
            andlist.append(i.split(">="))
            andlist[count].append(3)
            count=count+1
        elif "<" in i:
            andlist.append(i.split("<"))
            andlist[count].append(4)
            count=count+1
        elif ">" in i:
            andlist.append(i.split(">"))
            andlist[count].append(5)
            count=count+1

        else:
            andlist.append(i.split("="))
            andlist[count].append(0)
            count=count+1
    #print "andlist:   "
    #print andlist
    for i in range(len(h)):
        w.append(h[i].split(" or "))
    #print "w  :"  
    #print w
    orlist=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(w)):
        count1=0
        for j in range(len(w[i])):
            if "!=" in w[i][j]:
                orlist[i].append(w[i][j].split("!="))
                orlist[i][count1].append(1)
                count1=count1+1
            elif "<=" in w[i][j]:
                orlist[i].append(w[i][j].split("<="))
                orlist[i][count1].append(2)
                count1=count1+1
            elif ">=" in w[i][j]:
                orlist[i].append(w[i][j].split(">="))
                orlist[i][count1].append(3)
                count1=count1+1
            elif "<" in w[i][j]:
                orlist[i].append(w[i][j].split("<"))
                orlist[i][count1].append(4)
                count1=count1+1
            elif ">" in w[i][j]:
                orlist[i].append(w[i][j].split(">"))
                orlist[i][count1].append(5)
                count1=count1+1



            else:
                orlist[i].append(w[i][j].split("="))
                orlist[i][count1].append(0)
                count1=count1+1
    #print "orlist:    "
    #print orlist
    tab=[]
    tab=tns(a)
    #print tab
    andorr(andlist,orlist,tab)


def tns(a):
    #print a
    for i in range(len(a)):
        l=0
        if a[i]=='[':
            
            #print a[i]
            for j in range(i+1,len(a)):
                #print a[j]
                if a[j]==']':
                    l=1
                    #print a[i+1:j],l
                    #print a[j]
                    #print a[i+1:j]
                    break
            if l==1:
                #print l
                
                break
    s=''
    s=a[i+1:j]
    #print s
    tab=s.split(',')
    return tab
       

def orand2(a):
    #a='select ((a!=wwwd) or (a!=fjgkfj and b=sdjso and gg!=ujkh) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    #a='select ((a=wwwd) or (a=fjgkfj) or (olkfgo=grmkd and dkjg=wekf) or (dkhf=dufh))from [table1]'
    
    b=a.split(" or ")
    #print b
    h=[]
    h1=[]
    for m in range(len(b)):
        for i in range(len(b[m])):
            if b[m][i]=="(":
                k=0
                for j in range(i+1,len(b[m])):
                    if b[m][j]=="(":
                        k=1
                    if b[m][j]==")" and k==0:
                        k=1
                        if " and " in b[m][i:j]:
                            #print b[m][i+1:j]
                            h.append(b[m][i+1:j])
                        else:
                            #print b[m][i+1:j-1] 
                            h1.append(b[m][i+1:j])

    """o=""
    for i in range(len(a)-1):
        if a[i]=="[":
            st=i
            for j in range(i+1,len(a)):
                if a[j]=="]":
                    en=j
                    o=a[i+1:j-1]

    print o"""
    





    #print "h:  "
    #print h
    #print "h1:  "
    #print h1
    orlist=[]
    w=[]
    count=0
    count1=0
    for i in h1:
        if "!=" in i:
            orlist.append(i.split("!="))
            orlist[count].append(1)
            count=count+1
        elif "<=" in i:
            orlist.append(i.split("<="))
            orlist[count].append(2)
            count=count+1
        elif ">=" in i:
            orlist.append(i.split(">="))
            orlist[count].append(3)
            count=count+1
        elif "<" in i:
            orlist.append(i.split("<"))
            orlist[count].append(4)
            count=count+1
        elif ">" in i:
            orlist.append(i.split(">"))
            orlist[count].append(5)
            count=count+1


        else:
            orlist.append(i.split("="))
            orlist[count].append(0)
            count=count+1
    #print "orlist:   "
    #print orlist
    for i in range(len(h)):
        w.append(h[i].split(" and "))
    #print "w  :"  
    #print w
    andlist=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(w)):
        count1=0
        for j in range(len(w[i])):
            if "!=" in w[i][j]:
                andlist[i].append(w[i][j].split("!="))
                andlist[i][count1].append(1)
                count1=count1+1
            elif "<=" in w[i][j]:
                andlist[i].append(w[i][j].split("<="))
                andlist[i][count1].append(2)
                count1=count1+1
            elif ">=" in w[i][j]:
                andlist[i].append(w[i][j].split(">="))
                andlist[i][count1].append(3)
                count1=count1+1
            elif "<" in w[i][j]:
                andlist[i].append(w[i][j].split("<"))
                andlist[i][count1].append(4)
                count1=count1+1
            elif ">" in w[i][j]:
                andlist[i].append(w[i][j].split(">"))
                andlist[i][count1].append(5)
                count1=count1+1




            else:
                andlist[i].append(w[i][j].split("="))
                andlist[i][count1].append(0)
                count1=count1+1
    #print "andlist:    "
    #print andlist
    #print a
    tab=[]
    tab=tns(a)
    #print 'table',tab
    orandd(orlist,andlist,tab)











def differentiate2(a):
    c=0
    f=1
    for i in range(len(a)):
        if a[i]=='(':
            f=1
            for j in range(i+1,len(a)):
                if a[j]=='(':
                    f=1
                    break
                    
                elif a[j]==')':
                    f=0
                    break
                    
            if f==0:
                if " and " in a[i:j]:
                    #print 'orand'
                    c=1
                    orand2(a)
                    break
                elif " or " in a[i:j]:
                    #print 'andor'
                    c=1
                    andor2(a)
                    break
                else:
                    f=1
    if c==0:
        #print 'no','orand'
        orand2(a)


def orandd(o=[[]],a=[[[]]],t=[]):     
    #orlist=[['clas.rollno', 'marks.rollno', 0],['marks.date','clas.dob',0]]
    #andlist=[[['marks.rollno', 'clas.rollno', 0]], [['marks.subject','clas.surname',0],['marks.subject','clas.city',0]], [], [], [], [], [], [], [], []]
    orlist=o
    andlist=a
    tables=t
    global schema
    global l
    global dic
    k=0
    column1=[]
    val1=[]
    val2=[]
    column2=[]
    sn=[]
    if orlist!=[]:
        for i in orlist:
            arr=i[0].split('.')
            if arr[0]==tables[0]:
                column1.append(arr[0])
                val1.append(arr[1])
                arr=i[1].split('.')
                column2.append(arr[0])
                val2.append(arr[1])
            else:
                column2.append(arr[0])
                val2.append(arr[1])
                arr=i[1].split('.')
                column1.append(arr[0])
                val1.append(arr[1])
                
            sn.append(i[2])
        
    col1=[]
    col2=[]
    col3=[]
    col4=[]
    for i in range(len(column1)):
        col1.append(schema[column1[i]].index(val1[i]))
        col2.append(schema[column2[i]].index(val2[i]))
    #print 'table1',column1    
    #print 'col1',col1
    #print 'table2',column2
    #print 'col2',col2
    #print sn
    column11=[[]]
    column22=[[]]
    val11=[[]]
    val22=[[]]
    col11=[[]]
    col22=[[]]
    sn1=[[]]
    for i in range(10):
        column11.append([])
        column22.append([])
        val11.append([])
        val22.append([])
        sn1.append([])

        col11.append([])
        col22.append([])
    k=0
    for i in andlist:
        if i!=[[]]:
            for j in i:
                arr=j[0].split('.')
                #print arr,len(arr)
                #print tables,len(tables)
                
                if arr[0]==tables[0]:
                    column11[k].append(arr[0])
                    val11[k].append(arr[1])
                    arr=j[1].split('.')
                    column22[k].append(arr[0])
                    val22[k].append(arr[1])
                else:
                    column22[k].append(arr[0])
                    val22[k].append(arr[1])
                    arr=j[1].split('.')
                    column11[k].append(arr[0])
                    val11[k].append(arr[1])
                    
                sn1[k].append(j[2])
            k=k+1

    #print column11
    #print val11
    #print column22
    #print val22
    k=0
    for i in range(len(column11)):
        for j in range(len(column11[i])):
            #print schema[column11[i][j]],"   ",val11[i][j]
            col11[j].append(schema[column11[i][j]].index(val11[i][j]))
            col22[j].append(schema[column22[i][j]].index(val22[i][j]))
                               

    #print col11,col22
    table1=[[]]
    table2=[[]]
    t1=[[]]
    t2=[[]]
    solution=[[]]
    for i in range(20):
        table1.append([])
        table2.append([])
        solution.append([])
        t2.append([])

    table1=read(dic[tables[0]])
    table2=read(dic[tables[1]])


    m=0
    for i in range(len(table1[0])):
        for j in range(len(table2[0])):
            flag=0
            for k in range(len(orlist)):
                if sn[k]!=[]:
                    if sn[k]==0:
                        if table1[col1[k]][i]==table2[col2[k]][j]:
                            flag=1
                            break
                    elif sn[k]==2:
                        if int(table1[col1[k]][i])<=int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==3:
                        if int(table1[col1[k]][i])>=int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==4:
                        if int(table1[col1[k]][i])<int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==5:
                        if int(table1[col1[k]][i])>int(table2[col2[k]][j]):
                            flag=1
                            break
                    else:
                        if table1[col1[k]][i]!=table2[col2[k]][j]:
                            flag=1
                            break
            if flag==1:
                for h in range(len(table1)):
                    if table1[h]==[]:
                        break
                    solution[m].append(table1[h][i])
                for h in range(len(table2)):
                    if table2[h]==[]:
                        break
                    solution[m].append(table2[h][j])
                m=m+1
            else:
                for x in range(len(col11)):
                    flag=1
                    if sn1[x]!=[]:
                        for y in range(len(col11[x])):
                            if sn1[x][y]!=[]:
                                if sn1[x][y]==0:
                                    if not table1[col11[x][y]][i]==table2[col22[x][y]][j]:
                                        flag=0
                                        break
                                elif sn1[x][y]==2:
                                    if not int(table1[col11[x][y]][i])<=int(table2[col22[x][y]][j]):
                                        flag=0
                                        break

                                elif sn1[x][y]==3:
                                    if not int(table1[col11[x][y]][i])>=int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                elif sn1[x][y]==4:
                                    if not int(table1[col11[x][y]][i])<int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                elif sn1[x][y]==5:
                                    if not int(table1[col11[x][y]][i])>int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                else:
                                    if not table1[col11[x][y]][i]!=table2[col22[x][y]][j]:
                                        flag=0
                                        break
                        if flag==1:
                            for h in range(len(table1)):
                                if table1[h]==[]:
                                    break
                                solution[m].append(table1[h][i])
                            for h in range(len(table2)):
                                if table2[h]==[]:
                                    break
                                solution[m].append(table2[h][j])
                            m=m+1
                            break
    ##print solution
#"""    stri=`l`
    """name=stri+'.txt'
    
    scm=[]
    for i in range(len(schema[tables[0]])):
        scm.append(schema[tables[0]][i])
    for i in range(len(schema[tables[1]])):
        scm.append(schema[tables[1]][i])
    #scm.append(schema[tables[0]])
    #scm.append(schema[tables[1]])
    schema[l]=scm
    dic[stri]=name
    write(solution,name)
    ##l=l+1
    print schema
    print dic"""

    #global schema
    
    stri=`l`
    strin=stri+'.txt'
    #l=l+1
    #print l
    write(solution,strin)
    dic[stri]=strin
    scm=[]
    s=''
    for i in range(len(schema[tables[0]])):
        s=tables[0]
        s=s+'.'
        s=s+schema[tables[0]][i]
        scm.append(s)
    for i in range(len(schema[tables[1]])):
        s=tables[1]
        s=s+'.'
        s=s+schema[tables[1]][i]
        scm.append(s)
    schema[stri]=scm


    


def andorr(a=[[]],o=[[[]]],t=[]):
    global schema
    andlist=a
    #print andlist
    orlist=o
    tables=t
    column1=[]
    column2=[]
    val1=[]
    val2=[]
    col1=[]
    col2=[]
    column11=[[]]
    column22=[[]]
    col11=[[]]
    col22=[[]]
    val11=[[]]
    val22=[[]]
    sn=[]
    sn1=[[]]
    #solution=[[]]
    table1=[[]]
    table2=[[]]
    solution=[[]]

    if andlist!=[]:
        for i in andlist:
            arr=i[0].split('.')
            if arr[0]==tables[0]:
                column1.append(arr[0])
                val1.append(arr[1])
                arr=i[1].split('.')
                column2.append(arr[0])
                val2.append(arr[1])
            else:
                column2.append(arr[0])
                val2.append(arr[1])
                arr=i[1].split('.')
                column1.append(arr[0])
                val1.append(arr[1])
            sn.append(i[2])

    #print column1,val1,column2,val2,sn

    for i in range(len(column1)):
        col1.append(schema[column1[i]].index(val1[i]))
        col2.append(schema[column2[i]].index(val2[i]))
    #print col1,col2    
    for i in range(40):
        column11.append([])
        column22.append([])
        val11.append([])
        val22.append([])
        sn1.append([])
        col11.append([])
        col22.append([])
        solution.append([])
        
    k=0
    for i in orlist:
        if i!=[[]]:
            for j in i:
                arr=j[0].split('.')
                if arr[0]==tables[0]:
                    column11[k].append(arr[0])
                    val11[k].append(arr[1])
                    arr=j[1].split('.')
                    column22[k].append(arr[0])
                    val22[k].append(arr[1])
                else:
                    
                    column22[k].append(arr[0])
                    val22[k].append(arr[1])
                    arr=j[1].split('.')
                    column11[k].append(arr[0])
                    val11[k].append(arr[1])
                        
                sn1[k].append(j[2])
            k=k+1
    #print column11,column22
    k=0
    for i in range(len(column11)):
        for j in range(len(column11[i])):
            #print schema[column11[i][j]],"   ",val11[i][j]
            col11[j].append(schema[column11[i][j]].index(val11[i][j]))
            col22[j].append(schema[column22[i][j]].index(val22[i][j]))
    #print col11,col22
    m=0
    table1=read(dic[tables[0]])
    table2=read(dic[tables[1]])
    #print table1
    for i in range(len(table1[0])):
        for j in range(len(table2[0])):
            
            flag=0
            for k in range(len(andlist)):
                if sn[k]!=[]:
                    if sn[k]==0:
                        if not table1[col1[k]][i]==table2[col2[k]][j]:
                            flag=1
                            break 
                    elif sn[k]==2:
                        if not int(table1[col1[k]][i])<=int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==3:
                        if not int(table1[col1[k]][i])>=int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==4:
                        if not int(table1[col1[k]][i])<int(table2[col2[k]][j]):
                            flag=1
                            break
                    elif sn[k]==5:
                        if not int(table1[col1[k]][i])>int(table2[col2[k]][j]):
                            flag=1
                            break
                    else:
                        if not table1[col1[k]][i]!=table2[col2[k]][j]:
                            #print table1[col1[k]][i],table2[col2[k]][j]
                            
                            flag=1
                            break
            if flag==0:
                #print table1[0][i],table1[1][i],table2[0][j],table2[1][j]
                for x in range(len(col11)):
                    
                    if sn1[x]!=[]:
                        flag=1
                        for y in range(len(col11[x])):
                            
                            if sn1[x][y]!=[]:
                                print sn1[x][y]
                                if sn1[x][y]==0:
                                    if table1[col11[x][y]][i]==table2[col22[x][y]][j]:
                                        flag=0
                                        break
                                elif sn1[x][y]==2:
                                    if int(table1[col11[x][y]][i])<=int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                elif sn1[x][y]==3:
                                    if int(table1[col11[x][y]][i])>=int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                elif sn1[x][y]==4:
                                    if int(table1[col11[x][y]][i])<int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                elif sn1[x][y]==5:
                                    if int(table1[col11[x][y]][i])>int(table2[col22[x][y]][j]):
                                        flag=0
                                        break
                                else:
                                    #print table1[col11[x][y]][i],table2[col22[x][y]][j]
                                    if table1[col11[x][y]][i]!=table2[col22[x][y]][j]:
                                        flag=0
                                        break
                    if flag==1:
                            
                        for h in range(len(table1)):
                            if table1[h]==[]:
                                break
                            solution[m].append(table1[h][i])
                        for h in range(len(table2)):
                            if table2[h]==[]:
                                break
                            solution[m].append(table2[h][j])
                        m=m+1
                        break
    #print solution
    global l

    #global schema
    stri=`l`
    strin=stri+'.txt'
    l=l+1
    #print l
    write(solution,strin)
    dic[stri]=strin
    scm=[]
    s=''
    for i in range(len(schema[tables[0]])):
        s=tables[0]
        s=s+'.'
        s=s+schema[tables[0]][i]
        scm.append(s)
    for i in range(len(schema[tables[1]])):
        s=tables[1]
        s=s+'.'
        s=s+schema[tables[1]][i]
        scm.append(s)
    schema[stri]=scm

def help(a1,a2,stu=[],cc=[]):
    import csv
    #a='ak1.txt'
    #a=s2[0]
    o=[[],[],[],[],[],[],[],[],[],[],[]]

    a=a1
    s = list(csv.reader(open(a, 'rb'), delimiter='\t'))
    student=[[],[],[]]
    import csv
    #a='ak2.txt'
    a=a2
    c= list(csv.reader(open(a, 'rb'), delimiter='\t'))
    citycode=[[],[]]
    for i in range(100):
        student.append([])
        citycode.append([])
        o.append([])
    #stu=s1[0]
    #cc=s1[1]
    #stu=['name','phone','city']
    #cc=['city','code']
    res=[]
    #print len(student)
    #print s
    
    for i in range(len(s[0])):
        for j in range(len(s)):
            #print j,'    ',i
            #print s[j][i]
            student[i].append(s[j][i])        
    #print student

    for i in range(len(c[0])):
        for j in range(len(c)):
            citycode[i].append(c[j][i])        
    #print citycode

    for i in stu:
        for j in cc:
            if i==j:
                u=stu.index(i)
                k=cc.index(j)

    for i in stu:
        res.append(i)
    for j in cc:
        if j!=cc[k]:
            res.append(j)

    #print res                
    
    for i in range(len(student[0])):
    
        for j in range(len(citycode[0])):
            if student[u][i]==citycode[k][j]:
                for q in range(len(student)):
                    if student[q]==[]:
                        break
                    m=q
                    o[q].append(student[q][i])
                    m=m+1
                
                for n in range(len(citycode)):
                    if citycode[n]==[]:
                        break
                    if n==k:
                        m=m-1
                        n=n+1
                    else:
                   
                        o[m+n].append(citycode[n][j])

    """lol=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(o[0])):
        for j in range(m+n+1):
            lol[i].append(o[j][i])

    with open('sample2.txt', 'w') as f:
    
        w = csv.writer(f, dialect = 'excel-tab')
        w.writerows(lol)
    
    """
    global dic
    global l
    global schema
    stri=`l`
    
    strin=stri+'.txt'
    write2(o,strin)
    dic[stri]=strin
    schema[stri]=res






def tabname(a):
    p=0
    q=0
    o=""
    for i in range(len(a)):
        if a[i]=="[":
            p=0
            for j in range(i+1,len(a)):
                if a[j]=="[":
                    p=1
                    break
            if p==0:
                #print a[i:]
                for j in range(i+1,len(a)):
                    
                    if a[j]==']':
                        q=1
                        #print a[i+1:j]
                        break
        if q==1:
            break
    #print a[i+1:j]
    return a[i+1:j]

    #print o


def agg(a):
    f=1
    for i in range(len(a)):
        k=0
        if a[i]=='(':
            for j in range(i+1,len(a)):
                if a[j]=='(':
                    k=1
                    break
            if k==0:
                for j in range(i+1,len(a)):
                    if a[j]==')':
                        f=0
                        break
                if f==0:
                    break
    global l
    global schema
    global dic
    s=a[i+1:j].split(',')
    #print s
    fname=[]
    cname=[]
    cn=[]
    f1=[]
    tab=''
    #print schema
    #global schema
    #global dic
    tab=tabname(a)
    #print tab
    table=read(dic[tab])
    for i in s:
        w=i.split(':')
        fname.append(w[0])
        cname.append(w[1])
        cn.append(schema[tab].index(w[1]))
    #print cn
    #print fname
    #print cname
    solution=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    if "->" in a:
        r=a.split('->')
        #t1=''
        #t1=tabname(r[0])
        for i in range(len(r[0])):
            m=0
            if a[i]=='(':
                for j in range(i+1,len(r[0])):
                    if a[j]==')':
                        m=1
                        break
            if m==1:
                break
        f=a[i+1:j]
        #print f
        num=schema[tab].index(f)
        #print num
        check=[]
        for i in range(len(table[num])):
            if table[num][i] not in check:
                check.append(table[num][i])
                solution[0].append(table[num][i])
        
        
        #print solution


        
        for j in range(len(cn)):
            if fname[j]=='count':
                for i in range(len(check)):
                    count=0
                    for z in range(len(table[0])):
                        if table[num][z]==check[i]:
                            count=count+1
                    solution[j+1].append(count)
            if fname[j]=='max':
                for i in range(len(check)):
                    maxi=-9999
                    for z in range(len(table[0])):
                        #print table[0][z],i,j,z
                        if table[num][z]==check[i] and int(table[cn[j]][z])>maxi:
                            maxi=int(table[cn[j]][z])
                    solution[j+1].append(maxi)
            if fname[j]=='min':
                for i in range(len(check)):
                    mini=999999999
                    for z in range(len(table[0])):
                        #print table[0][z],i,j,z
                        if table[num][z]==check[i] and int(table[cn[j]][z])<mini:
                            mini=int(table[cn[j]][z])
                    solution[j+1].append(mini)
            if fname[j]=='avg':
                for i in range(len(check)):
                    summ=0
                    count=0
                    for z in range(len(table[0])):
                        if table[num][z]==check[i]:
                            count=count+1
                            summ=summ+int(table[cn[j]][z])
                    av=summ/count
                    solution[j+1].append(av)
            if fname[j]=='sum':
                for i in range(len(check)):
                    summ=0
                    for z in range(len(table[0])):
                        if table[num][z]==check[i]:
                            #count=count+1
                            summ=summ+int(table[cn[j]][z])
                    #av=summ/count
                    solution[j+1].append(summ)
            
        #global l
        stri=`l`
        strin=stri+'.txt'
        dic[stri]=strin
        write2(solution,strin)
        schema[stri]=[]
        schema[stri].append(f)
        for i in range(1,len(cn)+1):
            s=fname[i-1]
            s=s+'_'
            s=s+cname[i-1]
            schema[stri].append(s)




    else:        
        for j in range(len(cn)):
            if fname[j]=='count':
                count=0
                for z in range(len(table[0])):
                    if table[cn[j]][z]!=[]:
                        count=count+1
                solution[j+1].append(count)
            if fname[j]=='max':
                maxi=-9999
                for z in range(len(table[0])):
                    #print table[0][z],i,j,z
                    if table[cn[j]][z]!=[] and int(table[cn[j]][z])>maxi:
                        maxi=int(table[cn[j]][z])
                    solution[j+1].append(maxi)
            if fname[j]=='min':
                mini=999999999
                for z in range(len(table[0])):
                    #print table[0][z],i,j,z
                    if table[cn[j]][z]!=[] and int(table[cn[j]][z])<mini:
                            mini=int(table[cn[j]][z])
                    solution[j+1].append(mini)
            if fname[j]=='avg':
                #for i in range(len(check)):
                summ=0
                count=0
                for z in range(len(table[0])):
                    if table[cn[j]][z]!=[]:
                        count=count+1
                        summ=summ+int(table[cn[j]][z])
                        av=summ/count
                    solution[j+1].append(av)
            if fname[j]=='sum':
                #for i in range(len(check)):
                summ=0
                for z in range(len(table[0])):
                    if table[num][z]!=[]:
                        #count=count+1
                        summ=summ+int(table[cn[j]][z])
                    #av=summ/count
                    solution[j+1].append(summ)
            
        #global l
        stri=`l`
        strin=stri+'.txt'
        dic[stri]=strin
        write2(solution,strin)
        schema[stri]=[]
        #schema[stri]=f
        for i in range(0,len(cn)):
            s=fname[i]
            s=s+'_'
            s=s+cname[i]
            schema[stri].append(s)


            
            
def union(a):
    flag=0
    for i in range(len(a)):
        if a[i]=='[':
            for j in range(i+1,len(a)):
                if a[j]==']':
                    flag=1
                    break
            if flag==1:
                break
    b=a[i+1:j]
    c=b.split(',')
    global schema
    global dic
    table1=read(dic[c[0]])
    table2=read(dic[c[1]])
    solution=[[]]
    for i in range(100):
        solution.append([])
    sol=0
    for i in range(len(table1[0])):
        f=10
        for j in range(len(table2[0])):
            m=0
            v=0
            for k  in range(len(table1)):
                
                if table1[k]==[]:
                    v=1
                    break
                print table1[k][i],table2[k][j]
                if table1[k][i]!=table2[k][j]:
                    m=1
                    break
            #print len(table1[i])
            #print m,f,k
            if m==0:
                #print table1[k][i]
                f=11
                #print f
                break
        if f==10:
            #print 'ujkuj'
            for s in range(len(table1)):
                #print table1[s][i]
                if table1[s]==[]:
                    break
                solution[sol].append(table1[s][i])
            sol=sol+1
    for i in range(len(table2[0])):
        for j in range(len(table2)):
            if table2[j]==[]:
                break
            
            solution[sol].append(table2[j][i])
        sol=sol+1
    stri=`l`
    strin=stri+'.txt'
    write(solution,strin)
    dic[stri]=strin
    schema[stri]=schema[c[0]]

def inter(a):
    flag=0
    for i in range(len(a)):
        if a[i]=='[':
            for j in range(i+1,len(a)):
                if a[j]==']':
                    flag=1
                    break
            if flag==1:
                break
    b=a[i+1:j]
    c=b.split(',')
    global schema
    global dic
    table1=read(dic[c[0]])
    table2=read(dic[c[1]])
    solution=[[]]
    for i in range(100):
        solution.append([])
    sol=0
    for i in range(len(table1[0])):
        f=10
        for j in range(len(table2[0])):
            #m=0
            #v=0
            for k  in range(len(table1)):
                m=0
                if table1[k]==[]:
                    v=1
                    break
                #print table1[k][i],table2[k][j]
                if table1[k][i]!=table2[k][j]:
                    m=1
                    break
            #print len(table1[i])
            #print m,f,k
            if m==0:
                #print table1[k][i]
                f=11
                #print f
                break
        if f==11:
            #print 'ujkuj'
            for s in range(len(table1)):
                #print table1[s][i]
                if table1[s]==[]:
                    break
                solution[sol].append(table1[s][i])
            sol=sol+1
    stri=`l`
    strin=stri+'.txt'
    write(solution,strin)
    dic[stri]=strin
    schema[stri]=schema[c[0]]



def minus(a):
    flag=0
    for i in range(len(a)):
        if a[i]=='[':
            for j in range(i+1,len(a)):
                if a[j]==']':
                    flag=1
                    break
            if flag==1:
                break
    b=a[i+1:j]
    c=b.split(',')
    global schema
    global dic
    table1=read(dic[c[0]])
    table2=read(dic[c[1]])
    solution=[[]]
    for i in range(100):
        solution.append([])
    sol=0
    for i in range(len(table1[0])):
        f=10
        for j in range(len(table2[0])):
            m=0
            v=0
            for k  in range(len(table1)):
                
                if table1[k]==[]:
                    v=1
                    break
                #print table1[k][i],table2[k][j]
                if table1[k][i]!=table2[k][j]:
                    m=1
                    break
            #print len(table1[i])
            #print m,f,k
            if m==0:
                #print table1[k][i]
                f=11
                #print f
                break
        if f==10:
            #print 'ujkuj'
            for s in range(len(table1)):
                #print table1[s][i]
                if table1[s]==[]:
                    break
                solution[sol].append(table1[s][i])
            sol=sol+1
    stri=`l`
    strin=stri+'.txt'
    write(solution,strin)
    dic[stri]=strin
    schema[stri]=schema[c[0]]

run()

    
            
    
        
