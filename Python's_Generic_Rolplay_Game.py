import random
import matplotlib
import pygame
import Tkinter
class Characters:

  Self.name = Nombre
  Self.class = clase
  Self.level = 1
  Self.life = 100
  Self.strength = 10
  Self.intelligence = 10
  Self.inventory = []

def attack(Self.foe):
  damage = Self.strength + random.randint(0,10)
  enemy.life -= damage
  print(f"{Self.name} ataca a {enemy.name} causando {damage} de daño.")

def use_item (Self,item)
if item in Self.inventory:
  if item = "Heal Potion"

Self.live += 20
Self.inventory.remove(item)

print(f"{Self.name} usa un/a {item} y recupera 20 de HP.")

else: print(f" {Self.name} no sabe usar {item}.")
else: print(f" {item} no está en el inventario de {Self.name}.")

def show_stats(Self):
  print(f" {Self.name}, clase {self.class}, level: {Self.level}, HP: {Self.live}, strength: {Self.strength}, intelligence: {Self.intelligence}")

def class _init_(Self, name, level)
Self.name = name
Self.level = level
Self.life = 50 + ( level * 10)
self.strength = 5 + (level * 2)

def attack(Self.character):
  damage = Self.strength + random.randint(0,5)
  character.life -= damage
  print(f"{Self.name} ataca a {character.name} causando {damage} de daño.")

def make_character():
  name = input("ingresa un nombre:")
  clase = input("Elige tu Clase (Warrior/Mage):")
  return character (name,class)

def make_enemy(level):
name_enemy = ["Zombie", "Spider", "warden"]
name = random.choice(name_enemy)
return enemy(name,level)
def main ():

  player = make_character()
  enemy = make_enemy(player.level)
  while player.life > 0:
    player.show_stats()
    accion = input("¿Que quieres hacer? (atacar/usar objeto):").lower()
    if accion == "attack":
      player.attack(enemy)
elif accion == "use_item"
 item = input("¿que objeto usarás?:")
player.use_item
