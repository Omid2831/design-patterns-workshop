Feature: Interquartile range of battery brand lifespans
  As a consumer researcher
  I want to calculate the interquartile range (IQR) of two battery brands
  So that I can measure the spread of the middle 50% of their lifespans

  Background:
    Given a battery dataset "Brand A" with values 86,87,94,95,98,99,100,100,102,103,106,107,108,110,110,112,112,112,115,115
    And a battery dataset "Brand B" with values 55,82,86,94,95,100,101,103,105,106,107,109,110,113,113,116,117,119,124,132

  Scenario: Calculate IQR for Brand A
    When I calculate the interquartile range for "Brand A"
    Then the result should be 12.5

  Scenario: Calculate IQR for Brand B
    When I calculate the interquartile range for "Brand B"
    Then the result should be 17.0
