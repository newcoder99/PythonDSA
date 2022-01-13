def histogram(L):
  d={}
  for i in range(0,len(L)):
    if(L[i] in d.keys()):
      d[L[i]]=d[L[i]]+1
    else:
      d[L[i]]=1
  
  f={}
  for key, value in d.items():
    if value not in f:
        f[value] = [key]
    else:
        f[value].append(key)
  
  L=[]
  dictionary_items = f.items()
  sorted_items = sorted(dictionary_items)
  for key in sorted_items:
    key[1].sort()
    for i in key[1]:
      L.append((i,key[0]))


  return Ls