<h1 align="center">lazyGitleaks</h1>
<p align="center">Find juicy secrets in the repositories</p>
<p align="center">lazyGitleaks is a python script clone and scan the repositories to find hard-coded secrets</p>

<details open="open">
<summary>Table of Contents</summary>
  <ol>
    <li><a href="#screen">Screenshot</a></li>
    <li><a href="#Disclaimer">Disclaimer</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#results-and-discussion">Results and FQAs</a></li>
    <li><a href="#to-do">To-Do</a></li>
  </ol>
</details>

<h2 id="screen"> :clapper: Screenshot</h2>
<p align="center"> 
  <img src="assets/img/screenshot.png">
</p>

```sh

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

                lazyGitleaks ver. 0.1 Beta | Developed by @bassammaged <kemet>

  Do you interested in finding secrets? Are you depending on gitleaks tool? Do you usually preform
  large scan scale against different repositories? No worries. lazyGitleaks comes to automate the scan
  and use custom .toml template to find the juicy secrets are living in repositories.

usage: lazyGitleaks.py [-h] -p PLATFORM -t TARGET [-a] [-o] [-v]

required arguments:
  -p PLATFORM, --platform PLATFORM
                        Specify the version control platform [github, gitlab]
  -t TARGET, --target TARGET
                        Provide the targeted account name

optional arguments:
  -h, --help            show this help message and exit
  -a, --auth            By providing the flag the scan will be run with authentication mechanism.
  -o, --org             By providing the flag the target will classified as organization account.
  -v, --verbose         Allows the script to print out the message level start with debug.
```

<h2 id="Disclaimer"> :pencil: Disclaimer</h2>

`lazyGitleaks` is in beta version and is supposed to be free of issues but if any issues are encountered, please submit the ticket,lazyGitleaks is coded and published to be used in particular circumstances:

1. Engaging in penetration testing activity.
2. Carry on a Bug hunting activity.
3. Source code review.
4. Any other legal activity that is already approved by the owner of the asset.

`lazyGitleaks` is created to work with all version control, which means there are many version control that will be supported soon.
 
<h2 id="Features"> :fuelpump: Features</h2>

- [x] `lazyGitleaks` supports GitHub.
- [ ] `lazyGitleaks` supports GitLab.
- [x] `lazyGitleaks` uses an environment variable for storing Credentials.
- [x] `lazyGitleaks` perform GitHub API calls and clone all available repositories.
- [x] `lazyGitleaks` supports authenticated [public & private repositories] and non-authenticated [public repositories].
- [x] `lazyGitleaks` monitors the GitHub API limitation and the script detects the required time to postpone the job.
- [x] `lazyGitleaks` has its unique `gitleaks.toml` that helps to find more secrets.
- [ ] `lazyGitleaks` supports pause & continue.


>**Warning** <br>
>Authenticated scan it's run without issues when the target account is an organization that you are a member of or the provided github PAT is belong to the same target account.


<h2 id="prerequisites"> :cd: Prerequisites</h2>

1. Python3
2. `pip` package manager
3. `python3 -m pip install requirements.txt`
4. Feel Free to use `lazyGitleaks` via `lazyGitleaks.py` script

> **Note** <br>
> Github credendtial has to provided through enviornment variables as the following: <br>
> `LG_GITHUB_TOKEN="<github_username>:<github_pat>"`

<h2 id="results-and-discussion"> :paperclip: Results and FQAs</h2>

```json
[
 {
  "Description": "AWS Manager ID",
  "StartLine": 139,
  "EndLine": 139,
  "StartColumn": 21,
  "EndColumn": 40,
  "Match": "AIPAIK7LV6U6UXJXQQR3",
  "Secret": "AIPA",
  "File": "README.md",
  "Commit": "",
  "Entropy": 1.5,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "access-key",
   "aws",
   "cloud"
  ],
  "RuleID": "aws-manager-id"
 }
]
```

```json
[
 {
  "Description": "GitHub Personal Access Token",
  "StartLine": 50,
  "EndLine": 50,
  "StartColumn": 150,
  "EndColumn": 189,
  "Match": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "Secret": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.5153117,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "pat-key",
   "github",
   "version-control"
  ],
  "RuleID": "github-pat"
 },
 {
  "Description": "GitHub Personal Access Token",
  "StartLine": 59,
  "EndLine": 59,
  "StartColumn": 147,
  "EndColumn": 186,
  "Match": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "Secret": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.5153117,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "pat-key",
   "github",
   "version-control"
  ],
  "RuleID": "github-pat"
 },
 {
  "Description": "GitHub Personal Access Token",
  "StartLine": 59,
  "EndLine": 59,
  "StartColumn": 224,
  "EndColumn": 263,
  "Match": "ghp_8zrErw6PvpPWaoPepQLN19sXLeAOSH06Zx1M",
  "Secret": "ghp_8zrErw6PvpPWaoPepQLN19sXLeAOSH06Zx1M",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.8341837,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "pat-key",
   "github",
   "version-control"
  ],
  "RuleID": "github-pat"
 },
 {
  "Description": "GitHub Personal Access Token",
  "StartLine": 63,
  "EndLine": 63,
  "StartColumn": 37,
  "EndColumn": 76,
  "Match": "ghp_8zrErw6PvpPWaoPepQLN19sXLeAOSH06Zx1M",
  "Secret": "ghp_8zrErw6PvpPWaoPepQLN19sXLeAOSH06Zx1M",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.8341837,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "pat-key",
   "github",
   "version-control"
  ],
  "RuleID": "github-pat"
 },
 {
  "Description": "AirBrake API",
  "StartLine": 98,
  "EndLine": 98,
  "StartColumn": 13,
  "EndColumn": 62,
  "Match": "\"AIRBRAKE_KEY: 'cae7f5949eaf243d0cccfa1329f092d8'\"",
  "Secret": "\"AIRBRAKE_KEY: 'cae7f5949eaf243d0cccfa1329f092d8'\"",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.533661,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "api-key",
   "airbrake",
   "app monitor"
  ],
  "RuleID": "airbrake-api"
 },
 {
  "Description": "AirBrake API",
  "StartLine": 99,
  "EndLine": 99,
  "StartColumn": 14,
  "EndColumn": 63,
  "Match": "\"AIRBRAKE_KEY: 'cae7f5949eaf243d0cccfa1329f092d8'\"",
  "Secret": "\"AIRBRAKE_KEY: 'cae7f5949eaf243d0cccfa1329f092d8'\"",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 4.533661,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "api-key",
   "airbrake",
   "app monitor"
  ],
  "RuleID": "airbrake-api"
 },
 {
  "Description": "AirBrake project key",
  "StartLine": 120,
  "EndLine": 120,
  "StartColumn": 13,
  "EndColumn": 33,
  "Match": "\"AIRBRAKE_ID: 179755\"",
  "Secret": "\"AIRBRAKE_ID: 179755\"",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 3.8208888,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "project-id",
   "airbrake",
   "app monitor"
  ],
  "RuleID": "airbrake-project-key"
 },
 {
  "Description": "AirBrake project key",
  "StartLine": 121,
  "EndLine": 121,
  "StartColumn": 14,
  "EndColumn": 34,
  "Match": "\"AIRBRAKE_ID: 179755\"",
  "Secret": "\"AIRBRAKE_ID: 179755\"",
  "File": "apps/third_eye/lazy_gitleaks/README.md",
  "Commit": "",
  "Entropy": 3.8208888,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "project-id",
   "airbrake",
   "app monitor"
  ],
  "RuleID": "airbrake-project-key"
 },
 {
  "Description": "GitHub Personal Access Token",
  "StartLine": 71,
  "EndLine": 71,
  "StartColumn": 171,
  "EndColumn": 210,
  "Match": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "Secret": "ghp_A5COGOVYUGnhYWILWawMfjpAAeeVeC5no94V",
  "File": "apps/third_eye/lazy_gitleaks/run.py",
  "Commit": "",
  "Entropy": 4.5153117,
  "Author": "",
  "Email": "",
  "Date": "",
  "Message": "",
  "Tags": [
   "pat-key",
   "github",
   "version-control"
  ],
  "RuleID": "github-pat"
 }
]
```

<h2 id="to-do"> :paperclip: To-Do</h2>

- [x] Support pause & continue. 
- [ ] Support gitlab. 
