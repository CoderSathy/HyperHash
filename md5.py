import hashlib

def hash(data):
       result = hashlib.md5(data.encode()) 
       return(result.hexdigest())