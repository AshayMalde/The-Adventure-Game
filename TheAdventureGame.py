import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glEnable(GL_DEPTH_TEST)

def choose_character():
    characters = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    print("Choose your character:")
    for key, value in characters.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice (1-3): ")
    return characters.get(choice, "Unknown")

player_health = 100

inventory = []

spells = {"Fireball": 20, "Lightning": 25, "Heal": -15, "Ice Blast": 30, "Shield": -20}

def cast_spell(spell):
    global player_health
    if spell in spells:
        effect = spells[spell]
        if effect < 0:
            player_health = min(100, player_health - effect)
            print(f"You used {spell}! Health: {player_health}")
        else:
            print(f"You cast {spell} dealing {effect} damage!")
    else:
        print("Unknown spell!")

def solve_puzzle():
    puzzles = {
        "Easy": ("What is 2 + 2?", "4"),
        "Medium": ("Solve: 10 / 2 + 3", "8"),
        "Hard": ("What is the square root of 144?", "12")
    }
    for difficulty, (question, answer) in puzzles.items():
        print(f"{difficulty} Puzzle: {question}")
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print(f"Correct! You solved a {difficulty} puzzle and received a reward!")
            pick_up_item(f"{difficulty} Puzzle Reward")
        else:
            print("Incorrect! You take damage.")
            take_damage(10)

def side_quest():
    print("A villager asks for your help to defeat a monster!")
    choice = input("Do you accept? (Y/N) ").lower()
    if choice == "y":
        print("You fought bravely and won! You received a reward.")
        pick_up_item("Silver Sword")
    else:
        print("You ignored the request and walked away.")

def pick_up_item(item):
    inventory.append(item)
    print(f"You picked up: {item}")

def show_inventory():
    print("Inventory:", inventory if inventory else "Empty")

def take_damage(amount):
    global player_health
    player_health -= amount
    print(f"You took {amount} damage! Health: {player_health}")
    if player_health <= 0:
        print("Game Over!")
        pygame.quit()
        exit()

def boss_fight():
    print("A powerful boss appears!")
    boss_health = 50
    while boss_health > 0:
        action = input("Attack (A), Dodge (D), or Cast Spell (S)? ").lower()
        if action == "a":
            boss_health -= 10
            print(f"You hit the boss! Boss health: {boss_health}")
        elif action == "d":
            print("You dodged the boss attack!")
        elif action == "s":
            cast_spell("Fireball")
            boss_health -= 20
        else:
            take_damage(10)
    print("Boss defeated!")

def game_storyline():
    print("Welcome to the Adventure Quest!")
    print("Your journey begins in a dark forest...")
    choice = input("Do you explore a cave (C) or follow the path (P)? ").lower()
    if choice == "c":
        print("You found a mysterious artifact!")
        pick_up_item("Ancient Artifact")
        solve_puzzle()
    elif choice == "p":
        print("You encounter a group of enemies!")
        attack_enemy()
        side_quest()
    boss_fight()

def attack_enemy():
    print("You attack the enemy and defeat it!")

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            cast_spell("Fireball")
        if keys[pygame.K_i]:
            show_inventory()
        if keys[pygame.K_p]:
            pick_up_item("Magic Potion")
        if keys[pygame.K_b]:
            boss_fight()
        if keys[pygame.K_m]:
            solve_puzzle()
        pygame.display.flip()
        pygame.time.wait(10)

player = choose_character()
print(f"You have chosen: {player}")
game_storyline()
game_loop()
pygame.quit()
