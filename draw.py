import consts
import sys
import pygame
from math import sin, cos

RESOURCE_RADUIS = consts.RESOURCE_RADIUS
PLAYER_POSITIONS = [
        (0,0,150,150),
        (500,0,150,150),
        (0,440,150,150),
        (500,440,150,150),
]

black = 0,0,0

def draw_resource_tile(surface, tile):
    pi2 = 2 * 3.14
    n = 6
    position = tile.location

    pygame.draw.polygon(
        surface, 
        tile.color,
        [
            (
                cos(i / n * pi2 + 3.14 / 2) * RESOURCE_RADUIS + position[0],
                sin(i / n * pi2 + 3.14 / 2) * RESOURCE_RADUIS + position[1]
            )
            for i in range(0,n)
        ]
    )
    myfont = pygame.font.SysFont("monospace", 15)
    if tile.chit:
        label = myfont.render(str(tile.chit), 1, (0,0,0))
        surface.blit(label, tile.location)

def draw_settlement(surface, settlement):
    size = 20 if settlement.city else 10
    pygame.draw.circle(
            surface,
            settlement.color,
            settlement.position,
            size
    )

def draw_road(surface, road):
    pygame.draw.line(
            surface,
            road.color,
            road.start,
            road.end,
            10
    )

def print_board(screen, board):
    for tile in board.tiles:
        draw_resource_tile(screen, tile)
    for settlement in board.settlements:
        draw_settlement(screen, settlement)
    for road in board.roads:
        draw_road(screen, road)

def print_player(screen, player):
    position = PLAYER_POSITIONS[player.number - 1]
    pygame.draw.rect(screen, (255,255,255), position, 5)
    text = 'Player ' + str(player.number)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(
            text,
            1,
            player.color
    )
    screen.blit(label, (position[0] + 30, position[1] + 5))
    text = 'Points: ' + str(player.points)
    label = myfont.render(
            text,
            1,
            (255,255,255)
    )
    screen.blit(label, (position[0] + 10, position[1] + 20))
    #text = 'Resources: ' + str(sum([player.hand[resource] for resource in player.hand]))
    #label = myfont.render(text, 1, (255,255,255))
    #screen.blit(label, (position[0] + 10, position[1] + 35))
    text = 'Brick: ' + str(player.hand[consts.Resource.BRICK])
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 35))
    text = 'Grain: ' + str(player.hand[consts.Resource.GRAIN])
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 50))
    text = 'Lumber: ' + str(player.hand[consts.Resource.LUMBER])
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 65))
    text = 'Ore: ' + str(player.hand[consts.Resource.ORE])
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 80))
    text = 'Wool: ' + str(player.hand[consts.Resource.WOOL])
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 95))
    text = 'Dev Cards: ' + str(len(player.d_cards))
    label = myfont.render(text, 1, (255, 255, 255))
    screen.blit(label, (position[0] + 10, position[1]  + 110))
    text = 'Knights: ' + str(player.knights)
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (position[0] + 10, position[1] + 125))

def print_screen(screen, board, text, players, buttons=[]):
    screen.fill(black)
    print_board(screen, board)
    for player in players:
        print_player(screen, player)
    pygame.draw.rect(screen, (255,255,255), (0,590,640,50), 5)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(
            text,
            1,
            (255,255,255)
    )
    screen.blit(label, (20, 600))
    print_buttons(screen, buttons)
    pygame.display.flip()

def print_buttons(screen, buttons):
    start = 200
    for button in buttons:
        pygame.draw.rect(screen, (255,255,255), (start, 605, 150, 20), 2)
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(button['label'], 1, (255,255,255))
        screen.blit(label, (start + 10, 607))
        button['pos'] = (start, 605, 150, 20)
        start += 170

