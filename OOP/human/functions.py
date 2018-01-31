from re import match

def check(param, string = False ) : 
   
    if match(r"[0-9]+", str(param) ) != None and not string :  
        return True
    
    if match(r"[a-zA-Zа-яА-ЯЁё]+", str(param) ) != None and string :  
        return True
