Feature: BDD Demo

Scenario: Accept input and display message
    Given User is on Home Page "http://localhost:5000/" on browser "chrome"
     When User Enters Username as "John Doe"
     And User clicks on "Submit" button
     Then Message displayed "Hello John Doe"
     Then close browser
