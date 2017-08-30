class Resource(object):
    BRICK = 0
    GRAIN = 1
    LUMBER = 2
    ORE = 3
    WOOL = 4

ResourceColors = {
        Resource.BRICK: (250,0,0),
        Resource.LUMBER: (0,51,0),
        Resource.WOOL: (0,255,0),
        Resource.GRAIN: (255,204,0),
        Resource.ORE: (102,102,153),
        'desert': (153,102,0),
}

PlayerColors = {
        1: (255, 0, 0),
        2: (255, 255, 0),
        3: (0, 255, 0),
        4: (0, 0, 255)
}

CENTER = (300,300)
RESOURCE_RADIUS = 50

TilePositions = {
        0: (CENTER[0] - 2 * RESOURCE_RADIUS, CENTER[1] - 4 * RESOURCE_RADIUS),
        1: (CENTER[0], CENTER[1] - 4 * RESOURCE_RADIUS),
        2: (CENTER[0] + 2 * RESOURCE_RADIUS, CENTER[1] - 4 * RESOURCE_RADIUS),

        11: (CENTER[0] - 3 * RESOURCE_RADIUS, CENTER[1] - 2 * RESOURCE_RADIUS),
        12: (CENTER[0] - RESOURCE_RADIUS, CENTER[1] - 2 * RESOURCE_RADIUS),
        13: (CENTER[0] + RESOURCE_RADIUS, CENTER[1] - 2 * RESOURCE_RADIUS),
        3: (CENTER[0] + 3 * RESOURCE_RADIUS, CENTER[1] - 2 * RESOURCE_RADIUS),

        10: (CENTER[0] - 4 * RESOURCE_RADIUS, CENTER[1]),
        17: (CENTER[0] - 2 * RESOURCE_RADIUS, CENTER[1]),
        18: (CENTER[0], CENTER[1]),
        14: (CENTER[0] + 2 * RESOURCE_RADIUS, CENTER[1]),
        4: (CENTER[0] + 4 * RESOURCE_RADIUS, CENTER[1]),

        9: (CENTER[0] - 3 * RESOURCE_RADIUS, CENTER[1] + 2 * RESOURCE_RADIUS),
        16: (CENTER[0] - RESOURCE_RADIUS, CENTER[1] + 2 * RESOURCE_RADIUS),
        15: (CENTER[0] + RESOURCE_RADIUS, CENTER[1] + 2 * RESOURCE_RADIUS),
        5: (CENTER[0] + 3 * RESOURCE_RADIUS, CENTER[1] + 2 * RESOURCE_RADIUS),

        8: (CENTER[0] - 2 * RESOURCE_RADIUS, CENTER[1] + 4 * RESOURCE_RADIUS),
        7: (CENTER[0], CENTER[1] + 4 * RESOURCE_RADIUS),
        6: (CENTER[0] + 2 * RESOURCE_RADIUS, CENTER[1] + 4 * RESOURCE_RADIUS),
}

TileSettlementMap = {
        #Tile: [settlements]
        0: [0,1,2,8,9,10],
        1: [2,3,4,10,11,12],
        2: [4,5,6,12,13,14],

        11: [7,8,9,17,18,19],
        12: [9,10,11,19,20,21],
        13: [11,12,13,21,22,23],
        3: [13,14,15,23,24,25],

        10: [16,17,18,27,28,29],
        17: [18,19,20,29,30,31],
        18: [20,21,22,31,32,33],
        14: [22,23,24,33,34,35],
        4: [24,25,26,35,36,37],

        9: [28,29,30,38,39,40],
        16: [30,31,32,40,41,42],
        15: [32,33,34,42,43,44],
        5: [34,35,36,44,45,46],

        8: [39,40,41,47,48,49],
        7: [41,42,43,49,50,51],
        6: [43,44,45,51,52,53],
}

SettlementPositions = {
        0: (150, 70),
        1: (200, 45),
        2: (250, 70),
        3: (300, 45),
        4: (350, 70),
        5: (400, 45),
        6: (450, 70),

        7: (100, 160),
        8: (150, 135),
        9: (200, 160),
        10: (250, 135),
        11: (300, 160),
        12: (350, 135),
        13: (400, 160),
        14: (450, 135),
        15: (500, 160),

        16: (50, 265),
        17: (100, 240),
        18: (150, 265),
        19: (200, 240),
        20: (250, 265),
        21: (300, 240),
        22: (350, 265),
        23: (400, 240),
        24: (450, 265),
        25: (500, 240),
        26: (550, 265),

        27: (50, 330),
        28: (100, 365),
        29: (150, 330),
        30: (200, 365),
        31: (250, 330),
        32: (300, 365),
        33: (350, 330),
        34: (400, 365),
        35: (450, 330),
        36: (500, 365),
        37: (550, 330),

        38: (100, 435),
        39: (150, 460),
        40: (200, 435),
        41: (250, 460),
        42: (300, 435),
        43: (350, 460),
        44: (400, 435),
        45: (450, 460),
        46: (500, 435),

        47: (150, 530),
        48: (200, 555),
        49: (250, 530),
        50: (300, 555),
        51: (350, 530),
        52: (400, 555),
        53: (450, 530),
}

Roads = [
        (0,1),
        (1,2),
        (2,3),
        (3,4),
        (4,5),
        (5,6),

        (7,8),
        (8,9),
        (9,10),
        (10,11),
        (11,12),
        (12,13),
        (13,14),
        (14,15),

        (16,17),
        (17,18),
        (18,19),
        (19,20),
        (20,21),
        (21,22),
        (22,23),
        (23,24),
        (24,25),
        (25,26),

        (27,28),
        (28,29),
        (29,30),
        (30,31),
        (31,32),
        (32,33),
        (33,34),
        (34,35),
        (35,36),
        (36,37),

        (38,39),
        (39,40),
        (40,41),
        (41,42),
        (42,43),
        (43,44),
        (44,45),
        (45,46),

        (47,48),
        (48,49),
        (49,50),
        (50,51),
        (51,52),
        (52,53),

        (0,8),
        (2,10),
        (4,12),
        (6,14),

        (7,17),
        (9,19),
        (11,21),
        (13,23),
        (15,25),

        (16,27),
        (18,29),
        (20,31),
        (22,33),
        (24,35),
        (26,37),

        (28,38),
        (30,40),
        (32,42),
        (34,44),
        (36,46),

        (39,47),
        (41,49),
        (43,51),
        (45,53),
]

def get_midpoint(point1, point2):
    return ((point1[0] + point2[0]) * .5, (point1[1] + point2[1]) * .5)

RoadMidpoints = {
        i: get_midpoint(SettlementPositions[road[0]], SettlementPositions[road[1]])
        for i,road in enumerate(Roads)
}

Costs = {
        'road': {
            Resource.BRICK: 1,
            Resource.LUMBER: 1,
        },
        'settlement': {
            Resource.BRICK: 1,
            Resource.GRAIN: 1,
            Resource.LUMBER: 1,
            Resource.WOOL: 1,
        },
        'city': {
            Resource.GRAIN: 2,
            Resource.ORE: 3,
        },
        'd_card': {
            Resource.GRAIN: 1,
            Resource.ORE: 1,
            Resource.WOOL: 1,
        },
}
