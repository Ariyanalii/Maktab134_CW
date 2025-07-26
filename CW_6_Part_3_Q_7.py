

def limited(func):
    def wrapper(*args, **kwargs):
        limited_list = []
    
        
        for i in limited_list:
            if len(limited_list) > 3:
                limited_list.append(func)
                print(f"You've hitted the limit: {limited_list}")
        return func(*args, **kwargs)
    return wrapper




@limited
def in_string():
    
    print("Hello World")

in_string()
