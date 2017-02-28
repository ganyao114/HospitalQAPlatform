class PrivateExc(Exception):
    def __init__(self,name):
        print 'par---' + name + '---is private!'

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname]= value

    def __getattribute__(self, item):
        if item in self.privates:
            raise PrivateExc(item, self)
        else:
            return self.__dict__[item]