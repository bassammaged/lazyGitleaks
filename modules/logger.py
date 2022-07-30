from os import path,mkdir
from shutil import rmtree
from sys import exit
import logging,colorama

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

    def __init__(self,initiateState,platform,target,verbose):
        self.initiateState      = initiateState
        self.platform           = platform
        self.target             = target
        self.verbose            = verbose
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

    def add_log(self,severity,message):
        '''
            add() is written to log the msg and severity of msg.
            Arguments:
                criticality_level: determine the level of log.
                - `d` for debug.
                - `i` for informative.
                - `w` for warning.
                - `e` for error.
                - `c` for critical.
                
                message: it holds the message that you want to log.
            Process:
                - logging the error message and level of criticality.
                - if the level of criticality is `c` or `e`, the script will be terminated.
        '''
        filename = path.join(self.working_dir,'debug.log')
        # logging.basicConfig(filename=filename,encoding='utf-8',level=logging.DEBUG,format="%(levelname)s|%(asctime)s|%(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(handlers=[logging.FileHandler(filename=filename, 
                                                 encoding='utf-8', mode='a+')],level=logging.DEBUG,format="%(levelname)s|%(asctime)s|%(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')
        if severity == 'd':
            logging.debug(message)
        elif severity == 'w':
            logging.warning(message)
        elif severity == 'e':
            logging.error(message)
        elif severity == 'c':
            logging.critical(message)
        else:
            logging.info(message)

        # -- Checking the verbosity
        self._verbose(severity,message)

        # -- terminate the script in error neither critical
        if severity == 'c' or severity == 'e':
            terminator()

    def _verbose(self,severity,message):
        '''
            _verbose() checks the verbosity status and print out the colored message if verbose was enabled.
        '''
        if self.verbose:
            sign = '\u0021'
            color = colorama.Fore.LIGHTBLUE_EX
            if severity == 'd':
                sign = '>'
                color = colorama.Fore.LIGHTCYAN_EX
            if severity == 'w':
                sign = '\u2622'
                color = colorama.Fore.YELLOW
            elif severity == 'e':
                sign = '\u2718'
                color = colorama.Fore.LIGHTRED_EX
            elif severity == 'c':
                sign = '\u2718'
                color = colorama.Fore.RED
            elif severity == 'f':
                sign = '\u2714'
                color = colorama.Fore.GREEN

            print(color + '[' + sign + '] ' + message + colorama.Style.RESET_ALL)


class terminator:
    '''
        terminator class is written to be used by `log_it` class to terminate the script incase of the level of logging is `c` either `e`.
    '''
    def __init__(self):
        exit()
    

