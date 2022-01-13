def del_char(s,c):
  if(len(c)>1):
    return s
  else:
    s=s.replace(c,'')
    return s
      
s = input()
c = input()
print(del_char(s,c))