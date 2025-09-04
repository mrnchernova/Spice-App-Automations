# Actions-App-Automations

## RUN
**clone project**

### set up venv
**create new virtual environment**
> python -m venv venv
> 
> py -m venv venv
> 
> python3 -m venv venv

**Select virtual environment for use in current project**
<img width="756" height="308" alt="img" src="https://github.com/user-attachments/assets/91c9e5fc-90a1-48ad-b983-a5c2b5b46068" />

<img width="1020" height="676" alt="img_1" src="https://github.com/user-attachments/assets/d72561d4-10bf-411c-8023-e1b5ac6fea06" />

**transfer to virtual environment**
 <img width="822" height="271" alt="img_2" src="https://github.com/user-attachments/assets/f6cf083d-10f2-4c76-a2d3-bf555642b31f" />

if something like that 
<img width="1024" height="423" alt="img_3" src="https://github.com/user-attachments/assets/309f65a7-c447-4519-b890-a46ab77237bd" />

**go to PowerShell as Administrator**

> Set-ExecutionPolicy RemoteSigned
 
> A
 
**Create New Tab again**


## Install
> pip install pytest-playwright

> playwright install


## Requirements
**get list of installed tools**
> pip list

**Generate a list of all Python packages currently installed in the active virtual environment (or in the global Python environment) and save the list to the requirements.txt file**
> pip freeze > requirements.txt

**Install all Python packages listed in the file**
> pip install -r requirements.txt

```
# (------------test_first.py----------)
from playwright.sync_api import Page, expect

def test_wiki2(page:Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('From today\'s featured article')).to_be_visible()
    page.get_by_role('link', name='Talk').click()
    expect(page.locator('#talkheader')).to_contain_text('Welcome! This page is for discussing the contents of the English Wikipedia\'s Main Page.')
```

