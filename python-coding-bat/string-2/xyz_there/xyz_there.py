# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    count = 0
    if str == "xyz":
        count += 1
    elif len(str) >= 4:
        for i in range(len(str) - 2):
            if str[i:i+3] == "xyz":
                if str[i-1] != ".":
                    count += 1
    if count == 1:
        return True
    return False
