@web @google
Feature: search for highest and lowest price in ebay home page
  As a ebay customer,
  I search lower and highest price

  Scenario: search for prices range
    Given browser is open on ebay website
    When get highest and lowest price
    Then print them


