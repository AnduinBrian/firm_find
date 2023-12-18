import os, argparse,json

root_path = ""

def parse_agv():
    global root_path
    parser = argparse.ArgumentParser(
        prog="Firm Find",
        description="The script auto find important file in squashfs-root",
    )
    parser.add_argument('-f', metavar="", help="Path to squashfs-root",required=True)
    args = parser.parse_args()
    root_path = args.f

def load_config(path):
    with open(path, "r") as file:
        json_obj = json.load(file)
        return json_obj

def list_files(startpath):
    file_info = []
    for i in os.walk(startpath):
        for file in i[2]:
            file_info.append(i[0] + "/" + file)
    return file_info

def find_file(file_to_find, all_file):
    print("[+] File need to be found:")
    print("  [-] Finding Web Service file:")
    found = 0
    for i in all_file:
        file_name = i.split("/")[-1]
        if file_name in file_to_find["webservers_file"]:
            found = 1
            print("    [-] %s" % (i.split(root_path)[-1]))
    if found == 0:
        print("    [!] No file be found !!")
    
    print("  [-] Finding Password file:")
    found = 0
    for i in all_file:
        file_name = i.split("/")[-1]
        if file_name in file_to_find["password_file"]:
            found = 1
            print("    [-] %s" % (i.split(root_path)[-1]))
    if found == 0:
        print("    [!] No file be found !!")
    
    print("  [-] Finding ELF file:")
    found = 0
    for i in all_file:
        file_name = i.split("/")[-1]
        if file_name in file_to_find["elf_file"]:
            found = 1
            print("    [-] %s" % (i.split(root_path)[-1]))
    if found == 0:
        print("    [!] No file be found !!")
    print("")

def find_extension(ext_to_find, all_file):
    print("[+] File with extension need to be found:")
    print("  [-] Find Password extension file:")
    found = 0
    for i in all_file:
        extension_file_name = i.split(".")[-1]
        if extension_file_name in ext_to_find["passwd_file"]:
            found = 1
            print("    [-] %s" % ((i.split(root_path)[-1])))
    if found == 0:
        print("    [!] No file be found !!")
    
    print("  [-] Find config extension file:")
    found = 0
    for i in all_file:
        extension_file_name = i.split(".")[-1]
        if extension_file_name in ext_to_find["conf_file"]:
            found = 1
            print("    [-] %s" % ((i.split(root_path)[-1])))
    if found == 0:
        print("    [-] No file be found !!")
    
    print("  [-] Find Database extension file:")
    found = 0
    for i in all_file:
        extension_file_name = i.split(".")[-1]
        if extension_file_name in ext_to_find["db_file"]:
            found = 1
            print("    [-] %s" % ((i.split(root_path)[-1])))
    if found == 0:
        print("    [!] No file be found !!")

    print("  [-] Find SSL extension file:")
    found = 0
    for i in all_file:
        extension_file_name = i.split(".")[-1]
        if extension_file_name in ext_to_find["ssl_file"]:
            found = 1
            print("    [-] %s" % ((i.split(root_path)[-1])))
    if found == 0:
        print("    [!] No file be found !!")

    print("  [-] Find SSH extension file:")
    found = 0
    for i in all_file:
        extension_file_name = i.split(".")[-1]
        if extension_file_name in ext_to_find["ssh_file"]:
            found = 1
            print("    [-] %s" % ((i.split(root_path)[-1])))
    if found == 0:
        print("    [!] No file be found !!")   
    print("")

if __name__ == "__main__":
    print("")
    print("######################## FIRMWARE SEARCHING ########################")
    curr_path = os.getcwd()
    json_path = curr_path + "/config/config.json"
    json_obj = load_config(json_path)
    file_to_find = json_obj["config"]["file"]
    ext_to_find = json_obj["config"]["extension"]
    parse_agv()
    if "squashfs-root" not in root_path:
        print("[-] Not a squashfs-root dir !!")
        exit()
    all_file = list_files(root_path)
    find_file(file_to_find, all_file)
    find_extension(ext_to_find, all_file)


