from modules.logger import CustomError
from os import path,chdir
import subprocess
from progress.bar import Bar
import colorama

class gt:
    def __init__(self,working_dir, repos_data,logIt):
        self.working_dir    = working_dir
        self.repos_data     = repos_data
        self.logIt          = logIt
        self.cloned_repos   = []

        self._check_repos()

    def _check_repos(self):
        '''
            Check the cloned repos
        '''
        try:
            for repos_name,repos_values in self.repos_data.items():
                if repos_values['cloned'] == True:
                    self.cloned_repos.append(repos_name)
            
            if len(self.cloned_repos) == 0:
                raise CustomError('e','There are no cloned repo to run gitleaks')
            else:
                self._run_gitleaks()
            
        except CustomError as e:
            self.logIt.add_log(e.severity,e.message)
        except Exception as e:
            self.logIt.add_log('c','Error raised while checking cloned repos {}'.format(e))
        
    def _run_gitleaks(self):
        repos_failed = []
        self.logIt.add_log('i','Gitleaks jumps in to check the possible leaked secrets')
        dirname = path.dirname(__file__)
        bar     = Bar('Scanning:',max=len(self.cloned_repos))

        for repo in self.cloned_repos:
            chdir(path.join(self.working_dir,repo))
            bar.next()
            cmd = subprocess.run(['gitleaks','detect','--no-git',self.working_dir,'-c',path.join(dirname,'..','config','gitleaks.toml'),'-r',path.join(self.working_dir,'gitleaks-result-'+repo+'.json'),'-v'],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            if cmd.returncode != 0 and cmd.returncode != 1:
                repos_failed.append(repo)

        bar.finish()

        if len(repos_failed) != 0:
            self.logIt.add_log('w','gitleaks failed to scan ' + len(repos_failed) + 'repositories out of ' + len(self.cloned_repos))
        
        print(colorama.Fore.GREEN + '\u2714 lazyGitleaks done the job, You can find the result and logs in {}'.format(self.working_dir) + colorama.Style.RESET_ALL)

