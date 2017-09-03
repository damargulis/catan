import consts
import pygame
from board import Board
from draw import print_screen
from dice import Dice
from player import Player
import sys

pygame.init()

size = consts.SCREEN_SIZE
black = consts.BLACK
screen = pygame.display.set_mode(size)

def pick_settlements(players, board):
    def draft_round(players, board, second):
        for i, player in enumerate(players):
            text = 'Player ' + str(player.number) + ': Pick a spot to settle'
            print_screen(screen, board, text, players)
            settlement = player.place_settlement(board)
            text = 'Player ' + str(player.number) + ': Place a road'
            print_screen(screen, board, text, players)
            player.place_road(board, settlement)
            if second:
                tiles = board.get_tiles(settlement)
                for tile in tiles:
                    resource = board.tiles[tile].resource
                    if resource is not None:
                        player.take_resource(board.tiles[tile].resource)

    draft_round(players, board, False)
    players.reverse()
    draft_round(players, board, True)
    players.reverse()

def give_resources(board, total):
    for num, tile in enumerate(board.tiles):
        if tile.resource and not tile.blocked and tile.chit == total:
            for settlement_number in consts.TileSettlementMap[num]:
                for settlement in board.settlements:
                    if settlement.number == settlement_number:
                        settlement.player.take_resource(tile.resource)
                        if settlement.city:
                            settlement.player.take_resource(tile.resource)

def get_possible_purchases(player, board, players):
    can_afford = []
    for item in consts.Costs:
        if player.can_afford(item) and player.can_buy(board, item):
            def func_creator(item):
                def make_purchase():
                    player.purchase(item, board)
                    if item == 'road':
                        print_screen(screen, board, 'Place your road', players)
                        player.place_road(board)
                    elif item == 'settlement':
                        print_screen(screen, board, 'Place your settlement', players)
                        player.place_settlement(board)
                    elif item == 'city':
                        print_screen(screen, board, 'Pick a settlement to city', players)
                        player.place_city(board)
                    elif item == 'd_card':
                        card = player.pick_d_card(board)
                        buttons = [{'label': 'ok', 'action': end_turn}]
                        print_screen(screen, board, 'You picked a ' + card.label, players, buttons)
                        player.pick_option(buttons)
                    return [], None
                return make_purchase
            can_afford.append({
                'label': item,
                'action': func_creator(item),
            })
    can_afford.append({
        'label': 'cancel',
        'action': end_turn
    })
    return can_afford

def end_turn():
    return [], None

def main():
    board = Board()
    dice = Dice()
    players = [ Player(i) for i in range(1,5) ]
    player_turn = 0
    pick_settlements(players, board)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        player = players[player_turn]
        def roll_dice():
            total = sum(dice.roll())
            give_resources(board, total)
            buttons = [
                    {
                        'label': 'End Turn',
                        'action': end_turn,
                    }
            ]
            possible_purchases = get_possible_purchases(player, board, players)

            def make_purchase():
                return possible_purchases, 'Buy:'

            if len(possible_purchases) > 1:
                buttons.append({
                    'label': 'Make Purchase',
                    'action': make_purchase
                })
            return buttons, 'You Rolled: ' + str(total)
        buttons = [
                {
                    'label': 'Roll Dice',
                    'action': roll_dice
                 }
        ]

        d_cards = [{'label': card.label, 'action': card.action} for card in player.d_cards] 
        def play_d_card():
            return d_cards, 'Which Card: '
        if player.d_cards:
            buttons.append({
                'label': 'Play D Card',
                'action': play_d_card
            })
        label = 'Player %s\'s Turn' % player.number
        while buttons:
            print_screen(screen, board, label, players, buttons)
            option = player.pick_option(buttons)
            buttons, label = option['action']()
        player_turn = (player_turn + 1) % 4

if __name__ == '__main__':
    main()
