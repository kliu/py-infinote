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
                
#fails because of empty vector?                
def test_1():
    #We create an initial buffer that consists of one segment by user 0. This is the starting point.
    initial_segment = Segment(0, "abcdefghi")
    initial_buffer = Buffer([initial_segment])
    #abcdefghi
    #print initial_buffer.toString()
    #Now, we create a State object from this so we can manipulate this buffer.
    state = State(initial_buffer)
    #At this moment, the state object is initialized with "abcdefghi" and an empty state vector (because no requests have been executed yet).
    #Now let's suppose user 2 wants to insert some text at position 2. We first create a buffer for the inserted data.
    r1_segment = Segment(2, "ac")
    print 'segment: %s' % r1_segment.toString()
    r1_buffer = Buffer([r1_segment])
    print 'buffer: %s' % r1_buffer.toString()
    #Now we create an operation for this request. Since the user wants to insert text, the Operations.Insert class is what we need.
    r1_operation = Insert(2, r1_buffer) #2 is the insert offset
    print 'operation: %s' % r1_operation.toString()
    #The operation was issued when the document was still at its initial state (i.e. when no other users had issued requests). Therefore, we create an empty state vector.
    
    r1_vector = Vector()
   
    #Finally, we wrap this into a DoRequest object.
    r1 = DoRequest(2, r1_vector, r1_operation)
    print 'dorequest: %s' % r1.toString()
    #print state.canExecute(r1)    
    print 'vector: %s' % state.vector.toString()
    #We now ask the state object to execute this request for us.
    #At this point, the request has been executed and the changes have been applied to the document.
    #print state.vector.toString() #2:1
    #r2_segment = Segment(3, "bc")
    #r2_buffer = Buffer([r2_segment])
    #r2_operation = Insert(3, r2_buffer)
    print state.buffer.toString()


def test_2():
    _state = State()   
    test_text = 'fabreberrb ergber gerg erg rthej '
    example_log = [ ['i', (0,' ', 0, 'foobar foobar bar foo')], ]
    offset = 0
    buffer = Buffer([Segment(2, test_text)])
    print buffer.toString()
    operation = Insert(offset, buffer)
    request = DoRequest(2, r1_vector, operation)
    print _state.execute(request)
    #initial_segment = Segment(0, "abcdefghi")
    #initial_buffer = Buffer([initial_segment])
    #state = State(initial_buffer)
    
test_1()
#editor = InfinoteEditor()
#editor.logs = example_log
#editor.sync()
#print editor._state.buffer.toString()