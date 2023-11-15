*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  arttu  arttu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  aaaaa123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  aaaaa123
    Output Should Contain  Username must be at least 3 characters long and contain only letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ab88  aaaaa123
    Output Should Contain  Username must be at least 3 characters long and contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  abb  aaaaa12
    Output Should Contain  Password needs to be at least 8 characters and contain number or special character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  aaaaaaaa
    Output Should Contain  Password needs to be at least 8 characters and contain number or special character


*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command