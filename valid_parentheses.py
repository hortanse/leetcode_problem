#valid parentheses 
#Givin a string with ()[]{}, determine if it's balanced
#Approach: using stack
#pushing open brackets ((, {, [) into the stack
#when you see the closed brackets, check if it matches the last one pushed
#if the stack is empty in the end, it's valid

def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["} #create matching pairs

    for char in s:
        if char in mapping: #if it is a closing bracket
            top = stack.pop() if stack else "#" #get the last opened bracket
            if mapping[char] != top: #mismatch
                return False
        else:
            stack.append(char) #push opening bracket
    return not stack #stack should beempty if valid

# ✅ Test Cases
print(is_valid("({[]})"))  # Output: True
print(is_valid("{[(])}"))  # Output: False