Feature: Test adding new post Functionality
    Scenario: User wants to add a post to our app
        When user click on newpost link and enter title "mypost4" and enter content as "Python virtual environment" and submit
        Then new post will be added with title {"mypost4"}
