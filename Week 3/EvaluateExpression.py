def EvaluateExpression(L):
  stack=[]
  Z=[i for i in L.split(" ")]
  ops = { "+": (lambda x,y: x+y), "-": (lambda x,y: x-y),"*":(lambda x,y: x*y),"/":(lambda x,y: float(x/y)),"**":(lambda x,y: x**y)}
  operator=['+','-','/','*','**']
  for i in range(0,len(Z)):
    if(Z[i] in operator):
      value1=float(stack.pop())
      value2=float(stack.pop())
      value3=ops[Z[i]](value2,value1)
      stack.append(value3)
    else:
      stack.append(Z[i])
  return stack[0]