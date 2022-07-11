

with open('User_Memory.txt') as f:
    lines = f.readlines()
f.close()    



class User_1:
    def __init__(self,Name,Access,Status):
        self.Name = Name
        self.Access = Access
        self.Status = Status
    
    def get_Name(self):
        return(self.Name)
    def get_Access():
        return(self.Access)
    def get_Status():
        return(self.Status)

def create_user(createdby,Name,Access,Status):
    Write_to_User_Memory(Name,Access,Status)
    Name = User_1(Name,Access,Status)
    return(Name)

with open('User_Memory.txt') as f:
    lines = f.readlines()
    f.close()


def Write_to_User_Memory(Name,Access,Status):
    lines = 0
    with open('User_Memory.txt') as f:
        lines = f.readlines()
    f.close()
    xxyy = len(lines)   
    xx = [Name,Access,Status,]
    x = 0
    with open('User_Memory.txt',"a") as ft:
        while x <= 2:
            ft.write('\n')
            ft.write(str(xx[x]))
            
            x = x + 1 
    ft.close()    



    

