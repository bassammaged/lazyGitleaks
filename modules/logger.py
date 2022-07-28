from os import path,mkdir
from shutil import rmtree
from sys import exit

class CustomError(Exception):
    '''
        Exception raise for error in the script.
        
        Arguments:
            - message: holds the error message
            - criticality_level: takes level of the error. 
            
        Returns:
            No returns.
    '''

    def __init__(self,severity,message):
        '''
        Exception raise for error in the script.
        
        Arguments:
            - message: holds the error message
            - severity: takes level of the error. 
            
        Returns:
            No returns.
    '''
        self.severity   = severity
        self.message    = message

class logIt:
    '''
        logIt class is created to log the actions and their severities as well.
        
        Arguments:
            - message: holds the error message
            Need to be updated.
            
        Returns:
            No returns.
        Process:
            - logging the error message and level of criticality.
            - if the level of criticality is `c` or `e`, the script will be terminated.
    '''

    def __init__(self,initiateState,platform,target):
        self.initiateState     = initiateState;
        self.platform           = platform;
        self.target             = target;
        self.working_dir        = path.join(path.dirname(__file__),'..','logs',self.platform + '-' + self.target)


        # clear the old logs will be erase if initiateState = True 
        if self.initiateState == True:
            self._clear_the_logs()
            self._create_target_logs_container()


    def _clear_the_logs(self):
        '''
            _clear_the_logs() is method to clear the *.log file that related to the target.
        '''
        try:
            rmtree(path.join(self.working_dir))
        except Exception as e:
            pass
            
    def _create_target_logs_container(self):
        '''
            _create_target_logs_container() for creating the main logs work directory. 
        '''
        try:
            mkdir(path.join(self.working_dir))
        except Exception as e:
            print("ERROR! {}".format(e))


class terminator:
    '''
        terminator class is written to be used by `log_it` class to terminate the script incase of the level of logging is `c` either `e`.
    '''
    def __init__(self):
        exit()
    

