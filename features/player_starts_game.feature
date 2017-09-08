Feature: Player starts game

  As a player,
  I want to start a game
  So that I can play the game 

Scenario: start game

	Given the game is not running
  When the user types "python -m codebreaker"
  Then the game displays "Welcome to Code Breaker"
