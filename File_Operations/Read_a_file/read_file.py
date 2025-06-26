from parameter import search_key

def read_file(file_path, key):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    Found = False
    for line in lines :
        if key in line:
            print(f"{line}\n")
            Found = True
    if not Found:
        print(f"{lines}\n")


read_file("sample.log", search_key)