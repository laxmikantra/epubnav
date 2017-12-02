from opflib.opflib import OPFProcessor
from itertools import tee
    
class OPFNavigator(object):
    
    def __init__ (self, opf):
        self.opf = OPFProcessor(opf)
        self.pages = list(self.opf.pages())
        self.index = 0

    def __iter__ (self):
        return self

    def __next__ (self):
        try:
            item = self.pages[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def prev(self):
        try:
            item = self.pages[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item
    
    def current(self, obj=None):
        return self.pages[self.index]
    
    def first(self):
        return self.pages[0]   
    
    def last(self):
        return self.pages[-1]   

    # search by label seq 
    def search(self, page_id):
      for i in self.pages:
          if i[0] == page_id:
             return i

opf = "/home/sofycomps/work/input/accessible_epub/EPUB/package.opf"
if __name__ == "__main__":
    e = OPFNavigator(opf)
    import pdb; pdb.set_trace()