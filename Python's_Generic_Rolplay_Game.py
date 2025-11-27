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

def mostrar_estado(Self):
  print(f" {Self.name}, clase {self.class}, level: {Self.level}, HP: {Self.live}, strength: {Self.strength}, intelligence: {Self.intelligence}")
