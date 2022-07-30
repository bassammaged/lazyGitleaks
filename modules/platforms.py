from tabnanny import check
import requests,base64,datetime
from progress.bar import Bar
from time import sleep
from modules.logger import CustomError,terminator,logIt

class platform:
    '''
        platform class is designed to handle the data that will be common between the supported platforms.
    '''
    def __init__(self,args,auth_token):
        # Initiate the logs for the target
        self.logIt = logIt(True,args.platform,args.target,args.verbose)
        # Call the platform
        if args.platform == 'github':   # github platform
            self.logIt.add_log('i','The github class has been imported.')
            github(args,auth_token,self.logIt)

        



class github:
    '''
        github class is designed to manage the all API calls to github.
    '''
    def __init__(self,args,auth_token,logIt):
        self.args       = args
        self.auth_token = auth_token
        self.logIt      = logIt
        self.repos_data = {}
        self._set_endpoints()
        
    
    def _set_endpoints(self):
        '''
        _set_endpoints() is started with _ because its private function and it's designed to identify the github end-points
        will be used for the requests.
        '''
        if self.args.org == True:
            self.endpoint   = 'https://api.github.com/orgs/'+self.args.target+'/repos'
        elif self.args.org == False:
            if self.auth_token == None:
                 self.endpoint   = 'https://api.github.com/users/' + self.args.target + '/repos'
            else:
                self.endpoint   = 'https://api.github.com/user/repos' 

        self._send_github_requests()
    
    def _send_github_requests(self):
        '''
            _send_github_repo_requests(): is started with _ because its private function and it's designed to send a request to github based on repos_win_back()
            the return data will be handled by repos_win_back() as well.
        '''
        check_loop_status = True
        page_no = 1
        connection_tries = 0
        self.logIt.add_log('i','Retrieving repositories information...')
        while check_loop_status:    # iterate to retrieve all pages.
            try:
                if self.auth_token == None:   # With no authentication
                    req = requests.get(self.endpoint,params={"type":"all","per_page":"100","page":page_no})
                else:                   # With authentication
                    auth_token = base64.b64encode(self.auth_token.encode('ascii')).decode('ascii')
                    req = requests.get(self.endpoint,headers={"authorization":"Basic "+auth_token},params={"type":"all","per_page":"100","page":page_no})

                # -- Check the rate limitation
                check_ratelimit = self._monitor_github_limit(int(req.headers['X-RateLimit-Remaining']),int(req.headers['X-RateLimit-Reset']))
                if check_ratelimit == False: # within the limitation
                    data = req.json()
                    if req.status_code == 200 and len(data) != 0:   # There are repos's information in the body
                        for repo_data in data:
                            self.repos_data[repo_data['name']] = {"clone_url":repo_data['clone_url'],"private":repo_data['private'],"cloned":False}
                    elif req.status_code == 200 and len(data) == 0: # there are no more repo's information in the body
                        self.logIt.add_log('i','Repositories information already collected; No. of repos {}'.format(len(self.repos_data)))
                        # self._repo_win_back(first_repo_win_back_run=True)
                        print(self.repos_data)
                        check_loop_status = False
                    elif req.status_code == 401:
                        self.logIt.add_log('e','The provided credential is incorrect')
                    page_no = page_no + 1
            # If the connection to github API is failed the script will send 9 more tries
            except Exception as e:
                if connection_tries == 10:
                    self.logIt.add_log('e','Error occurred while checking the repositories via github. Error message: {}'.format(e))
                else:
                    self.logIt.add_log('w','Failed to retrieve the repositories. Error message: {}'.format(e))
                    sleep(10)
                    connection_tries = connection_tries + 1
                    self.logIt.add_log('w','Re-send the request to github API! No of tries: {}'.format(connection_tries)) 


    def _monitor_github_limit(self,ratelimit_remain,ratelimit_reset):
        '''
        _   monitor_github_limit() monitor the github limitation and stop the script process till github limitation is reset.
        '''
        if (ratelimit_remain <= 1):
            current_time = int(datetime.datetime.now().timestamp())
            waiting_time = (ratelimit_reset - current_time) + 120
            print('\u2622 Github limitation is exceeded, script will proceed the requests after ' + str(waiting_time/60) + ' minutes.')
            bar = Bar('Seconds passed:',max=waiting_time)
            for _ in range(1,waiting_time+1):
                sleep(1)
                bar.next()
            bar.finish()
        return False
    
    

class gitlab:
    pass