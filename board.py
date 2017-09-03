import consts
from random import shuffle
from draw import print_board

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

    def set_chit(self, chit):
        raise NotImplementedError

class Board(object):
    def __init__(self):
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
                [ Knight ] * 14
                + [ Point ] * 5
                + [ Monopoly ] * 2
                + [ RoadBuilder ] * 2
                + [ Monopoly ] * 2
        )

    def get_tiles(self, settlement):
        return [
                tile for tile in consts.TileSettlementMap
                if settlement.number in consts.TileSettlementMap[tile]
        ]

class Knight(object):
    label = 'Knight'

    def action():
        print('Playing knight')

class Point(object):
    label = 'Point'

    def action():
        print('playing point')

class Monopoly(object):
    label = 'Monopoly'

    def action(): 
        print('playing monopoly')

class RoadBuilder(object):
    label = 'Road Builder'

    def action():
        print('playing road builder')

class Monopoly(object):
    label = 'Monopoly'

    def action():
        print('Playing Monopoly')
