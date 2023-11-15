*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Login Link
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***
Login Page Should Be Open
    Go To Login Page

Register Page Should Be Open
    Go To Register Page