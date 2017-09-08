@wip
Feature: Player enters guess

As a player
I want to enter a guesss
So I can break the code

Scenario: Player enters four numbers
Given the game has been started
When the player enters a string of four digits
Then the game displays exactly four zeros, plusses and/or minuses

Scenario: Player enters something that not four numbers
Given the game has been started
When the player enters a string that is not exactly four digits
Then the game displays "Please enter four digits."
