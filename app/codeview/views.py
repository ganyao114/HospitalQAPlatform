from flask import request

from app.codeview import codeview
from app.codeview import filemanager
from app.codeview.filemanager import FileManager


@codeview.route(filemanager.base_rul,  methods = ['GET', 'POST'])
def dispatch():
    return filemanager.FileManager.dispatch_request(FileManager('D:\\Android'), request.args)
