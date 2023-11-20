*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Click Login Link
    Go To Starting Page
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Go To Starting Page
    Click Link  Register new user
    Register Page Should Be Open