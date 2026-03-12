Feature: Quartiles of battery brand lifespans
  As a consumer researcher
  I want to calculate Q1, Q2, and Q3 for two battery brands
  So that I can understand the distribution of their lifespans

  Background:
    Given a battery dataset "Brand A" with values 86,87,94,95,98,99,100,100,102,103,106,107,108,110,110,112,112,112,115,115
    And a battery dataset "Brand B" with values 55,82,86,94,95,100,101,103,105,106,107,109,110,113,113,116,117,119,124,132

  Scenario: Calculate Q1 for Brand A
    When I calculate quartile 1 for "Brand A"
    Then the result should be 98.5

  Scenario: Calculate Q2 for Brand A
    When I calculate quartile 2 for "Brand A"
    Then the result should be 104.5

  Scenario: Calculate Q3 for Brand A
    When I calculate quartile 3 for "Brand A"
    Then the result should be 111.0

  Scenario: Calculate Q1 for Brand B
    When I calculate quartile 1 for "Brand B"
    Then the result should be 97.5

  Scenario: Calculate Q2 for Brand B
    When I calculate quartile 2 for "Brand B"
    Then the result should be 106.5

  Scenario: Calculate Q3 for Brand B
    When I calculate quartile 3 for "Brand B"
    Then the result should be 114.5
