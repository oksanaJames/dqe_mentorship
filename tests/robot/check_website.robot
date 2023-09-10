*** Settings ***
Documentation   This suite contains tests cases for webpage elements validation
Library   SeleniumLibrary
Variables   variables.py


*** Test Cases ***
Header localization test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${COOKIE_BUTTON}
    Click Element    ${COOKIE_BUTTON}
    Switch Window    ${PAGE_TITLE}
    Log To Console  \n
    Element Text Should Be    ${LANGUAGE_LOCATOR}   (EN)
    FOR    ${locator}    IN    @{MENU_LOCATORS}
        Log To Console  Checking ${locator}
        Page Should Contain Link    ${locator}
    END
    Close Browser

'About' link navigation test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${COOKIE_BUTTON}
    Click Element    ${COOKIE_BUTTON}
    Switch Window    ${PAGE_TITLE}
    Log To Console  \nNavigating to ${ABOUT_LOCATOR}
    Click Link    ${ABOUT_LOCATOR}
    Location Should Be    ${ABOUT_URL}
    Close Browser


Search appearance word 'Python' test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${COOKIE_BUTTON}
    Click Element    ${COOKIE_BUTTON}
    Switch Window    ${PAGE_TITLE}
    Log To Console  \nClicking search button..
    Click Element    ${SEARCH_ICON}
    Wait Until Element Is Visible    ${SEARCH_FORM}
    Input Text    ${SEARCH_FORM}     Python
    Click Button    ${SEARCH_BUTTON}
    Wait Until Location Contains    ${SEARCH_RESULTS_PAGE}
    ${search_result}=    Get Text    ${SEARCH_RESULTS_LOCATOR}
    Log To Console  \nFound results: ${search_result}
    Should Be Equal As Strings    ${search_result}    ${EXPECTED_RESULT}
    Close Browser




