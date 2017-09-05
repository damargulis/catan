import consts
from random import shuffle
from draw import print_screen

class ResourceTile(object):
    def __init__(self, resource):
        self.resource = resource
        self.color = consts.ResourceColors[resource]
        self.blocked = False

    def set_chit(self, chit):
        self.chit = chit

    def set_location(self, location):
        self.location = consts.TilePositions[location]

class DesertTile(ResourceTile):
    def __init__(self):
        self.resource = None
        self.chit = None
        self.color = consts.ResourceColors['desert']
        self.blocked = True

    def set_chit(self, chit):
        raise NotImplementedError

class Board(object):
    def __init__(self):
        self.ports = self._get_ports()
        self.tiles = self._get_tiles()
        shuffle(self.tiles)
        for i, tile in enumerate(self.tiles):
            tile.set_location(i)
        chits = self._get_chits()
        i = 0
        for tile in self.tiles:
            try:
                tile.set_chit(chits[i])
                i += 1
            except:
                continue
        self.settlements = []
        self.roads = []
        self.d_cards = self._get_d_cards()
        shuffle(self.d_cards)

    def _get_ports(self):
        return consts.Ports

    def _get_tiles(self):
        tiles = []
        for i in range(3):
            tiles.append(ResourceTile(consts.Resource.BRICK))
        for i in range(4):
            tiles.append(ResourceTile(consts.Resource.LUMBER))
        for i in range(4):
            tiles.append(ResourceTile(consts.Resource.WOOL))
        for i in range(4):
            tiles.append(ResourceTile(consts.Resource.GRAIN))
        for i in range(3):
            tiles.append(ResourceTile(consts.Resource.ORE))
        tiles.append(DesertTile())
        return tiles

    def _get_chits(self):
        return [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    def _get_d_cards(self):
        return (
                [ Knight() ] * 14
                + [ Point() ] * 5
                + [ Monopoly() ] * 2
                + [ RoadBuilder() ] * 2
                + [YearOfPlenty() ] * 2
        )

    def get_tiles(self, settlement):
        return [
                tile for tile in consts.TileSettlementMap
                if settlement.number in consts.TileSettlementMap[tile]
        ]

class Knight(object):
    label = 'Knight'

    def make_action(self, screen, board, players, player):
        def action():
            player.play_d_card(self)
            print_screen(screen, board, 'Player ' + str(player.number) + ': Pick a settlement to Block', players)
            players_blocked = player.pick_tile_to_block(board)
            buttons = [
                    {
                        'label': 'Player ' + str(player_blocked.number),
                        'player': player_blocked
                    } for player_blocked in players_blocked
            ]
            if buttons:
                print_screen(screen, board, 'Take a resource from:', players, buttons)
                player_chosen = player.pick_option(buttons)
                player_chosen['player'].give_random_to(player)
            player.knights += 1
            if player.knights >= 3 and not self.largest_army:
                max_other = max([p.knights for p in players])
                if player.knights > max_other:
                    for p in players:
                        if p.largest_army:
                            p.largest_army = False
                            p.points -= 2
                    player.largest_army = True
                    player.points += 2
            return [], None
        return action

class Point(object):
    label = 'Point'

    def make_action(self, screen, board, players, player):
        raise NotImplementedError

class Monopoly(object):
    label = 'Monopoly'

    def make_action(self, screen, board, players, player):
        def action():
            player.play_d_card(self)
            buttons = [
                    {
                        'label': consts.ResourceMap[i],
                        'resource': i,
                    } for i in range(5)
            ]
            print_screen(screen, board, 'Take all of:', players, buttons)
            resource = player.pick_option(buttons)['resource']
            for p in players:
                if p != player:
                    player.hand[resource] += p.hand[resource]
                    p.hand[resource] = 0
            return [], None
        return action

class RoadBuilder(object):
    label = 'Road Builder'

    def make_action(self, screen, board, players, player):
        def action():
            player.play_d_card(self)
            for i in range(2):
                print_screen(screen, board, 'Player ' + str(player.number) + ': Place a road', players)
                player.place_road(board)
            return [], None
        return action

class YearOfPlenty(object):
    label = 'Year Of Plenty'

    def make_action(self, screen, board, players, player):
        def action():
            player.play_d_card(self)
            for i in range(2):
                buttons = [
                        {
                            'label': consts.ResourceMap[i],
                            'resource': i,
                        } for i in range(5)
                ]
                print_screen(screen, board, 'Player ' + str(player.number) + ': Pick a Resource', players, buttons)
                resource = player.pick_option(buttons)['resource']
                player.hand[resource] += 1
            return [], None

        return action
