# extendedAlphabet = "".join([chr(i) for i in range(ord(" "), ord("~") + 1)])
# otherChars = " 0123456789,.?-()!-\"\'"
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() + otherChars
alphabet = "abcdefghijklmnopqrstuvwxyz"

def xor(encodedChars, password):
    decodedChars = []
    for charIndex in range(len(encodedChars)):
        decodedChars.append(encodedChars[charIndex] ^ password[charIndex % len(password)])
    return decodedChars


# def findEnglish(string, encodingLength, words):
#     counter = 0
#     # for word in words:
#     #     if len(word) > 3 and word in string:
#     #         print(word)
#     #         counter += 1
#     for encodingLength in
#     return counter


if __name__ == '__main__':
    # print(alphabet)
    # load the two files
    with open("20k.txt", "r") as f:
        words = f.readlines()
    words = [word[:-1] for word in words]  # remove the trailing \n

    # probably the less frequent words will not prove useful
    words = words[:5000]
    # print(words)

    with open("p059_cipher.txt", "r") as f:
        encodedChars = list(map(lambda x: int(x), f.readline().split(",")))
    print(len(encodedChars))

    # key
    # "exp"

    decoded = xor(encodedChars, [ord('e'), ord('x'), ord('p')])
    sum = 0
    for char in decoded:
        sum += char
    print(sum, decoded)

    # for ch1 in alphabet:
    #     for ch2 in alphabet:
    #         for ch3 in alphabet:
    #             decoded = xor(encodedChars, [ord(ch1), ord(ch2), ord(ch3)])
    #             string = "".join(([chr(ch) for ch in decoded]))
    #
    #             for word in words:
    #                 if len(word) > 4 and word in string.lower():
    #                     print(string, [ch1, ch2, ch3])


    # READING THE TASK PROPERLY IS FOR THE WEAK

    # minLength = 3
    # wordBitsStart = []
    # wordBitsEnd = []
    # for word in words:
    #     if len(word) < minLength:
    #         continue
    #     if word[-minLength:] not in wordBitsStart:
    #         wordBitsStart.append(word[-minLength:])
    #     if word[:minLength] not in wordBitsStart and word[:minLength] not in words:
    #         wordBitsEnd.append(word[:minLength])
    # print(wordBitsStart)
    # print(wordBitsEnd)

    # guess the first words and "move" it along, searching for other words
    # for word in words:
    #     word = word.capitalize()
    #     print(word)
    #     decoded = [ord(char) for char in word]
    #     passwordToTry = xor(encodedChars[:len(word)], decoded)
    #     # print(word)
    #
    #     # try different offsets
    #     for offset in range(len(word), len(encodedChars) // 2):
    #         portionToXor = encodedChars[offset: len(word) + offset]
    #         result = xor(portionToXor, passwordToTry)
    #         # print(result)
    #
    #         # is it english?
    #         passes = True
    #         for char in result:
    #             if chr(char) not in alphabet:
    #                 passes = False
    #                 break
    #         if passes:
    #             string = "".join([chr(index) for index in result])
    #             for wordBit in wordBitsStart:
    #                 if wordBit in string:
    #                     print(word, wordBit, string)
    #             for wordBit in wordBitsEnd:
    #                 firstIndex = string.find(wordBit)
    #                 if firstIndex == -1:
    #                     continue
    #
    #                 if len(string) == firstIndex + len(wordBit) or string[firstIndex + len(wordBit)] in otherChars:
    #                     print(word, wordBit, string)
                # hope we get lucky
                # for word in words:
                #     if len(word) > 3 and word in "".join([chr(index) for index in result]):
                #         print(word, [chr(index) for index in result])


    # try getting sensible values
    # let's say that the passcode can't be longer than 100
    # paddingsLeft = [i for i in range(len(encodedChars) // 2)]
    # paddingsLeft = [150, 156, 170, 172, 174, 175, 179, 183, 185, 186, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753]
    #
    #
    # lastCheckedShifts = 0
    # minWordLength = 27
    #
    # for shiftIndex in range(lastCheckedShifts, minWordLength):
    #
    #     paddings = []
    #     for padding in paddingsLeft:
    #         if len(paddingsLeft) != 0 and padding > paddingsLeft[-1]:
    #             continue
    #         paddingCh = [0] * padding
    #         # try every char code
    #         for initChCode in range(0, 256):
    #             toTest = [0] * shiftIndex + [initChCode] + [0] * (padding - shiftIndex)
    #
    #             if len(toTest) != padding + 1:
    #                 print("HEELPP, it's doing something wrong")
    #
    #             decoded = xor(encodedChars, toTest)
    #
    #             # check if all are alphanumeric
    #             checkChars = [chr(decoded[char]) for char in range(shiftIndex, len(decoded), padding + 1)]
    #             # print("checkchars: ", checkChars)
    #
    #             passes = True
    #             for char in checkChars:
    #                 if char not in alphabet:
    #                     # print(char)
    #                     passes = False
    #                     break
    #             if passes:
    #                 # print(decoded, "'" + checkChars + "'")
    #                 paddings.append(padding + 1)
    #                 break
    #     print(paddings)
    #     paddingsLeft = paddings
    #     print(paddingsLeft)
