import copy
import random
import colorama
import time
inittime = time.time()

drehungen = 0
"""
□(■B-Orange)□□
(■L-Green)(■U-White)(■R-Blue)(■D-Yellow)
□(■F-Red)□□
"""
Redface = Frontface = 2, 1
Whiteface = Upface = 1, 1

Greenface = Leftface = 1, 0
Blueface = Rightface = 1, 2
Yellowface = Downface = 1, 3
Orangeface = Backface = 0, 1


o = "orange"
g = "green"
w = "white"
b = "blue"
y = "yellow"
r = "red"



# def cubemuster():
#     whitespaces = 0
#     for i in range(3):
#         extra_lengh = 6
#         for element in range(3):
#             if isinstance(cube[1][0][i][element], str):
#                 extra_lengh += 2
#         whitespaces = max(len(str(cube[1][0][i][0])) + len(str(cube[1][0][i][1])) + len(str(cube[1][0][i][2])) + extra_lengh, whitespaces)
#
#
#     for element in cube[0][1]:
#         print(" " * whitespaces, element)
#
#     print(cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[1][3][0])
#     print(cube[1][0][1], cube[1][1][1], cube[1][2][1], cube[1][3][1])
#     print(cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[1][3][2])
#
#     for element in cube[2][1]:
#         print(" " * whitespaces, element)

#     print()

def cubemuster():
    whitespaces = 0
    for i in range(3):
        extra_lengh = 6
        for element in range(3):
            if isinstance(cube[1][0][i][element], str):
                extra_lengh += 2
        whitespaces = max(len(str(cube[1][0][i][0])) + len(str(cube[1][0][i][1])) + len(str(cube[1][0][i][2])) + extra_lengh, whitespaces)


    for linie in cube[0][1]:
        print(" " * whitespaces, end="[")
        for index, color in enumerate(linie):
            farbe = using_colorama(color)
            print(farbe, color, colorama.Style.RESET_ALL, end="")
            if index != len(linie) - 1:
                print(end=",")

        print("]")


    first_ebene = cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[1][3][0]
    second_ebene = cube[1][0][1], cube[1][1][1], cube[1][2][1], cube[1][3][1]
    third_ebene = cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[1][3][2]
    all_ebenen = (first_ebene, second_ebene, third_ebene)

    for ebene in all_ebenen:
        for linie in ebene:
            print(end="[")
            for index, color in enumerate(linie):

                farbe = using_colorama(color)
                print(farbe, color, colorama.Style.RESET_ALL, end="")
                if index != len(linie) - 1:
                    print(end=",")
            print(end="]\t")
        print()




    # for element in cube[2][1]:
    #     print(" " * whitespaces, element)

    for linie in cube[2][1]:
        print(" " * whitespaces, end="[")
        for index, color in enumerate(linie):
            farbe = using_colorama(color)
            print(farbe, color, colorama.Style.RESET_ALL, end="")
            if index != len(linie) - 1:
                print(end=",")

        print("]")

    print()



def using_colorama(element_of_list):
    match element_of_list:
        case "red":
            farbe = colorama.Back.RED
        case "blue":
            farbe = colorama.Back.BLUE
        case "yellow":
            farbe = colorama.Back.YELLOW
        case "green":
            farbe = colorama.Back.GREEN
        case "white":
            farbe = colorama.Back.WHITE
        case "orange":
            farbe = f"\033[48;2;{255};{128};{0}m"
        case _:
            raise ValueError

    return farbe





def cubemusterverschoben():
    # whitespaces = 0
    # for i in range(3):
    #     extra_lengh = 6
    #     for element in range(3):
    #         if isinstance(cube[1][0][i][element], str):
    #             extra_lengh += 2
    #     whitespaces = max(len(str(cube[1][0][i][0])) + len(str(cube[1][0][i][1])) + len(str(cube[1][0][i][2])) + extra_lengh, whitespaces)

    whitespaces = 83

    for element in cube[0][1]:
        print(" " * whitespaces, element)

    print(cube[1][2][0], cube[1][3][0], cube[1][0][0], cube[1][1][0])
    print(cube[1][2][1], cube[1][3][1], cube[1][0][1], cube[1][1][1])
    print(cube[1][2][2], cube[1][3][2], cube[1][0][2], cube[1][1][2])

    for element in cube[2][1]:
        print(" " * whitespaces, element)

def reference_coordinate(Turning_face, white_is_up=False):
    if Turning_face == Frontface:
        northneighbor = Yellowface
        eastneighbor = Greenface
        southneighbor = Whiteface
        westneighbor = Blueface

    elif Turning_face == Backface:
        northneighbor = Yellowface
        eastneighbor = Blueface
        southneighbor = Whiteface
        westneighbor = Greenface

    elif Turning_face == Leftface:
        northneighbor = Yellowface
        eastneighbor = Orangeface
        southneighbor = Whiteface
        westneighbor = Redface

    elif Turning_face == Rightface:
        northneighbor = Yellowface
        eastneighbor = Redface
        southneighbor = Whiteface
        westneighbor = Orangeface

    else:
        print("Error no pasaste la cara correcta")

    if white_is_up:
        northneighbortemp = tuple(northneighbor)
        eastneighbortemp = tuple(eastneighbor)
        southneighbortemp = tuple(southneighbor)
        westneighbortemp = tuple(westneighbor)

        northneighbor = southneighbortemp
        southneighbor = northneighbortemp
        eastneighbor = westneighbortemp
        westneighbor = eastneighbortemp


    return northneighbor, eastneighbor, southneighbor, westneighbor

# hay dos tipos de cordenadas, los tipos, que es lo que se encuentra adelante, atras y abajo de mi, y lo otro, es lo que objetivamente se encuentra en el
def cubefacesorientation(Turning_face):
    # esta mierda esta enferma
    if Turning_face == Frontface:
        northneighbor = Whiteface
        eastneighbor = Blueface
        southneighbor = Yellowface
        westneighbor = Greenface

    elif Turning_face == Backface:
        northneighbor = Yellowface
        eastneighbor = Blueface
        southneighbor = Whiteface
        westneighbor = Greenface

    elif Turning_face == Leftface:
        northneighbor = Orangeface
        eastneighbor = Whiteface
        southneighbor = Redface
        westneighbor = Yellowface

    elif Turning_face == Rightface:
        northneighbor = Orangeface
        eastneighbor = Yellowface
        southneighbor = Redface
        westneighbor = Whiteface

    elif Turning_face == Downface:
        northneighbor = 0, 1
        eastneighbor = 1, 0
        southneighbor = 2, 1
        westneighbor = 1, 2

    elif Turning_face == Upface:
        northneighbor = 0, 1
        eastneighbor = 1, 2
        southneighbor = 2, 1
        westneighbor = 1, 0

    return northneighbor, eastneighbor, southneighbor, westneighbor

def Clockturn(Turning_face):
    global drehungen
    drehungen += 1
    """
        Turns `Turning_face` and its respective aristas clockwise. Complex if cases algorithms.
        □■□□
        ■■■■ -> ▣
        □■□□
        """
    # [[1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]
    # -> Clockturn
    # [[7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]]
    cubecopy = copy.deepcopy(cube)
    northneighbor, eastneighbor, southneighbor, westneighbor = cubefacesorientation(Turning_face)

    # es exactamente lo mismo que en anticlockwise, solo intercambien los terminos de cual se copia y en cual se pega intercambiandolos.
    # north, change the downermost layer: this thought is absolutely incorrect.

    # we have to define each case separetly
    print("Clockturn", end=": ")
    if Turning_face == Upface:
        print("Upface")
        # north, change the downermost layer
        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]

        # east, change the leftermost layer
        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[southneighbor[0]][southneighbor[1]][0][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        # south, change the uppermost layer
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]

        # west, change the rightermost layer
        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[northneighbor[0]][northneighbor[1]][2][1] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

    elif Turning_face == Leftface:
        print("Leftface")
        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]
        cube[northneighbor[0]][northneighbor[1]][1][0] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[northneighbor[0]][northneighbor[1]][1][0]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]

        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[southneighbor[0]][southneighbor[1]][1][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[southneighbor[0]][southneighbor[1]][1][0]
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]

    elif Turning_face == Rightface:
        print("Rightface")
        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[northneighbor[0]][northneighbor[1]][1][2] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[northneighbor[0]][northneighbor[1]][1][2]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][2]

        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]
        cube[southneighbor[0]][southneighbor[1]][1][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]

        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[southneighbor[0]][southneighbor[1]][1][2]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]

    elif Turning_face == Downface:
        print("Downface")
        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[northneighbor[0]][northneighbor[1]][0][1] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][2]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]

        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[southneighbor[0]][southneighbor[1]][2][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]
        # correct visual, correct logic

    elif Turning_face == Backface:
        print("Backface")
        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][0][1] = cubecopy[westneighbor[0]][westneighbor[1]][0][1]
        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2] # logic: , visual:

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]
        cube[eastneighbor[0]][eastneighbor[1]][0][1] = cubecopy[northneighbor[0]][northneighbor[1]][0][1]
        cube[eastneighbor[0]][eastneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][2]  # logic: , visual:

        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[southneighbor[0]][southneighbor[1]][0][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][1]
        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][2]  # logic: , visual:

        cube[westneighbor[0]][westneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][0][1] = cubecopy[southneighbor[0]][southneighbor[1]][0][1]
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]  # logic: , visual:
        # logic: acceptable , visual: good

    elif Turning_face == Frontface:
        print("Frontface")
        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][0]
        cube[northneighbor[0]][northneighbor[1]][2][1] = cubecopy[westneighbor[0]][westneighbor[1]][2][1]
        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]
        cube[eastneighbor[0]][eastneighbor[1]][2][1] = cubecopy[northneighbor[0]][northneighbor[1]][2][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]

        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]
        cube[southneighbor[0]][southneighbor[1]][2][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][1]
        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][2]

        cube[westneighbor[0]][westneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]
        cube[westneighbor[0]][westneighbor[1]][2][1] = cubecopy[southneighbor[0]][southneighbor[1]][2][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]
        # logic: acceptable , visual: good, like Backface



    # turning the normal surface of the cube.
    for indexrow, elementrow in enumerate(cubecopy[Turning_face[0]][Turning_face[1]]):
        for index, element in enumerate(elementrow):
            if indexrow == 0:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][0][2] = element
                elif index == 1:
                    cube[Turning_face[0]][Turning_face[1]][1][2] = element
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][2][2] = element


            elif indexrow == 1:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][0][1] = element
                elif index == 1:
                    cube[Turning_face[0]][Turning_face[1]][1][1] = element
                    pass
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][2][1] = element


            elif indexrow == 2:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][0][0] = element
                elif index == 1:
                    cube[Turning_face[0]][Turning_face[1]][1][0] = element
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][2][0] = element

    return cube

def AntiClockturn(Turning_face):
    global drehungen
    drehungen += 1
    """
        Turns `Turning_face` and its respective aristas anti-clockwise. Complex if cases algorithms.
        □■□□
        ■■■■ -> ▣
        □■□□
        """
    # [[1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]
    # -> Anticlockckturn
    # [[7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]]
    cubecopy = copy.deepcopy(cube)
    northneighbor, eastneighbor, southneighbor, westneighbor = cubefacesorientation(Turning_face)

    # es exactamente lo mismo que en Clockwise, solo intercambien los terminos de cual se copia y en cual se pega intercambiandolos.
    # north, change the downermost layer: this thought is absolutely incorrect.

    # we have to define each case separetly
    print("Anticlockturn", end=": ")
    if Turning_face == Upface:
        print("Upface")
        # north, change the downermost layer
        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][2][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        # east, change the leftermost layer
        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]

        # south, change the uppermost layer
        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[southneighbor[0]][southneighbor[1]][0][1] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

        # west, change the rightermost layer
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]

    elif Turning_face == Leftface:
        print("Leftface")
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[northneighbor[0]][northneighbor[1]][1][0]
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]

        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][1][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[southneighbor[0]][southneighbor[1]][1][0]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]

        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]
        cube[southneighbor[0]][southneighbor[1]][1][0] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]

    elif Turning_face == Rightface:
        print("Rightface")
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][2]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[northneighbor[0]][northneighbor[1]][1][2]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]

        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][1][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[southneighbor[0]][southneighbor[1]][1][2]
        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]

        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[southneighbor[0]][southneighbor[1]][1][2] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]

    elif Turning_face == Downface:
        print("Downface")
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][1][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][2]

        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][0][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][1][0]
        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]
        cube[eastneighbor[0]][eastneighbor[1]][1][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]

        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]
        cube[southneighbor[0]][southneighbor[1]][2][1] = cubecopy[westneighbor[0]][westneighbor[1]][1][2]
        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]
        # correct visual, correct logic

    elif Turning_face == Backface:
        print("Backface")
        cube[westneighbor[0]][westneighbor[1]][0][0] = cubecopy[northneighbor[0]][northneighbor[1]][0][0]
        cube[westneighbor[0]][westneighbor[1]][0][1] = cubecopy[northneighbor[0]][northneighbor[1]][0][1]
        cube[westneighbor[0]][westneighbor[1]][0][2] = cubecopy[northneighbor[0]][northneighbor[1]][0][2] # logic: , visual:

        cube[northneighbor[0]][northneighbor[1]][0][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][0]
        cube[northneighbor[0]][northneighbor[1]][0][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][1]
        cube[northneighbor[0]][northneighbor[1]][0][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][0][2]  # logic: , visual:

        cube[eastneighbor[0]][eastneighbor[1]][0][0] = cubecopy[southneighbor[0]][southneighbor[1]][0][0]
        cube[eastneighbor[0]][eastneighbor[1]][0][1] = cubecopy[southneighbor[0]][southneighbor[1]][0][1]
        cube[eastneighbor[0]][eastneighbor[1]][0][2] = cubecopy[southneighbor[0]][southneighbor[1]][0][2]  # logic: , visual:

        cube[southneighbor[0]][southneighbor[1]][0][0] = cubecopy[westneighbor[0]][westneighbor[1]][0][0]
        cube[southneighbor[0]][southneighbor[1]][0][1] = cubecopy[westneighbor[0]][westneighbor[1]][0][1]
        cube[southneighbor[0]][southneighbor[1]][0][2] = cubecopy[westneighbor[0]][westneighbor[1]][0][2]  # logic: , visual:
        # logic: acceptable , visual: good

    elif Turning_face == Frontface:
        print("Frontface")
        cube[westneighbor[0]][westneighbor[1]][2][0] = cubecopy[northneighbor[0]][northneighbor[1]][2][0]
        cube[westneighbor[0]][westneighbor[1]][2][1] = cubecopy[northneighbor[0]][northneighbor[1]][2][1]
        cube[westneighbor[0]][westneighbor[1]][2][2] = cubecopy[northneighbor[0]][northneighbor[1]][2][2]

        cube[northneighbor[0]][northneighbor[1]][2][0] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][0]
        cube[northneighbor[0]][northneighbor[1]][2][1] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][1]
        cube[northneighbor[0]][northneighbor[1]][2][2] = cubecopy[eastneighbor[0]][eastneighbor[1]][2][2]

        cube[eastneighbor[0]][eastneighbor[1]][2][0] = cubecopy[southneighbor[0]][southneighbor[1]][2][0]
        cube[eastneighbor[0]][eastneighbor[1]][2][1] = cubecopy[southneighbor[0]][southneighbor[1]][2][1]
        cube[eastneighbor[0]][eastneighbor[1]][2][2] = cubecopy[southneighbor[0]][southneighbor[1]][2][2]

        cube[southneighbor[0]][southneighbor[1]][2][0] = cubecopy[westneighbor[0]][westneighbor[1]][2][0]
        cube[southneighbor[0]][southneighbor[1]][2][1] = cubecopy[westneighbor[0]][westneighbor[1]][2][1]
        cube[southneighbor[0]][southneighbor[1]][2][2] = cubecopy[westneighbor[0]][westneighbor[1]][2][2]
        # logic: acceptable , visual: good, like Backface



    for indexrow, elementrow in enumerate(cubecopy[Turning_face[0]][Turning_face[1]]):
        for index, element in enumerate(elementrow):
            if indexrow == 0:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][2][0] = element
                elif index == 1:
                    cube[Turning_face[0]][Turning_face[1]][1][0] = element
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][0][0] = element

            elif indexrow == 1:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][2][1] = element
                elif index == 1:
                    pass
                    cube[Turning_face[0]][Turning_face[1]][1][1] = element
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][0][1] = element

            elif indexrow == 2:
                if index == 0:
                    cube[Turning_face[0]][Turning_face[1]][2][2] = element
                elif index == 1:
                    cube[Turning_face[0]][Turning_face[1]][1][2] = element
                elif index == 2:
                    cube[Turning_face[0]][Turning_face[1]][0][2] = element
    return cube

def random_scrambler(cube):
    for iteration_zahl in range(20):
        rotation_type = random.randint(1, 12)

        match rotation_type:
            case 1:
                Clockturn(Rightface)
            case 2:
                AntiClockturn(Rightface)
            case 3:
                Clockturn(Leftface)
            case 4:
                AntiClockturn(Leftface)
            case 5:
                Clockturn(Upface)
            case 6:
                AntiClockturn(Upface)
            case 7:
                Clockturn(Downface)
            case 8:
                AntiClockturn(Downface)
            case 9:
                Clockturn(Frontface)
            case 10:
                AntiClockturn(Frontface)
            case 11:
                Clockturn(Backface)
            case 12:
                AntiClockturn(Backface)

def yellow_dot_white_cross(cube):
    while not (cube[1][3][0][1] == "white" and cube[1][3][1][0] == "white" and cube[1][3][1][2] == "white" and cube[1][3][2][1] == "white"):
        # we repeat this loop until it is white point, yellow cross.
        # We included a clause, to only do this movement if there is no other white piece in the yellow face.
        # i need to check for each drehung ob ich etwas zerstoeren werde.
        # if piece finds itself in awkward position (half of times) it will do 1 movement to go to comnfortable, and in the repetition it will make it.
        # because there are many cases, i will try to incorporate them interlacingly, meaning, bringing them to a place where the problem is already solved.
        # if cube[][0:3][0:2][0:2] == "white":

        # BACKFACE GETTING RID OF WHITE PIECES (orange) # cube checked, logic, efficient.
        if cube[0][1][0][1] == w:
            while cube[1][3][0][1] == "white":
                Clockturn(Downface)
            Clockturn(Backface) # delegates to case 2

        if cube[0][1][1][0] == w: # case 1
            while cube[1][3][1][2] == "white": # das weisse teil wird hier landen [1][2]
                Clockturn(Downface)
            AntiClockturn(Leftface)

        if cube[0][1][1][2] == w: # case 2
            while cube[1][3][1][0] == "white": # das weisse teil wird hier landen [1][0]
                Clockturn(Downface)
            Clockturn(Rightface)

        if cube[0][1][2][1] == w:
            while cube[1][3][0][1] == "white": # das weisse teil wird hier landen [1][0]
                Clockturn(Downface)
            Clockturn(Backface) # delegates to case 1




        # RIGHTFACE GETTING RID OF WHITE PIECES (blue) # cube checked, logic, efficient.
        if cube[1][2][0][1] == w: # case 1
            while cube[1][3][0][1] == "white":
                Clockturn(Downface)
            AntiClockturn(Backface)

        if cube[1][2][1][0] == w:
            while cube[1][3][1][0] == "white":
                Clockturn(Downface)
            Clockturn(Rightface) # goes to case 1

        if cube[1][2][1][2] == w:
            while cube[1][3][1][0] == "white": # this clause will never get executed in a normal cube, because you cant have two pieces of the same color in the same arista
                Clockturn(Downface)
            Clockturn(Rightface)  # goes to case 2

        if cube[1][2][2][1] == w: # case 2
            while cube[1][3][2][1] == "white":
                Clockturn(Downface)
            Clockturn(Frontface)



        # UPFACE GETTING RID OF WHITE PIECES (white) # cube checked, logic, efficient.
        if cube[1][1][0][1] == w:
            while cube[1][3][0][1] == "white":
                Clockturn(Downface)
            Clockturn(Backface)
            Clockturn(Backface)

        if cube[1][1][1][0] == w:
            while cube[1][3][1][2] == "white":
                Clockturn(Downface)
            Clockturn(Leftface)
            Clockturn(Leftface)

        if cube[1][1][1][2] == w:
            AntiClockturn(Upface)
            while cube[1][3][1][0] == "white":
                Clockturn(Downface)
            Clockturn(Rightface)
            Clockturn(Rightface)

        if cube[1][1][2][1] == w:
            while cube[1][3][2][1] == "white":
                Clockturn(Downface)
            Clockturn(Frontface)
            Clockturn(Frontface)



        # LEFTFACE GETTING RID OF WHITE PIECES (green) # cube checked, logic, efficient.
        if cube[1][0][0][1] == w: # case 1
            while cube[1][3][0][1] == "white":
                Clockturn(Downface)
            Clockturn(Backface)

        if cube[1][0][1][0] == w:
            while cube[1][3][1][2] == "white":
                Clockturn(Downface)
            Clockturn(Leftface) # delegate to case 1

        if cube[1][0][1][2] == w:
            while cube[1][3][1][2] == "white":
                Clockturn(Downface)
            Clockturn(Leftface) # delegate to case 2

        if cube[1][0][2][1] == w: # case 2
            while cube[1][3][2][1] == "white":
                Clockturn(Downface)
            AntiClockturn(Frontface)


        # FRONTFACE GETTING RID OF WHITE PIECES (red) # cube checked, logic, efficient.
        if cube[2][1][0][1] == w: # delegation next round to solving case b
            while cube[1][3][2][1] == "white":
                Clockturn(Downface)
            Clockturn(Frontface)

        if cube[2][1][1][0] == w: # solving case a
            while cube[1][3][1][2] == "white":
                Clockturn(Downface)
            Clockturn(Leftface)

        if cube[2][1][1][2] == w: # solving case b
            while cube[1][3][1][0] == "white":
                Clockturn(Downface)
            AntiClockturn(Rightface)

        if cube[2][1][2][1] == w: # delegation next round to solving case b
            while cube[1][3][2][1] == "white":
                Clockturn(Downface)
            Clockturn(Frontface)



    return cube

def white_cross(cube):
    # Thinking:
    # Th efirst thing is that we need to check if middle is equal to piece neighboring yellow face.
    # if they are equal, check wether piece up there is white.
    # if piece up there is white, do turn.
    # if done, do this 4 times, and rotate yellow face.





    neighborslist = (Blueface, Orangeface, Greenface, Redface)

    print("The faces to analyze are the following")
    for neighbor in neighborslist:
        print(neighbor)


    for times in range(4):
        for face_to_analyze in neighborslist:
            center_piece = cube[face_to_analyze[0]][face_to_analyze[1]][1][1]


            if face_to_analyze == Leftface:
                location_white_piece = 1, 2
                if center_piece != cube[face_to_analyze[0]][face_to_analyze[1]][1][0]: # check if up and down are same color. #not like this, it is not orientation of piece if this were a perfect gitter, it is the actual place that this piece is occupying.
                    continue

            elif face_to_analyze == Rightface:
                location_white_piece = 1, 0
                if center_piece != cube[face_to_analyze[0]][face_to_analyze[1]][1][2]: # check if up and down are same color. #not like this, it is not orientation of piece if this were a perfect gitter, it is the actual place that this piece is occupying.
                    continue



            elif face_to_analyze == Backface:
                location_white_piece = 0, 1
                if center_piece != cube[face_to_analyze[0]][face_to_analyze[1]][0][1]:
                    continue

            elif face_to_analyze == Frontface:
                location_white_piece = 2,1
                if center_piece != cube[face_to_analyze[0]][face_to_analyze[1]][2][1]:
                    continue

            # por que no hay un tercer if clause
            # creo que con location white piece se refieren a la arista, que tiene el white.


            # si encontramos que unas de las piezas son iguales, vamos a entrar a este block, else, simplemente vamos a skip
            if cube[1][3][location_white_piece[0]][location_white_piece[1]] == w:# here we check if piece oberhalb de dar la vuelta es blanca, para que no se metan idiotas a joder.
                print("Functiono en cara: ", face_to_analyze, "los colores sincronos eran", center_piece)
                Clockturn(face_to_analyze)
                Clockturn(face_to_analyze)



        Clockturn(Downface)

    return cube

def does_corner_have_color(coordinate_white_or_yellow, color=w):
    # quiero hacer una funcion, que le doy la pieza en la cara blanca, y le doy un tuple, returnea con un bool diciendo si hay peligro ahi
    # arriba izquierda white
    if coordinate_white_or_yellow == (1, 1, 0, 0):
        if cube[1][1][0][0] == color or cube[1][0][0][2] == color or cube[0][1][2][0] == color:
            return True

    # arriba derecha white
    elif coordinate_white_or_yellow == (1, 1, 0, 2):
        if cube[1][1][0][2] == color or cube[0][1][2][2] == color or cube[1][2][0][0] == color:
            return True

    # abajo izquierda white
    elif coordinate_white_or_yellow == (1, 1, 2, 0):

        if cube[1][1][2][0] == color or cube[1][0][2][2] == color or cube[2][1][0][0] == color:
            return True

    # abajo derecha white
    elif coordinate_white_or_yellow == (1, 1, 2, 2):
        if cube[1][1][2][2] == color or cube[2][1][0][2] == color or cube[1][2][2][0] == color:
            return True


    elif coordinate_white_or_yellow == (1, 3, 0, 0):
        if cube[1][3][0][0] == color or cube[1][2][0][2] == color or cube[0][1][0][2] == color:
            return True

    elif coordinate_white_or_yellow == (1, 3, 0, 2):
        if cube[1][3][0][2] == color or cube[1][0][0][0] == color or cube[0][1][0][0] == color:
            return True

    elif coordinate_white_or_yellow == (1, 3, 2, 0):
        if cube[1][3][2][0] == color or cube[2][1][2][2] == color or cube[1][2][2][2] == color:
            return True

    elif coordinate_white_or_yellow == (1, 3, 2, 2):
        if cube[1][3][2][2] == color or cube[2][1][2][0] == color or cube[1][0][2][0] == color:
            return True





    else:
        return "Nunca llego a un case "

    return False

def white_corners_get_down(cube):
    """
    Vamos a chequear si hay piezas blancas en las esquinas de arriba. Vamos a bajarlas, para tenerlas todas abajo, y ahi empezar con la operacion rotativa.
    Tenemos que saber chequear
    """

    """
    El problema que tengo, es que subo una pieza sin blanco para arriba, y las 4 que quedan abajo, son blancas, no logra subir la pieza.  
    tenemos que hacer el test de si puede subir, no cuando esta abajo, sino preventivamente. 
    eso pasa si no ves al futuro. 
    RESUELTO
    """





    # if cube[1][1][0][0] == w or cube[1][0][0][2] == w or cube[0][1][2][0] == w: # arriba izquierda
    if does_corner_have_color((1, 1, 0, 0)):
        # pieza tiene blanco, bajala.
        # solo deberiamos bajar esta pieza, si la pieza que se encuentra abajo derecha no tiene blanco.
        while does_corner_have_color((1, 3, 0, 0)):
            Clockturn(Downface)
        AntiClockturn(Leftface)
        Clockturn(Downface)
        # en el momoento que en esa pieza no hay ningun blanco contaminado, puedo volver a subir esto, puramente.
        Clockturn(Leftface)


    # if cube[1][1][0][2] == w or cube[0][1][2][2] == w or cube[1][2][0][0] == w:     # arriba derecha
    if does_corner_have_color((1, 1, 0, 2)):
        # pieza tiene blanco, bajala.
        while does_corner_have_color((1, 3, 2, 0)):
            Clockturn(Downface)
        AntiClockturn(Backface)
        Clockturn(Downface)
        Clockturn(Backface)


    # if cube[1][1][2][0] == w or cube[1][0][2][2] == w or cube[2][1][0][0]: # abajo izquierda
    if does_corner_have_color((1, 1, 2, 0)):
        # pieza tiene blanco, bajala.
        while does_corner_have_color((1, 3, 2, 0)):
            Clockturn(Downface)
        Clockturn(Leftface)
        AntiClockturn(Downface)
        AntiClockturn(Leftface)


    # if cube[1][1][2][2] == w or cube[2][1][0][2] == w or cube[1][2][2][0] == w: # abajo derecha
    if does_corner_have_color((1, 1, 2, 2)):
        # pieza tiene blanco, bajala.
        while does_corner_have_color((1, 3, 2, 2)):
            Clockturn(Downface)
        AntiClockturn(Rightface)
        Clockturn(Downface)
        Clockturn(Rightface)
    return cube

    # avia vug, ya no hay, por lo menos no con cubo perfecto

def algoritmo_abajo_izquierda_arriba_derecha(currentface, white_is_up=False):
    """
    Abajo
    izquierda
    arriba
    derecha
    """
    northneighbor, eastneighbor, southneighbor, westneighbor = reference_coordinate(currentface, white_is_up)
    AntiClockturn(eastneighbor)
    AntiClockturn(southneighbor)
    Clockturn(eastneighbor)
    Clockturn(southneighbor)
    # el problema esta con la funcion reference_coordinate

def algoritmo_abajo_azq_arri_der_alternativa(currentface, white_is_up=True):
    northneighbor, eastneighbor, southneighbor, westneighbor = reference_coordinate(currentface, white_is_up=white_is_up)
    Clockturn(currentface)
    Clockturn(southneighbor)
    AntiClockturn(currentface)


def white_corners(cube):
    while not (cube[1][1][0][0] == w and cube[1][1][0][2] == w and cube[1][1][2][0] == w and cube[1][1][2][2]) == w:
        """
        Frontface is frontface.             
        """
        if does_corner_have_color((1, 3, 2, 0), r) and does_corner_have_color((1, 3, 2, 0), b) and does_corner_have_color((1, 3, 2, 0), w):
            # print("Empezar subicion de blue con rojo")
            while not (cube[1][1][2][2] == w and does_corner_have_color((1, 1, 2, 2), r) and does_corner_have_color((1, 1, 2, 2), b)):
                if cube[2][1][2][2] == w:
                    algoritmo_abajo_azq_arri_der_alternativa(Redface, white_is_up=True)
                    print("una cosa bonita")
                else:
                    algoritmo_abajo_izquierda_arriba_derecha(Redface, white_is_up=True)
            # print("Terminada la subicion de blue con rojo")

        if does_corner_have_color((1, 3, 2, 2), g) and does_corner_have_color((1, 3, 2, 2), r) and does_corner_have_color((1, 3, 2, 2), w):
            # print("Empezar subicion de green con rojo")
            while not (cube[1][1][2][0] == w and does_corner_have_color((1, 1, 2, 0), g) and does_corner_have_color((1, 1, 2, 0), r)):
                if cube[1][0][2][0] == w:
                    algoritmo_abajo_azq_arri_der_alternativa(Greenface, white_is_up=True)
                    print("una cosa bonita")
                else:
                    algoritmo_abajo_izquierda_arriba_derecha(Greenface, white_is_up=True)
            # print("Terminada la subicion de green con rojo")

        if does_corner_have_color((1, 3, 0, 2), g) and does_corner_have_color((1, 3, 0, 2), o) and does_corner_have_color((1, 3, 0, 2), w):
            # print("Empezar subicion de green con orange")
            while not (cube[1][1][0][0] == w and does_corner_have_color((1, 1, 0, 0), g) and does_corner_have_color((1, 1, 0, 0), o)):
                if cube[0][1][0][0] == w:
                    algoritmo_abajo_azq_arri_der_alternativa(Orangeface, white_is_up=True)
                    print("una cosa bonita")
                else:
                    algoritmo_abajo_izquierda_arriba_derecha(Orangeface, white_is_up=True)
            # print("Terminada la subicion de green con orange")

        if does_corner_have_color((1, 3, 0, 0), b) and does_corner_have_color((1, 3, 0, 0), o) and does_corner_have_color((1, 3, 0, 0), w):
            # print("Empezar subicion de blue con orange")
            while not (cube[1][1][0][2] == w and does_corner_have_color((1, 1, 0, 2), b) and does_corner_have_color((1, 1, 0, 2), o)):

                if cube[1][2][0][2] == w:
                    algoritmo_abajo_azq_arri_der_alternativa(Blueface, white_is_up=True)
                    print("una cosa bonita")
                else:
                    algoritmo_abajo_izquierda_arriba_derecha(Blueface, white_is_up=True)
            # print("Terminada la subicion de blue con orange")

        Clockturn(Downface)


def second_layer(cube):
    """
    Si la pieza va a la izquierda,

    aristas = (
        (r, g),
        (o, b),
        (o, g),
        (b, r))
    """


    def algorithm_second_layer(current_face, turn_dir):
        northneighbor, eastneighbor, southneighbor, westneighbor = reference_coordinate(current_face)


        # current_face = la que iria en el front
        if turn_dir == "Right":
            Clockturn(northneighbor)
            Clockturn(eastneighbor)
            AntiClockturn(northneighbor)
            AntiClockturn(eastneighbor)
            AntiClockturn(northneighbor)
            AntiClockturn(current_face)
            Clockturn(northneighbor)
            Clockturn(current_face)

        elif turn_dir == "Left":
            AntiClockturn(northneighbor)
            AntiClockturn(westneighbor)
            Clockturn(northneighbor)
            Clockturn(westneighbor)
            Clockturn(northneighbor)
            Clockturn(current_face)
            AntiClockturn(northneighbor)
            AntiClockturn(current_face)


        return northneighbor, eastneighbor, southneighbor, westneighbor


    cubebroken = 0
    while not (cube[1][2][0][1] == b and cube[1][2][2][1] == b and cube[1][0][0][1] == g and cube[1][0][2][1] == g and cube[2][1][1][0] == r and cube[2][1][1][2] == r and cube[0][1][1][0] == o and cube[0][1][1][2] == o): # while second layer not ready
        if cube[1][2][1][2] == b:
            if cube[1][3][1][0] == r:
                print("Bluered")
                algorithm_second_layer(Blueface, "Right")
                cubebroken = 0


            elif cube[1][3][1][0] == o:
                print("Blueorange")
                algorithm_second_layer(Blueface, "Left")
                cubebroken = 0



        if cube[0][1][0][1] == o:
            if cube[1][3][0][1] == g:
                print("Orangegreen")
                algorithm_second_layer(Orangeface, "Left")
                cubebroken = 0

            elif cube[1][3][0][1] == b:
                print("Orangeblue")
                algorithm_second_layer(Orangeface, "Right")
                cubebroken = 0


        if cube[1][0][1][0] == g:
            if cube[1][3][1][2] == r:
                print("Greenred")
                algorithm_second_layer(Greenface, "Left")
                cubebroken = 0

            elif cube[1][3][1][2] == o:
                print("Greenorange")
                algorithm_second_layer(Greenface, "Right")
                cubebroken = 0

        if cube[2][1][2][1] == r:
            if cube[1][3][2][1] == b:
                print("Redblue")
                algorithm_second_layer(Redface, "Left")
                cubebroken = 0

            elif cube[1][3][2][1] == g:
                print("Redgreen")
                algorithm_second_layer(Redface, "Right")
                cubebroken = 0

        cubebroken += 1
        Clockturn(Downface)

        if cubebroken >= 4:
            cubebroken = 0


            if not (cube[1][0][2][1] == g and cube[2][1][1][0] == r):
                algorithm_second_layer(Redface, "Right")

            if not (cube[2][1][1][2] == r and cube[1][2][2][1] == b):
                algorithm_second_layer(Blueface, "Right")

            if not (cube[1][2][0][1] == b and cube[1][0][1][2] == o):
                algorithm_second_layer(Orangeface, "Right")

            if not (cube[1][0][1][0] == o and cube[1][0][0][1] == g):
                algorithm_second_layer(Greenface, "Right")


def yellow_cross(cube):
    def algorithm_yellowcross(currentface):
        northneighbor, eastneighbor, southneighbor, westneighbor = reference_coordinate(currentface)

        Clockturn(currentface)
        Clockturn(eastneighbor)
        Clockturn(northneighbor)
        AntiClockturn(eastneighbor)
        AntiClockturn(northneighbor)
        AntiClockturn(currentface)

    while not (cube[1][3][1][0] == y and cube[1][3][1][2] == y and cube[1][3][0][1] == y and cube[1][3][2][1] == y):
        # el triangulo es a la derecha

        # deberiamos ir de mas perfecto a mas mierda, para que no haya la posibilidad de que se escape.
        # cube[1][3][1][2]
        # cube[1][3][1][0]
        # cube[1][3][0][1]
        # cube[1][3][2][1]

        # Linen rectas:
        if cube[1][3][1][0] == y and cube[1][3][1][2] == y:
            algorithm_yellowcross(Redface)
            continue # aqui salto, para que las prioridades bajas no caguen el perfecto.

        elif cube[1][3][0][1] == y and cube[1][3][2][1] == y:
            algorithm_yellowcross(Blueface)
            continue # aqui salto, para que las prioridades bajas no caguen el perfecto.


        # Die vier Dreiecke:
        if cube[1][3][1][0] == y and cube[1][3][2][1] == y:
            algorithm_yellowcross(Blueface)

        elif cube[1][3][2][1] == y and cube[1][3][1][2] == y:
            algorithm_yellowcross(Redface)

        elif cube[1][3][1][2] == y and cube[1][3][0][1] == y:
            algorithm_yellowcross(Greenface)

        elif cube[1][3][0][1] and cube[1][3][1][0] == y:
            algorithm_yellowcross(Orangeface)

        # Punkt in der Mitte
        if cube[1][3][1][0] != y and cube[1][3][1][2] != y and cube[1][3][0][1] != y and cube[1][3][2][1] != y:
            algorithm_yellowcross(Redface)
            algorithm_yellowcross(Redface)

def aristas_yellowcross(cube):
    # lugares relevantes para este movimiento revolucionario:
    # cube[Blueface[0]][Blueface[1]][2][1]
    # cube[Greenface[0]][Greenface[1]][1][2]
    # cube[Redface[0]][Redface[1]][1][0]
    # cube[Orangeface[0]][Blueface[1]][0][1]
    def yellowcross_algorithm(currentface):

        print("Aplico Funcion ***************************************")
        northneighbor, eastneighbor, southneighbor, westneighbor = reference_coordinate(currentface)

        Clockturn(eastneighbor)
        Clockturn(northneighbor)
        AntiClockturn(eastneighbor)
        Clockturn(northneighbor)
        Clockturn(eastneighbor)
        Clockturn(northneighbor)
        Clockturn(northneighbor)
        AntiClockturn(eastneighbor)
        Clockturn(northneighbor)


    while not (cube[Blueface[0]][Blueface[1]][1][2] == b and cube[Greenface[0]][Greenface[1]][1][0] == g and cube[Redface[0]][Redface[1]][2][1] == r and cube[Orangeface[0]][Orangeface[1]][0][1] == o):



        # preparation of two parallel lines.
        if cube[Blueface[0]][Blueface[1]][1][2] == b and cube[Greenface[0]][Greenface[1]][1][0] == g:
            yellowcross_algorithm(Greenface)
            Clockturn(Upface) # esto hace sentido?
            # Google: R U R' U R U2 R' U y2 U y' R U R' U R U2 R' U

        elif cube[Redface[0]][Redface[1]][2][1] == r and cube[Orangeface[0]][Orangeface[1]][0][1] == o:
            yellowcross_algorithm(Orangeface)
            Clockturn(Upface)
            # Google: R U R' U R U2 R' U y2 U y' R U R' U R U2 R' U


        # el problema empieza cuando, las aristas no estan nebenan.
        if cube[Blueface[0]][Blueface[1]][1][2] == b and cube[Redface[0]][Redface[1]][2][1] == r:
            yellowcross_algorithm(Orangeface)
            continue


        elif cube[Blueface[0]][Blueface[1]][1][2] == b and cube[Orangeface[0]][Orangeface[1]][0][1] == o:
            yellowcross_algorithm(Greenface)
            continue


        elif cube[Greenface[0]][Greenface[1]][1][0] == g and cube[Redface[0]][Redface[1]][2][1] == r:
            yellowcross_algorithm(Blueface)
            continue


        elif cube[Greenface[0]][Greenface[1]][1][0] == g and cube[Orangeface[0]][Orangeface[1]][0][1] == o:
            yellowcross_algorithm(Redface)
            continue

        Clockturn(Downface)

def esquinas_yellowcross(cube):
    def check_everything_in_place():
        if does_corner_have_color((1, 3, 2, 0), b) and does_corner_have_color((1, 3, 2, 0), r):
            if does_corner_have_color((1, 3, 0, 0), b) and does_corner_have_color((1, 3, 0, 0), o):
                if does_corner_have_color((1, 3, 2, 2), g) and does_corner_have_color((1, 3, 2, 2), r):
                    if does_corner_have_color((1, 3, 0, 2), g) and does_corner_have_color((1, 3, 0, 2), o):
                        return True
        return False

    def algoritmo_intercambiar_esquinas_en_triangulo(currentface):
        northface, eastface, southface, westface = reference_coordinate(currentface, white_is_up=False)
        Clockturn(northface)
        Clockturn(eastface)
        AntiClockturn(northface)
        AntiClockturn(westface)
        Clockturn(northface)
        AntiClockturn(eastface)
        AntiClockturn(northface)
        Clockturn(westface)
        print("Algoritmo ejecuto. ")

    while not check_everything_in_place():

        if does_corner_have_color((1, 3, 2, 0), b) and does_corner_have_color((1, 3, 2, 0), r):
            algoritmo_intercambiar_esquinas_en_triangulo(Blueface)

        elif does_corner_have_color((1, 3, 0, 0), b) and does_corner_have_color((1, 3, 0, 0), o):
            algoritmo_intercambiar_esquinas_en_triangulo(Orangeface)

        elif does_corner_have_color((1, 3, 2, 2), g) and does_corner_have_color((1, 3, 2, 2), r):
            algoritmo_intercambiar_esquinas_en_triangulo(Redface)

        elif does_corner_have_color((1, 3, 0, 2), g) and does_corner_have_color((1, 3, 0, 2), o):
            algoritmo_intercambiar_esquinas_en_triangulo(Greenface)

        else:
            # dale cualquiera papi
            algoritmo_intercambiar_esquinas_en_triangulo(Greenface)


    # la pieza deberia preguntar, que colores tiene, y a partir de eso, informar y confirmar con el color de la cara que podemos saber facilmente.


def yellowface_orientar_esquinas(cube):
    while cube[1][3][0][0] != y:
        algoritmo_abajo_izquierda_arriba_derecha(Orangeface, white_is_up=False)
    Clockturn(Downface)
    while cube[1][3][0][0] != y:
        algoritmo_abajo_izquierda_arriba_derecha(Orangeface, white_is_up=False)
    Clockturn(Downface)
    while cube[1][3][0][0] != y:
        algoritmo_abajo_izquierda_arriba_derecha(Orangeface, white_is_up=False)
    Clockturn(Downface)
    while cube[1][3][0][0] != y:
        algoritmo_abajo_izquierda_arriba_derecha(Orangeface, white_is_up=False)

def terminar_cube(cube):
    while cube[2][1][0][1] != cube[2][1][1][1]:
        Clockturn(Upface)

    while cube[2][1][1][1] != cube[2][1][2][1]:
        Clockturn(Downface)





cubedict = {
    "scrambled rubix": [
        [[], [['red', 'yellow', 'white'], ['orange', 'orange', 'yellow'], ['green', 'red', 'blue']], [], []],

        [[['blue', 'white', 'red'], ['green', 'green', 'blue'], ['yellow', 'white', 'yellow']],
         [['white', 'blue', 'yellow'], ['white', 'white', 'orange'], ['green', 'blue', 'blue']],
         [['orange', 'green', 'orange'], ['yellow', 'blue', 'red'], ['red', 'white', 'white']],
         [['green', 'blue', 'yellow'], ['yellow', 'yellow', 'red'], ['orange', 'green', 'green']]],

        [[], [['red', 'orange', 'white'], ['red', 'red', 'green'], ['orange', 'orange', 'blue']], [], []]]




    ,"solved rubix": [
        [[], [["orange", "orange", "orange"], ["orange", "orange", "orange"], ["orange", "orange", "orange"]], [], []],

        [[["green", "green", "green"], ["green", "green", "green"], ["green", "green", "green"]],
         [["white", "white", "white"], ["white", "white", "white"], ["white", "white", "white"]],
         [["blue", "blue", "blue"], ["blue", "blue", "blue"], ["blue", "blue", "blue"]],
         [["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"]]],

        [[], [["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]], [], []],
    ],
    "experimento":
        [[[], [['orange', 'red', 'white'], ['orange', 'orange', 'yellow'], ['red', 'red', 'green']], [], []], [[['green', 'white', 'yellow'], ['blue', 'green', 'green'], ['white', 'yellow', 'yellow']], [['blue', 'blue', 'white'], ['red', 'white', 'red'], ['green', 'green', 'orange']], [['orange', 'blue', 'red'], ['yellow', 'blue', 'green'], ['yellow', 'green', 'white']], [['blue', 'white', 'yellow'], ['orange', 'yellow', 'white'], ['orange', 'blue', 'green']]], [[], [['red', 'white', 'blue'], ['orange', 'red', 'yellow'], ['red', 'orange', 'blue']], [], []]]
}








cube = cubedict["solved rubix"]
cubemuster()

print("scramblin")
random_scrambler(cube)
despues_scramble = copy.deepcopy(cube)
cubemuster()


print("Cruz blanca al rededor de punto Amarillo: ")
yellow_dot_white_cross(cube)
cubemuster()

print("Cruz blanca y aristas: ")
white_cross(cube)
cubemuster()

print("Bajar white corners")
white_corners_get_down(cube)
cubemuster()

print("Meter y orientar white corners: ")
white_corners(cube)
cubemuster()

print("Second Layer: ")
second_layer(cube)
cubemuster()

print("Yellow Cross: ")
yellow_cross(cube)
cubemuster()

print("Aristas en yellowcros: ")
aristas_yellowcross(cube)
cubemuster()

print("Esquinas en yellowlayer:" )
esquinas_yellowcross(cube)
cubemuster()

print("Orientar esquinas: ")
yellowface_orientar_esquinas(cube)
cubemuster()


print("Terminar cube lineas horizontales: ")
terminar_cube(cube)
cubemuster()

print("Zwischen das Verdrehen und loesen des Wuerfels wuerden so viele drehungen gemacht", drehungen)
print("Der Wuerfel sah so aus, genau nach der verdrehung:", despues_scramble)


"""Tips:
Ki: 6 fotos son suficiente, yo ya se cual es el del medio.
Vamos a poner las fotos en frente del user en un tkinter window. Donde encima de eso van a tener un grid de como deberia 
estar posicionado el cubo, ellos van a arrastrar la imagen al centro, y van a hacer el upscaling. Cuando yo ya tenga la certeza 
de que la imagen esta centrada, analizo los colores y chao pescado. 
"""





"""Geschichte: 
1: Para optimizar cantidad de drehungen, abajo izquierda arriba derecha mejorar. Lo hicimos. 
el code tiene el problema, que el clause que aniadi, no lo hace eficiente siempre, sino solo a veces. investigalo wudi. -> ya lo investigue.
vi un trend muy general, que en el 99 porciento de los casos, el clause que aniadi, reduce la  longitud del movidas mas que substancialmente
Ya integre un algoritmo, que siempre que haya una pieza blanca mirando para ti se aplica directamente. Como antes, se tenian que hacer 20 movimientos en abajo izquierda arriba derecha para meter una pieza que estaba
viendo para adelante, para que caiga en su puesto, y ahora solamente son 3, la cantidad de movimientos que son necesarios para um den zauberwuerfel zu loesen ist sehr stark vermindert. Normalerweise um ein faktor von 17, 
aber es ist auch sehr haufig der fall, dass es eine kleine oder eine grosse abweichung von 17 gibt, da wenn ich diese zwei verschiede algorithmen anwende, ist die ganze struktur vom wuerfel brutal geaendert. 
Die meiste male, macht es dass der wuerfel schneller loesbar ist, aber manchmal, geneiert es ein chaos in der struktur des wuerfels und es aendert die orientierung von etwas, was ich nicht erkennen kann, 
und deswegen, ist es der fall bei einer minderheit, dass es trotz verschnellerung langsamer am ende geht. es kann auch der fall sein dass es noch schneller als den fortschritt wird, weil ich etwas entknotet habe, was ich 
spaeter haette machen muessen. 
In manche faelle, gibt es sogar kein unterschied, und alles geht gleich, da es nicht mal die chance gab, dieses neue algorithmus anzuwenden.  
"""



"""Verbesserungsvorschlaege: 
Guidelines: No importa la eficiencia del code, lo que importa es cantidad de movidas, y entendimiento para mi.
1, Problema con dos respuestas: 
    1: Para evitar movimientos tontos, vamos a hacer que los movimientos se hacen 4 despues de lo que dice el codigo, y que si el codigo propone algo tonto y redundante, que no lo ejecute y que siga leyendo lo que el codigo propondria, para no hacer
    clock anticlock o para no hacer clock clock clock clock. 
    
    2: Al final del code vamos a encontrar una manera, de hacer un array paralelo, que podemos editar, sin editar el principal, 
    con ese podemos hacer experimentos paralelos para acortar la cantidad de movimiento que hacemos en total. 
    Eso lo hacemos para no hacer 3 veces a la derecha en vez de una vez a la izqueirda. 
    
2, Problema: En la definicion de la funcion Clockwise y anticlockwise, tengo una un caso para cada cara, muy ineficiente. Encuentra la manera, de hacer las aristas de una manera natural y programatica.

3, Cuando estas metiendo las esquinas blancas a su  lugar, y la orientacion de la esquina esta viendo para abajo, se hace un disparate tonto. No hay un algoritmo, como abajo iquierda arriba derecha que optimize esa parte?
    Es una de las partes mas ineficiente del code. 

"""
print(time.time()-inittime)