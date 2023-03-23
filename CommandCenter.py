def clear_file(filename):
    with open(filename, 'w') as f:
        f.truncate(0)


selectedFile = input("Type the file you want to delete: ")
delete = input("Are you sure you want to delete", selectedFile,"\n? Yes/No").upper()
if (delete == "YES"):
    clear_file('blockchain.txt')
