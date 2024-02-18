import shutil, requests, zipfile, os

url = 'https://codeload.github.com/usewge/wge/zip/refs/heads/main'
def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        print("Download update with success!")
    else:
        print("Fail to download update.")
        
def move_file_or_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Copping files: {source} -> {destination}")
    except Exception as e:
        print(f"Error on move: {e}")
        
def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("File extracted to:", extract_to)

def delete_file_or_folder(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File {path} deleted with success.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Folder {path} deleted with success.")
        else:
            print(f"The path {path} isnt valid.")
    except Exception as e:
        print(f"Error on delete {path}: {e}")

delete_file_or_folder("./requirements.txt")
delete_file_or_folder("./uninstall.bat")
delete_file_or_folder("./WGE.bat")
delete_file_or_folder("./WGE-debug.bat") 
delete_file_or_folder("./dist")
download_file(url, "./temp.zip")
extract_zip("./temp.zip", "./temp")
move_file_or_folder("./temp/wge-main/dist", "./")
move_file_or_folder("./temp/wge-main/requirements.txt", "./requirements.txt")
move_file_or_folder("./temp/wge-main/uninstall.bat", "./uninstall.bat")
move_file_or_folder("./temp/wge-main/WGE-debug.bat", "./WGE-debug.bat")
move_file_or_folder("./temp/wge-main/WGE.bat", "./WGE.bat")
delete_file_or_folder("./temp.zip")
delete_file_or_folder("./temp") 