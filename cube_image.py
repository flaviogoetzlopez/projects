import numpy, cv2


print("Press space when alligned and followed instructions")


decoded_cube = [
    [[], [['', '', ''], ['', '', ''], ['', '', '']], [], []],

    [[['', '', ''], ['', '', ''], ['', '', '']],
     [['', '', ''], ['', '', ''], ['', '', '']],
     [['', '', ''], ['', '', ''], ['', '', '']],
     [['', '', ''], ['', '', ''], ['', '', '']]],

    [[], [['', '', ''], ['', '', ''], ['', '', '']], [], []]]

color_ranges = {
'lower_blue': numpy.array([90, 50, 50]), # in app 180, 20, 20
'upper_blue':numpy.array([130, 255, 255]), # in app 260, 100, 100
'lower_red_rechts': numpy.array([160, 50, 50]), # 320, 20, 20
'upper_red_rechts': numpy.array([179, 255, 255]), # 360, 100, 100
'lower_red_links': numpy.array([0, 50, 50]), # 0, 20, 20
'upper_red_links': numpy.array([3, 255, 255]), # 16, 100, 10 # has gotten corrected.
'lower_orange': numpy.array([5, 50, 50]), # 20, 20, 20 # has gotten corrected
'upper_orange': numpy.array([20, 255, 255]), # 40, 100, 100
'lower_yellow': numpy.array([25, 50, 50]), # 50, 20, 20
'upper_yellow': numpy.array([32, 255, 255]), # 64, 100, 100
'lower_green': numpy.array([40, 50, 50]), # 80, 20, 20
'upper_green': numpy.array([88, 255, 255]), # 176, 100, 100
'lower_white': numpy.array([0, 0, 150]), # lo mas blanco 70 * 255
'upper_white': numpy.array([179, 40, 255]), # lo mas negro # 100
}

cap = cv2.VideoCapture(0)
didwork, frame = cap.read()
frame = cv2.resize(frame, (0, 0), fx=1.3, fy=1.3)
# print(frame.shape) #(624, 832, 3)
# defining poinit in cube for simplicity
len_side_cube = frame.shape[0] // 2 # the half of the height.
start_pos_x, start_pos_y = frame.shape[1]//2 - len_side_cube//2, len_side_cube // 2
extrema_cube_x, extrema_cube_y = start_pos_x + len_side_cube, start_pos_y + len_side_cube
WIDTH, HEIGHT = frame.shape[1], frame.shape[0]
len_mini_cube = len_side_cube // 3
half_len_mini_cube = len_mini_cube // 2
mitte_mitte_1_1 = (WIDTH//2, HEIGHT//2)
mitte_oben_0_1 = (WIDTH //2, start_pos_y + half_len_mini_cube)
mitte_unten_2_1 = (WIDTH // 2, round(start_pos_y + len_mini_cube * 2.5))

rechts_mitte_1_2 = (start_pos_x + round(len_mini_cube * 2.5), HEIGHT//2)
rechts_oben_0_2 = (start_pos_x + round(len_mini_cube * 2.5), start_pos_y + half_len_mini_cube)
rechts_unten_2_2 = (start_pos_x + round(len_mini_cube * 2.5), round(start_pos_y + len_mini_cube * 2.5))

links_mitte_1_0 = (start_pos_x+half_len_mini_cube, HEIGHT//2)
links_oben_0_0 = (start_pos_x+half_len_mini_cube, start_pos_y + half_len_mini_cube)
links_unten_2_0 = (start_pos_x+half_len_mini_cube, round(start_pos_y + len_mini_cube * 2.5))

liste_pixels = (links_oben_0_0, mitte_oben_0_1, rechts_oben_0_2, links_mitte_1_0, mitte_mitte_1_1, rechts_mitte_1_2, links_unten_2_0, mitte_unten_2_1, rechts_unten_2_2)

size_minicube = 90
entire_cube = numpy.zeros((3 * size_minicube, 4 * size_minicube, 3), dtype=numpy.uint8) # the standard data type, was either 1 or 0, now i can have ranges. # 180 is width
while True:
    didwork, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=1.3, fy=1.3)





    key_pressed = cv2.waitKey(1)
    if key_pressed == ord('q'):
        break

    if key_pressed == ord(" "):
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



        frame_reduced = numpy.array([[frame[height][width] for (width, height) in liste_pixels]]) # a picture of the 9 relevant pixels.
        frame_reduced = frame_reduced.reshape((3, 3, 3))
        hsv_reduced = cv2.cvtColor(frame_reduced, cv2.COLOR_BGR2HSV)

        cv2.imshow("Image Artistic", cv2.resize(frame_reduced, (150, 150)))
        len_cube_drittel = 50
        created_cube_image = numpy.zeros((3*len_cube_drittel, 3*len_cube_drittel, 3), dtype=numpy.uint8) # the standard data type, was either 1 or 0, now i can have ranges.



        # cv2.imshow("hsv to analyze", frame_reduced)

        yellowmask = cv2.inRange(hsv_reduced, color_ranges["lower_yellow"], color_ranges["upper_yellow"])
        greenmask = cv2.inRange(hsv_reduced, color_ranges['lower_green'], color_ranges['upper_green'])
        linksredmask = cv2.inRange(hsv_reduced, color_ranges['lower_red_links'], color_ranges['upper_red_links'])
        rechtsredmask = cv2.inRange(hsv_reduced, color_ranges['lower_red_rechts'], color_ranges['upper_red_rechts']) # i analyzed the image output from this image, and this one is the useful, links is only a decoy.
        redmask = cv2.bitwise_or(rechtsredmask, linksredmask)
        orangemask = cv2.inRange(hsv_reduced, color_ranges['lower_orange'], color_ranges['upper_orange'])
        whitemask = cv2.inRange(hsv_reduced, color_ranges['lower_white'], color_ranges['upper_white'])
        bluemask = cv2.inRange(hsv_reduced, color_ranges['lower_blue'], color_ranges['upper_blue'])

        list_pieces = [['', '', ''], ['', '', ''], ['', '', '']]
        for index, (width, height) in enumerate(liste_pixels):
            # blueColor, greenColor, redColor = frame[height][width]

            # to fix problem i might not conrevrt the entire image to special color but only pixel,
            # i might also analyze the surrounding 3 pixels around, so that i have a bigger sample size if idiot chickens out

            # now i dont convert entire images, but only some relevant pixels.
            color_tu_paint = (0, 0, 0)
            print(f"In index [{index // 3}, {index % 3}]. ", end="")
            if redmask[index//3][index%3]:
                print("Es ist Rot ", end="")
                list_pieces[index//3][index%3] = 'red'
                color_to_paint = (0, 0, 255)
            if bluemask[index//3][index%3]:
                print("Es ist Blau ", end="")
                list_pieces[index//3][index%3] = 'blue'
                color_to_paint = (255, 0, 0)
            if greenmask[index//3][index%3]:
                print("Es ist Gruen ", end="")
                list_pieces[index//3][index%3] = 'green'
                color_to_paint = (0, 255, 0)
            if yellowmask[index//3][index%3]:
                print("Es ist Gelb ", end="")
                list_pieces[index//3][index%3] = 'yellow'
                color_to_paint = (0, 255, 255)
            if orangemask[index//3][index%3]:
                print("Es ist Orange ", end="")
                list_pieces[index//3][index%3] = 'orange'
                color_to_paint = (0, 128, 255)
            if whitemask[index//3][index%3]:
                print("Es ist weiss ", end="")
                list_pieces[index//3][index%3] = 'white'
                color_to_paint = (255, 255, 255)
            print()


            # cv2.rectangle(created_cube_image, (((index//3) * 100), (index%3) * 100), (((index//3) * 100) + 100, (index%3) * 100+100), color_to_paint, -1)
            print(list_pieces)
            cv2.rectangle(created_cube_image, (((index%3) * len_cube_drittel), (index//3) * len_cube_drittel), (((index%3) * len_cube_drittel) + len_cube_drittel, (index//3) * len_cube_drittel+len_cube_drittel), color_to_paint, -1)
            color_to_paint = (0, 0, 0)
            cv2.imshow("Current Face", created_cube_image)



        # all_correct = input("All correct? (y/n)").casefold()
        print("All correct? (y/n)")
        if cv2.waitKey(-1) == ord('y'):

            # if 'y' == all_correct:
            # size_minicube = entire_cube[0] // 3
            created_cube_image = cv2.resize(created_cube_image, (size_minicube, size_minicube))
            match list_pieces[1][1]:
                case 'white':
                    decoded_cube[1][1] = list_pieces
                    entire_cube[size_minicube:2 * size_minicube,size_minicube:2*size_minicube] = created_cube_image
                case 'yellow':
                    decoded_cube[1][3] = list_pieces
                    entire_cube[size_minicube:2 * size_minicube,3 * size_minicube:] = created_cube_image
                case 'blue':
                    decoded_cube[1][2] = list_pieces
                    entire_cube[size_minicube:2*size_minicube,2*size_minicube:3*size_minicube] = created_cube_image
                case 'green':
                    decoded_cube[1][0] = list_pieces
                    entire_cube[size_minicube:2 * size_minicube,:size_minicube] = created_cube_image
                case 'orange':
                    decoded_cube[0][1] = list_pieces
                    entire_cube[:size_minicube,size_minicube:2*size_minicube] = created_cube_image
                case 'red':
                    decoded_cube[2][1] = list_pieces
                    entire_cube[2*size_minicube:,size_minicube:2 * size_minicube] = created_cube_image



            print("Cube status", decoded_cube)
            cv2.imshow("Entire Cube", entire_cube)

            ready = True
            for seite in (decoded_cube[0][1], decoded_cube[1][0], decoded_cube[1][1], decoded_cube[1][2], decoded_cube[1][3], decoded_cube[2][1]):
                for linie in seite:
                    for farbe in linie:
                        if farbe not in ("white", "yellow", "blue", "green", "orange", "red"):
                            ready = False
            if ready == True:
                print("Fertig! Naechster Schritt. ")



        if cv2.waitKey(1) == ord('n'):
            print("Now take correct picture. ")
            list_pieces = [['', '', ''], ['', '', ''], ['', '', '']] # if there was problem with picture and user doesnt like it, reset list, and dont assign.




    # we pushed these blocks of code to the bottom, because else our hsv image gets distorted
    for center in liste_pixels:
        cv2.circle(frame, center, 10, (128, 128, 128), -1)

    cv2.rectangle(frame, (start_pos_x, start_pos_y), (start_pos_x + len_side_cube, start_pos_y + len_side_cube), (0, 0, 0), 5)
    cv2.line(frame, (start_pos_x + len_side_cube // 3, start_pos_y), (start_pos_x + len_side_cube // 3, extrema_cube_y), (0, 0, 0), 5) # vertical first #  x * 2/3 == x // 1.5
    cv2.line(frame, (int(start_pos_x + (len_side_cube // 1.5)), start_pos_y), (int(start_pos_x + (len_side_cube // 1.5)), extrema_cube_y), (0, 0, 0), 5) # vertical second
    cv2.line(frame, (start_pos_x, start_pos_y + len_side_cube // 3), (extrema_cube_x, start_pos_y + len_side_cube // 3), (0, 0, 0), 5) # horizontal first
    cv2.line(frame, (start_pos_x, int(start_pos_y + len_side_cube // 1.5)), (extrema_cube_x, int(start_pos_y + len_side_cube // 1.5)), (0, 0, 0), 5) # horizontal second



    # cv2.imshow("Redleft", linksredmask) # we combined red links and red rechts damit es beeide ranges akzeptiert, obwohl der einzige der relevant ist ist rechts
    # cv2.imshow("Redright", rechtsredmask)
    # cv2.imshow("Redbitwise", bluemask)
    cv2.imshow("Video", frame)


cap.release()
cv2.destroyAllWindows()





"""In diesem moment koennen wir punkte identifizieren.
Wir koennen punkt in die mitte des wuerfels erkennen.
wir nehmen nur ein pixel, in die relevante punkte.
und converten zu hsv, dann koennen wir ueberpruefen.
"""





"""The three ways, that i can find the color of the cube are following:

1: sin esquinas, encontrando los masks y los colores que son grob, probablemente vamos  a tener que encontrarlo con los masks.
2: jetzt dass ich es schaffe, ordnung in den listen zu generieren, werde ich einfach vier punkte erstellen, und davon ein gitter generieren
3: ich werde eienfach zum letzten und ersten punkt, dann nehme ich meine referenzen im kontext dazu. nicht jeden punkt, einfach -> und <-

"""




# import pyautogui, PIL
# import numpy, cv2
#
# mybild = cv2.imread("Assets/Bild_rubix.png", cv2.IMREAD_COLOR)
# hsv = cv2.cvtColor(mybild, cv2.COLOR_BGR2HSV)
# # um Farbe von HSV von App zu HSV von cv2 muss man H/2 S/255*100 V/255*100
# lower_blue = numpy.array([90, 50, 50]) # in app 180, 20, 20
# upper_blue = numpy.array([130, 255, 255]) # in app 260, 100, 100
#
# lower_red_rechts = numpy.array([160, 50, 50]) # 320, 20, 20
# upper_red_rechts = numpy.array([179, 255, 255]) # 360, 100, 100
#
# lower_red_links = numpy.array([0, 50, 50]) # 0, 20, 20
# upper_red_links = numpy.array([8, 255, 255]) # 16, 100, 10
#
# lower_orange = numpy.array([10, 50, 50]) # 20, 20, 20
# upper_orange = numpy.array([20, 255, 255]) # 40, 100, 100
#
# lower_yellow = numpy.array([25, 50, 50]) # 50, 20, 20
# upper_yellow = numpy.array([32, 255, 255]) # 64, 100, 100
#
# lower_green = numpy.array([40, 50, 50]) # 80, 20, 20
# upper_green = numpy.array([70, 255, 255]) # 140, 100, 100
#
# lower_white = numpy.array([0, 0, 210]) # lo mas blanco 80 * 255
# upper_white = numpy.array([179, 20, 255]) # lo mas negro # 100
#
# mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#
#
# result = cv2.bitwise_and(mybild, mybild, mask=mask)
# # mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
# # mask = cv2.inRange(hsv, lower_green, upper_green)
# # mask = cv2.inRange(hsv, lower_red_links, upper_red_links)
# # mask = cv2.inRange(hsv, lower_orange, upper_orange)
# # mask = cv2.inRange(hsv, lower_white, upper_white)
# print(f"shape is: height, width{mybild.shape}")
#
# HEIGHT = mybild.shape[0]
# WIDTH = mybild.shape[1]
#
#
# mitte_mitte_1_1 = (WIDTH//2, HEIGHT//2)
# mitte_oben_0_1 = (WIDTH //2, HEIGHT * 1//6)
# mitte_unten_2_1 = (WIDTH // 2, HEIGHT * 5//6)
#
# rechts_mitte_1_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT//2)
# rechts_oben_0_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT * 1//6)
# rechts_unten_2_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT * 5//6)
#
# links_mitte_1_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT//2)
# links_oben_0_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT * 1//6)
# links_unten_2_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT * 5//6)
# liste_pixels = (links_oben_0_0, mitte_oben_0_1, rechts_oben_0_2, links_mitte_1_0, mitte_mitte_1_1, rechts_mitte_1_2, links_unten_2_0, mitte_unten_2_1, rechts_unten_2_2)
#
# for width, height in liste_pixels:
#     blueColor, greenColor, redColor = mybild[height][width]
#     h, s, v = hsv[height][width]
#
#     print("Coordinates:", width, height, "RGB", redColor, greenColor, blueColor, "\t\tHSV", h, s, v, end="")
#     mybild[height:height+3,width:width+3] = (0, 0, 0)
#
#     color = None
#     if redColor > 250 and greenColor > 250 and blueColor > 250:
#         color = 1 # white
#         print("white")
#
#     elif redColor < 44 and greenColor < 44 and blueColor < 44:
#         color = 2 #black
#         print("black")
#
#     elif redColor > 200 and greenColor > 200 and blueColor < 100:
#         color = 4 #yellow
#         print("yellow")
#
#     elif redColor > 200 and greenColor > 25 and blueColor < 100:
#         color = 3 # orange
#         print("orange")
#
#     # elif redColor > 200 &  greenColor < 100 & blueColor > 200:
#     #     color = 5 #purple
#
#     elif redColor > 250 and greenColor < 200 and blueColor < 200:
#         color = 6 #red
#         print("red")
#
#     elif redColor < 200 and greenColor > 250 and blueColor < 200:
#         color = 7 #green
#         print("green")
#
#     elif redColor < 200 and greenColor < 200 and blueColor >= 230:
#         color = 8 #blue
#         print("blue")
#
#     if color == None:
#         print("Not able to recognize")
#
# cv2.imshow("HSV", hsv)
# cv2.imshow('BGR', mybild)
# cv2.imshow('final', result)
# cv2.imshow("Mask", mask)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#
# import pyautogui, PIL
# import numpy, cv2
#
# mybild = cv2.imread("Assets/Bild_3.png", cv2.IMREAD_COLOR)
# hsv = cv2.cvtColor(mybild, cv2.COLOR_BGR2HSV)
# # um Farbe von HSV von App zu HSV von cv2 muss man H/2 S/255*100 V/255*100
# lower_blue = numpy.array([90, 50, 50]) # in app 180, 20, 20
# upper_blue = numpy.array([130, 255, 255]) # in app 260, 100, 100
#
# lower_red_rechts = numpy.array([160, 50, 50]) # 320, 20, 20
# upper_red_rechts = numpy.array([179, 255, 255]) # 360, 100, 100
#
# lower_red_links = numpy.array([0, 50, 50]) # 0, 20, 20
# upper_red_links = numpy.array([8, 255, 255]) # 16, 100, 10
#
# lower_orange = numpy.array([10, 50, 50]) # 20, 20, 20
# upper_orange = numpy.array([20, 255, 255]) # 40, 100, 100
#
# lower_yellow = numpy.array([25, 50, 50]) # 50, 20, 20
# upper_yellow = numpy.array([32, 255, 255]) # 64, 100, 100
#
# lower_green = numpy.array([40, 50, 50]) # 80, 20, 20
# upper_green = numpy.array([70, 255, 255]) # 140, 100, 100
#
# lower_white = numpy.array([0, 0, 210]) # lo mas blanco 80 * 255
# upper_white = numpy.array([179, 20, 255]) # lo mas negro # 100
#
# mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
# result = cv2.bitwise_and(mybild, mybild, mask=mask)
#
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# result = cv2.bitwise_and(result, result, mask=mask)
#
#
# grayimage = cv2.cvtColor(mybild, cv2.COLOR_BGR2GRAY)
#
# corners = cv2.goodFeaturesToTrack(grayimage, 100, 0.01, 50) # image_to_analyze, number of best corners, confidence of corner, euclidian distance between corners so that points nebenan dont get recognized.
# corners = numpy.int0(corners)
#
# for corner in corners:
#     x, y = corner.ravel() # ravel flattens array, removes all nestings.
#     cv2.circle(mybild, (x, y), 10, (255, 255, 0), -1)
#
#
# # mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
# # mask = cv2.inRange(hsv, lower_green, upper_green)
# # mask = cv2.inRange(hsv, lower_red_links, upper_red_links)
# # mask = cv2.inRange(hsv, lower_orange, upper_orange)
# # mask = cv2.inRange(hsv, lower_white, upper_white)
# print(f"shape is: height, width{mybild.shape}")
#
# HEIGHT = mybild.shape[0]
# WIDTH = mybild.shape[1]
#
#
# mitte_mitte_1_1 = (WIDTH//2, HEIGHT//2)
# mitte_oben_0_1 = (WIDTH //2, HEIGHT * 1//6)
# mitte_unten_2_1 = (WIDTH // 2, HEIGHT * 5//6)
#
# rechts_mitte_1_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT//2)
# rechts_oben_0_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT * 1//6)
# rechts_unten_2_2 = (WIDTH//2 + HEIGHT*1//3, HEIGHT * 5//6)
#
# links_mitte_1_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT//2)
# links_oben_0_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT * 1//6)
# links_unten_2_0 = (WIDTH//2 - HEIGHT * 1//3, HEIGHT * 5//6)
# liste_pixels = (links_oben_0_0, mitte_oben_0_1, rechts_oben_0_2, links_mitte_1_0, mitte_mitte_1_1, rechts_mitte_1_2, links_unten_2_0, mitte_unten_2_1, rechts_unten_2_2)
#
# for width, height in liste_pixels:
#     blueColor, greenColor, redColor = mybild[height][width]
#     h, s, v = hsv[height][width]
#
#     print("Coordinates:", width, height, "RGB", redColor, greenColor, blueColor, "\t\tHSV", h, s, v, end="")
#     mybild[height:height+3,width:width+3] = (0, 0, 0)
#
#
#
# cv2.imshow("HSV", hsv)
# cv2.imshow('BGR', mybild)
# cv2.imshow('final', result)
# cv2.imshow("Mask", mask)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
