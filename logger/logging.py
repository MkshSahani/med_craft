# filname: logging.py 

def log(api_refrence : str = "", msg : str = "", data : any = {}): 
    print(f"[*] LOG -> {api_refrence} msg : {msg} data : {data}")

def info(api_refrence: str = "", msg : str = "", data : any = {}): 
    print(f"[*] INFO -> {api_refrence} msg : {msg} data : {data}")

def error(api_refrence: str = "", msg : str = "", data : any = {}) :
    print(f"[*] EROR -> {api_refrence} msg : {msg} data : {data} ")
