def formatUrlParam(paramRaw):
    res = {}
    params = paramRaw.split("&")
    for param in params:
        keyValueArr = param.split("=")
        if (len(keyValueArr) == 1):
            continue
        res[keyValueArr[0]] = keyValueArr[1]
    
    return res