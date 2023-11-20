*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  testib
    Set Password  testitesti
    Set Password Confirmation  testitesti
    Submit Credentials
    Register Should Fail With Message  Password needs numbers or special characters


Register With Nonmatching Password And Password Confirmation
    Set Username  testic
    Set Password  testi123
    Set Password Confirmation  testi124353
    Submit Credentials
    Register Should Fail With Message  Password and confirmation password don't match

Login After Successful Registration
    Set Username  testid
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  testid
    Set Password  testi123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  testie
    Set Password  testi
    Set Password Confirmation  testi
    Submit Credentials
    Register Should Fail With Message  Password is too short
    Go To Login Page
    Login Page Should Be Open
    Set Username  testie
    Set Password  testi
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open
    
Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

