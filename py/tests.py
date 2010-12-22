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
        print self._state.canExecute(request)
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
                
           
def test_1():
    initial_segment = Segment(0, "abcdefghi")
    initial_buffer = Buffer([initial_segment])
    state = State(initial_buffer)
    r1_segment = Segment(2, "ac")
    r1_buffer = Buffer([r1_segment])
    r1_operation = Insert(2, r1_buffer) 
    r1_vector = Vector()
    r1 = DoRequest(2, r1_vector, r1_operation)
    executed_r1 = state.execute(r1) 
    print 'Request 1: %s' % executed_r1.toString()
    print ' Vector 1: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 1: %s\n' % state.buffer #this outputs abaccdefghi
    #so far so good
    r2_segment = Segment(3, "bc")
    r2_buffer = Buffer([r2_segment])
    r2_operation = Insert(3, r2_buffer)
    r2_vector = Vector()
    r2 = DoRequest(3, r2_vector, r2_operation)
    executed_r2 = state.execute(r2)
    print 'Request 2: %s' % executed_r2.toString()
    print ' Vector 2: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 2: %s' % state.buffer #this should output "abaccbcdefghi"
    #aba-bc-ccdefghi offset 3


    
test_1()
