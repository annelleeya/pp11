def rev():
    word=input()
    lst=word.split()
    lst.reverse()
    ans=''
    for i in lst:
        ans+=i+' '
    print (ans)
rev()