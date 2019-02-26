Feature: Test Home Page
    Scenario:After login user will get a Home link to view all post
        When user click on Home link
        Then User should contain a page with last Post of last user!

    Scenario:user wants to update or delete his/her post
        When user click on Home link and user wants to update his/her post
        Then User should contain a page with two buttons "Update" or "Delete"
