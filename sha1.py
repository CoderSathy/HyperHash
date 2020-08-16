import hashlib

def hash(data):
       result = hashlib.sha1(data.encode()) 
       return(result.hexdigest())