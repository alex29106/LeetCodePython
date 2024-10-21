def isMatch(s: str, p: str):
    reg_pointer = 0
    text_pointer = 0
    last_text = None
    # for i in range(len(s))
    while True:
        try:
            this_text = s[text_pointer]
            if p[reg_pointer] == this_text or p[0] == ".":
                reg_pointer += 1
                text_pointer += 1
                last_text = this_text
            elif p[reg_pointer] == "*":
                if last_text == ".":
                    return True
                elif last_text != this_text:
                    if this_text == p[reg_pointer + 1]:
                        last_text = this_text
                        reg_pointer += 1
                        text_pointer += 1
                    else:
                        return False
                else:
                    text_pointer += 1
            elif p[reg_pointer + 1] == "*":
                reg_pointer += 2
            else:
                return False
            if text_pointer == len(s):
                return True
        except:
            return False


print(isMatch("aab","c*a*b"))