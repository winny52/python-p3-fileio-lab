def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt',  mode="w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f"{file_name}.txt", "a",encoding="utf-8") as file:
        file.write(append_content)

def read_file(file_name):
    pass
    with open(f"{file_name}.txt", "r", encoding="utf-8") as file:
        return file.read()


write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")