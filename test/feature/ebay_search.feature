@web @google
Feature: open a browser and search for a keyword
  As a ebay customer,
  I search for something in the web

  Scenario: search for some keyword
    Given browser is open on ebay website
    When type a "bag"
    Then check there is more than one results


