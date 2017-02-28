# @Authors Swift Gan
# @Org trend_micro
import json
import os
from abc import abstractmethod

from Flask import Response

#you need to filter it to invoke dispatch_request
base_rul = '/RichFilemanager/connectors/python/filemanager.python'

init_ret = {
    "data": {
        "id": "/",
        "type": "initiate",
        "attributes": {
            "config": {
                "options": {
                    "culture": "ru",
                },
                "security": {
                    "allowFolderDownload": True,
                },
                "upload": {
                    "chunkSize": 10000000,
                }
            }
        }
    }
}

def check_path(path):
    return True

def genarate_path(home, path):
    return os.path.abspath(home + path)

# decorator to filter illegal path
def path_check(pars_name):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            isLegal = True
            for par_name in pars_name:
                if check_path(kwargs[par_name]) == False:
                    isLegal = False
                    break
            if isLegal:
                func(*args, **kwargs)
        return handle_args
    return handle_func


#for Flask
class NoCacheReponse(Response):

    def __init__(self, response=None, status=None, headers=None,
                 mimetype=None, content_type=None, direct_passthrough=False):
        Response.__init__(self, response, status, headers
                       , mimetype, content_type, direct_passthrough)
        # No Cache
        self.headers.add('Cache-Control', 'no-cache, no-store, must-revalidate') #Http 1.1


class IFileManager:
    @abstractmethod
    def initiate(self):
        pass

    @abstractmethod
    def getfolder(self, path):
        pass

    @abstractmethod
    def rename(self, old_path, new_path):
        pass



class IFileOperate:

    @abstractmethod
    def get_file(self, path):
        pass

    @abstractmethod
    def copy_file(self, path_from, path_to):
        pass

    @abstractmethod
    def del_file(self, path):
        pass

    @abstractmethod
    def move_file(self, path_from, path_to):
        pass

    @abstractmethod
    def mkdir(self, path, dir_name):
        pass

    @abstractmethod
    def get_dir_info(path):
        pass

    @abstractmethod
    def get_file_info(path):
        pass

class FileManager(IFileManager):

    private_url = None;
    IconDirectory = './images/fileicons/'
    imgExtensions = [".jpg", ".png", ".jpeg", ".gif", ".bmp"]

    def __init__(self, url):
        self.private_url = url;
        pass

    def initiate(self):
        return json.dump(init_ret)

    def getfolder(self, path):
        pass

    def rename(self, old_path, new_path):
        pass

    @staticmethod
    def dispatch_request(filemanager, pars):
        filemanager.private_url
        mode = pars['mode']
        if mode != None:
            if mode == 'initiate':
                return filemanager.initiate()
            elif mode == 'getfolder':
                return filemanager.getfolder(pars['path'])
            elif mode == 'rename':
                return filemanager.rename(pars['old'], pars['new'])
            else:
                pass



def get_dir_info(path):
    pass

def get_file_info(path):
    pass




def disable_cache():
    pass