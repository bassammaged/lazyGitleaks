import argparse
from modules.logger import terminator,CustomError
import colorama
from os import path,environ

class inputs:
    '''
        class inputs() is handling the inputs that have to be provided by the user, additional to verify those input as well.
    '''

    def __init__(self):
        self._define_platforms()
        self._take_inputs()
        self._input_checks()

    def _take_inputs(self):
        parse       = argparse.ArgumentParser()
        optional    = parse._action_groups.pop()
        require     = parse.add_argument_group('required arguments')

        require.add_argument('-p','--platform',required=True,help="Specify the version control platform [github, gitlab]", type=str)
        require.add_argument('-t','--target',required=True,help="Provide the targeted account name",type=str)
        optional.add_argument('-a','--auth',help="By providing the flag the scan will be run with authentication mechanism.",default=False,action="store_true") 

        parse._action_groups.append(optional)
        self.args = parse.parse_args()


    def _input_checks(self):
        '''
            _input_checks(): is coded to check the all inputs are matching with the requirement of the script
        '''
        try:
            # ------ Checking the platform
            if self.args.platform not in self.supported_platforms:
                raise CustomError('e','The platform isn\'t listed in supported version control platform')
            
            # ------ Checking the auth
            if self.args.auth == True:
                env = 'LG_' + self.args.platform.upper() + '_TOKEN'
                auth = environ.get(env)
                if auth == None:
                    raise CustomError('e','the {} isn\'t exist in the environment variables or has None value'.format(env))
            
        except CustomError as e:
            print(colorama.Fore.LIGHTRED_EX  + '\u2718 ' + e.message + colorama.Style.RESET_ALL)
            terminator()
        except Exception as e:
            print(colorama.Fore.RED  + '\u2718 ' + e + colorama.Style.RESET_ALL)
            terminator()


    def _define_platforms(self):
        '''
            _define_platforms() is check the platforms are supported by the tool and create self.supported_platforms variable.
        '''
        import json
        with open(path.join(path.dirname(__file__),'..','config','platforms.json')) as f:
                self.supported_platforms = json.load(f)
        
