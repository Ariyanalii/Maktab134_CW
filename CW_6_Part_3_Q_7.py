

def limited(func):
    def wrapper(func, *args, **kwargs):
        limited_list = []
        
        if func > len(limited_list):
            print(f"You've hitted the limit: {limited_list}")
        return func(*args, **kwargs)
    return wrapper




@limited
def in_string():

    
    print("Hello World")


in_string()