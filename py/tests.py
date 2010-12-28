import os, sys

WEBUI_ROOT = os.path.dirname(os.path.realpath(__file__))[:-5]
sys.path.append(WEBUI_ROOT)
from infinote import *
    
           
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
    print '\nRequest 1: %s' % executed_r1.toString()
    print ' Vector 1: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 1: %s\n' % state.buffer #this outputs abaccdefghi
    #INSERT
    r2_segment = Segment(3, "bc")
    r2_buffer = Buffer([r2_segment])
    r2_operation = Insert(3, r2_buffer)
    r2_vector = Vector()
    r2 = DoRequest(3, r2_vector, r2_operation)
    executed_r2 = state.execute(r2)
    print 'Request 2: %s' % executed_r2.toString()
    print ' Vector 2: %s' % state.vector.toString() 
    print ' Result 2: %s\n' % state.buffer #this should output "abaccbcdefghi"
    #DELETE 
    r3_operation = Delete(0, 5)
    r3_vector = Vector() 
    r3 = DoRequest(4, r3_vector, r3_operation)
    executed_r3 = state.execute(r3)
    print 'Request 3: %s' % executed_r3.toString()
    print ' Vector 3: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 3: %s\n' % state.buffer #this should output "acbcfghi"
    #UNDO
    r4_vector = Vector() 
    r4 = UndoRequest(4, r4_vector)
    executed_r4 = state.execute(r4)
    print 'Request 4: %s' % executed_r3.toString()
    print ' Vector 4: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 4: %s\n' % state.buffer #this should output "abaccbcdefghi"
    #INSERT
    r5_segment = Segment(5, "BLABLA")
    r5_buffer = Buffer([r5_segment])
    r5_operation = Insert(4, r5_buffer)
    r5_vector = Vector()
    r5 = DoRequest(5, r5_vector, r5_operation)
    executed_r5 = state.execute(r5)
    print 'Request 5: %s' % executed_r5.toString()
    print ' Vector 5: %s' % state.vector.toString() 
    print ' Result 5: %s\n' % state.buffer #this should output "abaccbcdefghi"
    #REDO
    r6_vector = Vector() 
    r6 = UndoRequest(3, r6_vector)
    executed_r6 = state.execute(r6)
    print 'Request 6: %s' % executed_r6.toString()
    print ' Vector 6: %s' % state.vector.toString() #this outputs 2:1
    print ' Result 6: %s\n' % state.buffer #this should output "abaccbcdefghi"
    
test_1()
