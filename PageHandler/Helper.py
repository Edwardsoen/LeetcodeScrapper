import os
import json 


class PathManager(): 
    def __init__(self) -> None:
        self.path = os.getcwd()
        self.target_path = self.create_parent_folder()

    def create_parent_folder(self): 
        folder_name = "Leetcode Scrapper Output"
        target_path = os.path.join(os.curdir , folder_name)
        try: 
            os.mkdir(target_path)   
        except FileExistsError: 
            pass
        return target_path

    def get_path(self): 
        return self.target_path

    def create_folder(self, name): 
        end_path = os.path.join(self.target_path, name)
        try: 
            os.mkdir(end_path)
        except FileExistsError as e: 
            pass
        return end_path

    def create_status_log(self): 
        pass

PATH_MANAGER = PathManager()

def log_data(data, folder_name, file_name): 
    file_name += ".json"
    folder = PATH_MANAGER.create_folder(folder_name)
    with open(os.path.join(folder,file_name), "w") as f: 
        json.dump(data, f)
    

class NoCredentialsError(Exception): 
    def __init__(self, url):
        self.message = f"The page {url} require login but login credentials not passed"
        super().__init__(self.message)

