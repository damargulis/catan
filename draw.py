import consts
import sys
import pygame
from math import sin, cos

RESOURCE_RADUIS = consts.RESOURCE_RADIUS
PLAYER_POSITIONS = consts.PLAYER_POSITIONS

black = consts.BLACK
white = consts.WHITE

def draw_resource_tile(surface, tile):
    pi = 3.14
    n = 6
    position = tile.location
    pygame.draw.polygon(
        surface, 
        tile.color,
        [
            (
                cos(i / n * 2 * pi + pi / 2) * RESOURCE_RADUIS + position[0],
                sin(i / n * 2 * pi + pi / 2) * RESOURCE_RADUIS + position[1]
            )
            for i in range(0,n)
        ]
    )
    if tile.chit:
        print_text(surface, str(tile.chit), tile.location, black)

def draw_settlement(surface, settlement):
    pygame.draw.circle(
            surface,
            settlement.color,
            settlement.position,
            consts.CITY_SIZE if settlement.city else consts.SETTLEMENT_SIZE
    )

def draw_road(surface, road):
    pygame.draw.line(
            surface,
            road.color,
            road.start,
            road.end,
            consts.ROAD_WIDTH
    )

def print_board(screen, board):
    for tile in board.tiles:
        draw_resource_tile(screen, tile)
    for settlement in board.settlements:
        draw_settlement(screen, settlement)
    for road in board.roads:
        draw_road(screen, road)

def print_text(screen, text, position, color=white):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, color)
    screen.blit(label, position)

def print_player(screen, player):
    position = PLAYER_POSITIONS[player.number - 1]
    pygame.draw.rect(screen, (255,255,255), position, 5)
    print_text(
            screen, 
            'Player ' + str(player.number), 
            (position[0] + 30, position[1] + 5),
            player.color, 
    )
    print_text(
            screen,
            'Points: ' + str(player.points),
            (position[0] + 10, position[1] + 20),
    )
    print_text(
            screen,
            'Brick: ' + str(player.hand[consts.Resource.BRICK]),
            (position[0] + 10, position[1] + 35),
    )
    print_text(
            screen,
            'Grain: ' + str(player.hand[consts.Resource.GRAIN]),
            (position[0] + 10, position[1] + 50),
    )
    print_text(
            screen,
            'Lumber: ' + str(player.hand[consts.Resource.LUMBER]),
            (position[0] + 10, position[1] + 65),
    )
    print_text(
            screen,
            'Ore: ' + str(player.hand[consts.Resource.ORE]),
            (position[0] + 10, position[1] + 80)
    )
    print_text(
            screen,
            'Wool: ' + str(player.hand[consts.Resource.WOOL]),
            (position[0] + 10, position[1] + 95)
    )
    print_text(
            screen,
            'Dev Cards: ' + str(len(player.d_cards)),
            (position[0] + 10, position[1] + 110)
    )
    print_text(
            screen,
            'Knights: ' + str(player.knights),
            (position[0] + 10, position[1] + 125)
    )

def print_screen(screen, board, text, players, buttons=[]):
    screen.fill(black)
    print_board(screen, board)
    for player in players:
        print_player(screen, player)
    pygame.draw.rect(screen, (255,255,255), (0,590,640,50), 5)
    print_text(screen, text, (20,600))
    print_buttons(screen, buttons)
    pygame.display.flip()

def print_buttons(screen, buttons):
    start = 200
    for button in buttons:
        pygame.draw.rect(screen, (255,255,255), (start, 605, 150, 20), 2)
        print_text(screen, button['label'], (start + 10, 607))
        button['pos'] = (start, 605, 150, 20)
        start += 170

