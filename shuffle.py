def shuffle(L1,L2):
  L3=[]
  if(len(L1)==len(L2)):
   for i in range(0,len(L1)):
     L3.append(L1[i])
     L3.append('')
  
   j=1
   for i in range(0,len(L2)):
     L3[j]=L2[i]
     j=j+2
  else:
    if(len(L1)>len(L2)):
      for i in range(0,len(L2)):
        L3.append(L1[i])
        L3.append('')
      j=1
      for i in range(0,len(L2)):
        L3[j]=L2[i]
        j=j+2
      L3=L3+L1[len(L2):]
    else:
      L3=['']*(len(L1)+len(L2))
      j=0
      for i in range(0,len(L1)):
        L3[j]=L1[i]
        j=j+2
      j=1
      for i in range(0,len(L1)):
        L3[j]=L2[i]
        j=j+2
      ind=L3.index('')
      for i in range(len(L1),len(L2)):
        L3[ind]=L2[i]
        ind=ind+1
        

  return L3