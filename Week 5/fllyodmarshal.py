import numpy as np
def flloydMarshal(VMat):
  (rows,cols,x)=VMat.shape
  infinity= np.max(VMat)*rows*rows+1
  SP=np.zeros(shape=(rows,cols,cols+1))

  for i in range(rows):
    for j in range(cols):
      SP[i,j,0]=infinity

  for i in range(rows):
    for j in range(cols):
      if VMat[i,j,0]==1:
        SP[i,j,0]=VMat[i,j,1]

  for i in range(1,cols+1):
    for j in range(rows):
      for k in range(cols):
        SP[i,j,k]=min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])
  return (SP[:,:,cols])