from parameter import parameters

def update_file(file_path, key, value):
    with open(file_path, "r") as file:
        read = file.readlines()
    
    updated= False
    with open(file_path, "w") as file:
        for line in read:
            if key in line:
                file.write(f"{key} = {value}\n")
                updated= True
            else:
                file.write(line)

        if not updated:
            file.write(f"{key} = {value}\n")

for key,value in parameters.items():

    update_file("server.conf", key, value)