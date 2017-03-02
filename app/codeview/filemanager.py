# @Authors Swift Gan
# @Org trend_micro
import json
import os
from abc import abstractmethod

#you need to filter it to invoke dispatch_request
import time

base_rul = '/static/connectors/python/filemanager.python'

init_ret = {
    "data": {
        "id": "/",
        "type": "initiate",
        "attributes": {
            "config": {
                "options": {
                    "culture": "zh-cn",
                    'overrideClientConfig':False
                },
                "security": {
                    "allowFolderDownload": True,
                    'editRestrictions': [
                        "txt",
                        "csv",
                        "md",
                        "c",
                        "h",
                        "cpp",
                        "xml",
                        "json",
                        "smali",
                        "java"
                    ]
                },
                "upload": {
                    "chunkSize": 10000000,
                }
            }
        }
    }
}


editfile = {
    "data":{
        "id":"/My_folder/llalalalala/demo.txt",
        "type":"file",
        "attributes":{
            "name":"demo.txt",
            "extension":"txt",
            "path":"/userfiles/My_folder/llalalalala/demo.txt",
            "readable":1,
            "writable":1,
            "created":"",
            "modified":"02 Mar 2017 06:53",
            "timestamp":1488437617,
            "height":0,
            "width":0,
            "size":"8",
            "content":"dawdwdad"
        }
    }
}

getfolder_test = {
    "data": [
        {
            "id": "/logo.png",
            "type": "file",
            "attributes": {
                "name": "logo.png",
                "extension": "png",
                "path": "/rfm/userfiles/logo.png",
                "readable": 1,
                "writable": 1,
                "created": "18 Aug 2016 17:09",
                "modified": "20 Aug 2016 19:21",
                "timestamp": 1471713699,
                "height": 128,
                "width": 128,
                "size": "15664"
            }
        },
        {
            "id": "/audio.mp3",
            "type": "file",
            "attributes": {
                "name": "audio.mp3",
                "extension": "mp3",
                "path": "/rfm/userfiles/audio.mp3",
                "readable": 0,
                "writable": 0,
                "created": "18 Aug 2016 17:09",
                "modified": "20 Aug 2016 19:21",
                "timestamp": 1462441126,
                "height": 0,
                "width": 0,
                "size": "4387104"
            }
        },
        {
            "id": "/images/",
            "type": "folder",
            "attributes": {
                "name": "images",
                "path": "/rfm/userfiles/images/",
                "readable": 1,
                "writable": 1,
                "created": "02 Sep 2016 10:42",
                "modified": "19 Oct 2016 00:24",
                "timestamp": 1476829464
            }
        }
    ]
}

split_path = os.path.split

path_exists = os.path.exists

def check_path(path):
    if path_exists('../'):
        return False
    else:
        return True

def genarate_path(home, path):
    return os.path.abspath(home + path)

def file_extension(name):
    return name.split('.')[-1]

# decorator to filter illegal path
def path_check(pars_name):
    def handle_func(func):
        def handle_args(**kwargs):
            isLegal = True
            for par_name in pars_name:
                if check_path(kwargs[par_name]) == False:
                    isLegal = False
                    break
            if isLegal:
                func(**kwargs)
        return handle_args
    return handle_func


# #for Flask
# class NoCacheReponse(Response):
#
#     def __init__(self, response=None, status=None, headers=None,
#                  mimetype=None, content_type=None, direct_passthrough=False):
#         Response.__init__(self, response, status, headers
#                        , mimetype, content_type, direct_passthrough)
#         # No Cache
#         self.headers.add('Cache-Control', 'no-cache, no-store, must-revalidate') #Http 1.1

def is_writeable(path, check_parent=False):
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        # The path exists and is writeable
        return True
    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        # The path exists and is not writeable
        return False
    # The path does not exists or is not writeable
    if check_parent is False:
        # We're not allowed to check the parent directory of the provided path
        return False
    # Lets get the parent directory of the provided path
    parent_dir = os.path.dirname(path)
    if not os.access(parent_dir, os.F_OK):
        # Parent directory does not exit
        return False
    # Finally, return if we're allowed to write in the parent directory of the
    # provided path
    return os.access(parent_dir, os.W_OK)


def is_readable(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        # The path exists and is readable
        return True
    # The path does not exist
    return False

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


# hal for file sys
class IFileOperator:

    @staticmethod
    def get_operator():
        return CommonFileOperator()

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
    def get_dir_info(self, path):
        pass

    @abstractmethod
    def get_file_info(self, path):
        pass

    @abstractmethod
    def writable(self, path):
        pass

    @abstractmethod
    def readable(self, path):
        pass

    @abstractmethod
    def get_file_size(self, path):
        pass

    @abstractmethod
    def is_dir(self, path):
        pass

    @abstractmethod
    def get_files_in_folder(self, path):
        pass

    @abstractmethod
    def read_doc(self, path):
        pass

class CommonFileOperator(IFileOperator):

    def readable(self, path):
        return is_readable(path)

    def get_file(self, path):
        file = None
        try:
            file = open(path)
        except IOError as e:
            print e
        return file

    def copy_file(self, path_from, path_to):
        pass

    def del_file(self, path):
        pass

    def move_file(self, path_from, path_to):
        pass

    def mkdir(self, path, dir_name):
        pass

    def get_dir_info(self, path):
        try:
            return {
                'id': '/' + os.path.basename(path) + '/',
                'type': 'folder',
                'attributes': {
                    'name':os.path.basename(path),
                    'path': None, # can not ret real path
                    'readable': 1 if self.readable(path) else 0,
                    'writable': 1 if self.writable(path) else 0,
                    'created': time.ctime(os.path.getctime(path)),
                    'modified': time.ctime(os.path.getmtime(path)),
                    'timestamp': int(os.path.getctime(path)),
                }
            }
        except Exception as e:
            print e
        return None

    def is_dir(self, path):
        try:
            return os.path.isdir(path)
        except:
            return None

    def get_files_in_folder(self, path):
        try:
            paths = []
            for filename in os.listdir(path):
                paths.append(os.path.join(path, filename).decode('gbk'))
            return paths
        except:
            return None

    def get_file_info(self, path):
        try:
            return {
                'id':'/' + os.path.basename(path),
                'type':'file',
                'attributes': {
                    'name':os.path.basename(path),
                    'extension': file_extension(os.path.basename(path)),
                    'path': None, # can not ret real path
                    'readable': 1 if self.readable(path) else 0,
                    'writable': 1 if self.writable(path) else 0,
                    'created': time.ctime(os.path.getctime(path)),
                    'modified': time.ctime(os.path.getmtime(path)),
                    'timestamp': int(os.path.getctime(path)),
                    'height': 0,
                    'width': 0,
                    'size': self.get_file_size(path)
                }
            }
        except Exception as e:
            print e
        return None

    def read_doc(self, path):
        with self.get_file(path) as file:
            return file.read()

    def writable(self, path):
        return is_writeable(path, True)

    def readable(self, path):
        return is_readable(path)

    def get_file_size(self, path):
        try:
            return os.path.getsize(path)
        except:
            return None

class FileManager(IFileManager):

    private_path = None
    file_operator = None
    IconDirectory = './images/fileicons/'
    imgExtensions = [".jpg", ".png", ".jpeg", ".gif", ".bmp"]

    def __init__(self, url):
        self.private_path = url;
        self.file_operator = IFileOperator.get_operator()
        pass

    def initiate(self):
        return json.dumps(init_ret)

    def getfolder(self, path):
        if path[-1:] == '/':
            path = path[:-1]
        folder_path = genarate_path(self.private_path, path)
        file_infos = []
        isdir = self.file_operator.is_dir(folder_path)
        if isdir == None:
            pass
        elif isdir:
            file_paths = self.file_operator.get_files_in_folder(folder_path)
            if file_paths != None:
                for file_path in file_paths:
                    if not self.file_operator.is_dir(file_path):
                        file_info = self.file_operator.get_file_info(file_path)
                        if file_info != None:
                            file_info['attributes']['path'] = path + file_info['id']
                            file_info['id'] = file_info['attributes']['path']
                            file_infos.append(file_info)
                    else:
                        folder_info = self.file_operator.get_dir_info(file_path)
                        if folder_info != None:
                            folder_info['attributes']['path'] = path + folder_info['id']
                            folder_info['id'] = folder_info['attributes']['path']
                            file_infos.append(folder_info)
                return json.dumps({'data': file_infos})
        return json.dumps({'data': ''})
    def rename(self, old_path, new_path):
        pass

    def readfile(self, path):
        if path[-1:] == '/':
            path = path[:-1]
        file_path = genarate_path(self.private_path, path)
        content = self.file_operator.read_doc(file_path)
        file_info = self.file_operator.get_file_info(file_path)
        if file_info != None:
            file_info['attributes']['path'] = path + file_info['id']
            file_info['id'] = file_info['attributes']['path']
            file_info['attributes']['content'] = content
            return json.dumps({'data': file_info})


    @staticmethod
    def dispatch_request(filemanager, pars):
        mode = pars['mode']
        if mode != None:
            if mode == 'initiate':
                return filemanager.initiate()
            elif mode == 'getfolder':
                return filemanager.getfolder(pars['path'])
            elif mode == 'rename':
                return filemanager.rename(pars['old'], pars['new'])
            elif mode == 'editfile':
                return filemanager.readfile(pars['path'])
            else:
                pass



def get_dir_info(path):
    pass

def get_file_info(path):
    pass




def disable_cache():
    pass