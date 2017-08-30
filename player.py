import consts
import math
import pygame
import sys

class Player(object):
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.hand = {
                consts.Resource.BRICK: 0,
                consts.Resource.LUMBER: 0,
                consts.Resource.WOOL: 0,
                consts.Resource.GRAIN: 0,
                consts.Resource.ORE: 0,
        }
        self.d_cards = []
        self.points = 0
        self.settlements_left = 5
        self.roads_left = 15
        self.cities_left = 4
        self.longest_road = 0
        self.knights = 0

    def take_resource(self, resource):
        self.hand[resource] += 1

    def can_afford(self, item):
        for resource in consts.Costs[item]:
            if self.hand[resource] < consts.Costs[item][resource]:
                return False
        return True

    def can_buy(self, board, item):
        if item == 'd_card':
            return True
        elif item == 'road':
            if self.roads_left > 0:
                return True
            return False
        elif item == 'city':
            if self.cities_left > 0:
                for settlement in board.settlements:
                    if settlement.player == self and not settlement.city:
                        return True
            return False
        elif item == 'settlement':
            pass # figure this out -- and need a new place_settlement that must be attatched to current road


    def purchase(self, item, board):
        for resource in consts.Costs[item]:
            self.hand[resource] -= consts.Costs[item][resource]

    def place_road(self, board, settlement=None):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for num,pos in consts.RoadMidpoints.items():
                    dist = math.hypot(pos[0] - event.pos[0], pos[1] - event.pos[1])
                    if dist < 20:
                        roads = [(road.start, road.end) for road in board.roads ]
                        if pos not in roads:
                            road = Road(self.color, consts.Roads[num])
                            if settlement:
                                if road.start == settlement.position or road.end == settlement.position:
                                    board.roads.append(road)
                                    self.roads_left -= 1
                                    return
                            else:
                                roads_owned = [r for r in board.roads if r.color == self.color]
                                print(roads_owned)
                                for test_r in roads_owned:
                                    if road.start == test_r.start or test_r.end == road.end or road.start == test_r.end or road.end == test_r.start:
                                        board.roads.append(road)
                                        self.roads_left -= 1
                                        return

    def place_city(self, board):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for settlement in board.settlements:
                    if settlement.player == self:
                        pos = settlement.position
                        dist = math.hypot(pos[0] - event.pos[0], pos[1] - event.pos[1])
                        if dist < 10:
                            settlement.make_city()
                            return

    def place_settlement(self, board):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for num,pos in consts.SettlementPositions.items():
                    dist = math.hypot(pos[0] - event.pos[0], pos[1] - event.pos[1])
                    if dist < 10:
                        numbers = [settlement.number for settlement in board.settlements ]
                        if num not in numbers:
                            connected_roads = [ road for road in consts.Roads if num in road ]
                            adj = [ road[0] if road[1] == num else road[1] for road in connected_roads ]
                            combined = set(adj).intersection(set(numbers))
                            if len(combined) == 0:

                                settlement = Settlement(self, num)
                                board.settlements.append(settlement)
                                self.settlements_left -= 1
                                self.points += 1
                                return settlement

    def pick_option(self, options):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for option in options:
                    if is_inside(event.pos, option['pos']):
                        return option

def is_inside(pos, box):
    if pos[0] < box[0]:
        return False
    if pos[0] > box[0] + box[2]:
        return False
    if pos[1] < box[1]:
        return False
    if pos[1] > box[1] + box[3]:
        return False
    return True

class Settlement(object):
    def __init__(self, player, number):
        self.player = player
        self.color = player.color,
        self.number = number
        self.position = consts.SettlementPositions[number]
        self.city = False

    def make_city(self):
        self.city = True
        self.player.points += 1

class Road(object):
    def __init__(self, color, spots):
        self.color = color
        self.start = consts.SettlementPositions[spots[0]]
        self.end = consts.SettlementPositions[spots[1]]
