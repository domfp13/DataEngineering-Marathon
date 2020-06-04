
import main

def test():
    """Simulates how the event will flow
    """
    main.marathon_execution({'name':'marathon/Marathon-SQ-MPC003-Productivity.xlsx', 
                            'bucket':'app-dataengineering'}, 'This is super fun')

test()
