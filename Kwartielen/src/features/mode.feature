Feature: Mode lifespan of battery brands
  As a consumer researcher
  I want to calculate the mode lifespan of two battery brands
  So that I can identify the most frequently occurring lifespan value

  Background:
    Given a battery dataset "Brand A" with values 86,87,94,95,98,99,100,100,102,103,106,107,108,110,110,112,112,112,115,115
    And a battery dataset "Brand B" with values 55,82,86,94,95,100,101,103,105,106,107,109,110,113,113,116,117,119,124,132

  Scenario: Calculate mode for Brand A
    When I calculate the mode for "Brand A"
    Then the mode should contain 112

  Scenario: Calculate mode for Brand B
    When I calculate the mode for "Brand B"
    Then the mode should contain 113
