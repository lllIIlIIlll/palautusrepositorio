*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  arttu
    Set Password  kalle123
    Set PasswordC  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  kalle123
    Set PasswordC  kalle123
    Submit Credentials
    Page Should Contain  Username must be at least 3 characters long and contain only letters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  aaaa
    Set Password  kalleaaa
    Set PasswordC  kalleaaa
    Submit Credentials
    Page Should Contain  Password needs to be at least 8 characters and contain number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  aaaa
    Set Password  aa123456
    Set PasswordC  aa654321
    Submit Credentials
    Page Should Contain  Passwords don't match

Login After Successful Registration
    Set Username  aaaa
    Set Password  aa123456
    Set PasswordC  aa123456
    Submit Credentials
    Successful Login
    Logout
    Set Username  aaaa
    Set Password  aa123456
    Login
    Login Should Succeed

Login After Failed Registration
    Set Username  a
    Set Password  aa123456
    Set PasswordC  aa123456
    Submit Credentials
    Registration Failed
    Set Username  a
    Set Password  aa123456
    Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordC
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Login
    Click Button  Login

Logout
    Click Button  Logout

Successful Login
    Go To Logged In Page

Login Should Succeed
    Main Page Should Be Open

Registration Should Succeed
    Logged In Should Be Open

Registration Failed
    Go To Login Page