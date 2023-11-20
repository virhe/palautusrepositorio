*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testi123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  testi123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  testi123  testi123
    Output Should Contain  Username should consist of only letters

Register With Valid Username And Too Short Password
    Input Credentials  testi  a
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  testitesti
    Output Should Contain  Password needs numbers or special characters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
