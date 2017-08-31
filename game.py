import consts
import pygame
from board import Board
from draw import print_screen
from dice import Dice
from player import Player
import sys

pygame.init()

size = width, height = 640, 640
black = (0,0,0)

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
                tiles = [tile for tile in consts.TileSettlementMap if settlement.number in consts.TileSettlementMap[tile]]
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
        if tile.chit == total:
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
                        def select_ok():
                            return [], None
                        card = player.pick_d_card(board)
                        buttons = [{'label': 'ok', 'action': select_ok}]
                        print_screen(screen, board, 'You picked a ' + card, players, buttons)
                        player.pick_option(buttons)
                    return [], None
                return make_purchase
            can_afford.append({
                'label': item,
                'action': func_creator(item),
            })
    def cancel():
        return [], None
    can_afford.append({
        'label': 'cancel',
        'action': cancel
    })
    return can_afford

def main():
    board = Board()
    dice = Dice()
    players = [ Player(i, consts.PlayerColors[i]) for i in range(1,5) ]
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
            def end_turn():
                return [], None
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
        if len(player.d_cards):
            buttons.append({'label': 'Play D Card'})
        label = 'Player %s\'s Turn' % player.number
        while buttons:
            print_screen(screen, board, label, players, buttons)
            option = player.pick_option(buttons)
            buttons, label = option['action']()
        player_turn = (player_turn + 1) % 4
        print('player ' + str(player_turn))

if __name__ == '__main__':
    main()
