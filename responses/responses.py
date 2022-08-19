def send_error(msg : str = "", data: any = {}):
    return {
        'status': 400,
        'data': data,
        'message': msg
    }

def send_response(msg: str = "", data: any = {}):
    return {
        'status': 200,
        'data': data,
        'message': msg
    }