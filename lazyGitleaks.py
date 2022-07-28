from modules.userInputs import inputs

def banner():
    '''
    banner() is a function designed to show the tool name, version and short description.
    '''
    tool_banner = '''
    
 ██▓    ▄▄▄      ▒███████▒▓██   ██▓     ▄████  ██▓▄▄▄█████▓ ██▓    ▓█████ ▄▄▄       ██ ▄█▀  ██████ 
▓██▒   ▒████▄    ▒ ▒ ▒ ▄▀░ ▒██  ██▒    ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▓██▒    ▓█   ▀▒████▄     ██▄█▒ ▒██    ▒ 
▒██░   ▒██  ▀█▄  ░ ▒ ▄▀▒░   ▒██ ██░   ▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▒██░    ▒███  ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
▒██░   ░██▄▄▄▄██   ▄▀▒   ░  ░ ▐██▓░   ░▓█  ██▓░██░░ ▓██▓ ░ ▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
░██████▒▓█   ▓██▒▒███████▒  ░ ██▒▓░   ░▒▓███▀▒░██░  ▒██▒ ░ ░██████▒░▒████▒▓█   ▓██▒▒██▒ █▄▒██████▒▒
░ ▒░▓  ░▒▒   ▓▒█░░▒▒ ▓░▒░▒   ██▒▒▒     ░▒   ▒ ░▓    ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░ ░ ▒  ░ ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▓██ ░▒░      ░   ░  ▒ ░    ░    ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
  ░ ░    ░   ▒   ░ ░ ░ ░ ░ ▒ ▒ ░░     ░ ░   ░  ▒ ░  ░        ░ ░      ░    ░   ▒   ░ ░░ ░ ░  ░  ░  
    ░  ░     ░  ░  ░ ░     ░ ░              ░  ░               ░  ░   ░  ░     ░  ░░  ░         ░  
                 ░         ░ ░                                                                     
    '''

    description     = '''
  Do you interested in finding secrets? Are you depending on gitleaks tool? Do you usually preform 
  large scan scale against different repositories? No worries. lazyGitleaks comes to automate the scan 
  and use custom .toml template to find the juicy secrets are living in repositories.
    '''

    version         = '''
                lazyGitleaks ver. 0.1 Beta | Developed by @bassammaged <kemet>
'''

    print(tool_banner,version,description)


def main():
    banner()
    inputs()


if __name__ == "__main__":
    main()