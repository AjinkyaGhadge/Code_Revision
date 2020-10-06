def balancedParanthesis(s):
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
            continue
        if not stack:
            return False
        top = stack.pop()
        if i == ')':
            if top is not '(':
                return False
        if i == '}':
            if top is not '{':
                return False
        if i == ']':
            if top is not '[':
                return False

    if stack:
        return False
    else:
        return True

if __name__ == "__main__" :  
    expr = "{()}[]";  
    if balancedParanthesis(expr) : 
        print("Balanced");  
    else : 
        print("Not Balanced");
