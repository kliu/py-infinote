import os, sys

WEBUI_ROOT = os.path.dirname(os.path.realpath(__file__))[:-5]
sys.path.append(WEBUI_ROOT)
from infinote import *

example_log = [ ['i', (0,' ', 0, 'foobar foobar bar foo')], ]

class InfinoteEditor(object):
    
    def __init__(self):
        self.logs = []
        self._state = State()

    def _handleInsert(self, params):
        buffer = Buffer([Segment(params[0], params[3])])
        operation = Insert(params[2], buffer)
        request = DoRequest(params[0], Vector(params[1]), operation)
        executedRequest = self._state.execute(request)
        

    def _handleDelete(self, params):
        buffer = Buffer(Segment(params[2], params[3]))
        request = DoRequest(params[0], Vector(params[1]), operation)
        executedRequest = self._state.execute(request)
        
        
    def _handleUndo(self, params):
        request = UndoRequest(self._localUser, self._state.vector)
        if self._state.canExecute(request):
            executedRequest = self._state.execute(request)
            
            
    def sync(self):
        for log in self.logs:
            if log[0] == 'i':
                self._handleInsert(log[1])
            elif log[0] =='d':
                self._handleDelete(log[1])
            elif log[0] == 'u':
                self._handleUndo(log[1])
                
editor = InfinoteEditor()
editor.logs = example_log
editor.sync()
print editor._state.buffer