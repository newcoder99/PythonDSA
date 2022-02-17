class stack:
    def __init__(self):
        self.stack = []
    def push(self,d):
        self.stack += [d]
    def pop(self):
        t = self.stack[-1]
        self.stack=self.stack[:-1]
        return t
    def top(self):
        return self.stack[-1]
def infix_to_postfix(infexp):
    op = ['+','-','*','/','^']
    priority ={'+':1,'-':1,'*':2,'/':2,'^':3}
    exp = list(infexp)
    st = stack()
    postfix=''
    for elm in exp:
        if elm == '(':
            st.push(elm)
        elif elm == ')':
            while st.top() != '(' :
                postfix += st.pop()
                if st.stack == []:
                    break
            st.pop()
        elif elm not in op:
            postfix += elm
        else:
            while st.stack and st.top() != '(' and priority[elm] <= priority[st.top()]:
                postfix += st.pop()
            st.push(elm)
    while st.stack:
       postfix += st.pop()
    print (postfix)
exp = input()
infix_to_postfix(exp)