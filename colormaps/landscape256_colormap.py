from numpy import array

'''
256-level colormap created by make_colormap utility from file landscape256.png
Actually taken from a slice of a photograph of the Pyrenees
'''
landscape256 = array([ \
[62, 90, 44], [65, 91, 57], [29, 53, 27], [59, 78, 52],
[69, 92, 52], [66, 87, 56], [18, 31, 16], [3, 2, 8],
[3, 1, 6], [3, 4, 8], [4, 6, 10], [32, 46, 34],
[34, 55, 38], [11, 23, 19], [4, 4, 6], [5, 16, 16],
[27, 42, 43], [8, 26, 27], [16, 37, 22], [71, 100, 61],
[72, 100, 53], [66, 90, 47], [54, 77, 44], [66, 94, 53],
[66, 98, 52], [69, 94, 63], [36, 54, 33], [26, 44, 26],
[62, 80, 60], [44, 60, 37], [67, 77, 49], [70, 82, 55],
[35, 53, 25], [29, 55, 32], [62, 97, 55], [70, 102, 58],
[64, 90, 59], [24, 45, 29], [45, 63, 50], [20, 35, 38],
[12, 26, 40], [25, 37, 50], [4, 17, 27], [36, 51, 44],
[65, 88, 60], [52, 69, 50], [40, 49, 33], [79, 89, 54],
[62, 79, 46], [62, 88, 50], [68, 95, 53], [61, 83, 57],
[54, 73, 49], [68, 84, 57], [74, 96, 58], [84, 110, 66],
[85, 109, 66], [93, 115, 74], [91, 112, 69], [97, 117, 74],
[88, 114, 66], [87, 114, 71], [59, 80, 53], [68, 84, 58],
[74, 94, 63], [56, 79, 48], [66, 88, 59], [69, 92, 59],
[83, 106, 78], [76, 96, 80], [103, 125, 124], [102, 127, 128],
[100, 125, 131], [92, 113, 138], [93, 116, 135], [100, 123, 142],
[102, 124, 146], [104, 126, 149], [105, 125, 147], [105, 126, 148],
[111, 132, 155], [124, 143, 167], [133, 150, 174], [131, 148, 173],
[128, 145, 170], [122, 142, 164], [114, 135, 156], [112, 133, 154],
[106, 127, 148], [111, 129, 146], [129, 146, 162], [141, 155, 170],
[152, 165, 179], [150, 163, 177], [149, 163, 176], [153, 169, 181],
[152, 169, 181], [157, 170, 183], [167, 176, 190], [174, 180, 196],
[171, 179, 196], [159, 171, 190], [152, 169, 189], [142, 163, 184],
[132, 149, 175], [102, 126, 147], [94, 120, 142], [100, 122, 151],
[101, 126, 150], [98, 123, 148], [93, 118, 146], [94, 119, 148],
[96, 122, 149], [77, 103, 130], [73, 99, 126], [75, 98, 126],
[79, 100, 128], [86, 108, 133], [91, 113, 136], [104, 122, 141],
[96, 109, 123], [103, 118, 129], [104, 124, 138], [146, 153, 166],
[198, 182, 172], [240, 218, 204], [210, 197, 189], [217, 206, 186],
[215, 199, 177], [226, 206, 190], [212, 189, 168], [190, 172, 157],
[189, 175, 159], [227, 205, 180], [235, 209, 188], [235, 210, 186],
[220, 203, 180], [231, 224, 206], [249, 249, 223], [241, 229, 206],
[220, 196, 169], [248, 238, 199], [251, 242, 208], [248, 244, 217],
[219, 218, 210], [123, 130, 134], [117, 130, 149], [115, 133, 150],
[113, 139, 161], [110, 142, 174], [124, 161, 200], [124, 172, 224],
[113, 173, 237], [114, 173, 237], [118, 170, 239], [116, 171, 238],
[112, 173, 239], [117, 173, 237], [121, 166, 222], [101, 126, 169],
[158, 164, 164], [234, 217, 207], [241, 238, 210], [240, 214, 198],
[216, 197, 174], [227, 209, 191], [212, 183, 158], [218, 196, 175],
[197, 188, 176], [213, 202, 188], [225, 204, 181], [166, 164, 159],
[94, 109, 131], [89, 113, 135], [90, 108, 127], [98, 108, 118],
[158, 145, 134], [231, 194, 166], [232, 196, 165], [245, 211, 176],
[231, 199, 171], [218, 190, 171], [220, 197, 179], [149, 141, 131],
[131, 127, 133], [181, 164, 154], [192, 173, 157], [231, 212, 198],
[227, 205, 184], [231, 214, 194], [115, 121, 123], [59, 81, 106],
[89, 104, 124], [96, 111, 124], [79, 96, 117], [84, 102, 116],
[92, 110, 124], [86, 102, 125], [130, 135, 137], [191, 190, 181],
[185, 178, 176], [165, 154, 145], [201, 186, 164], [107, 108, 120],
[82, 107, 132], [88, 103, 115], [79, 101, 122], [111, 151, 196],
[110, 152, 216], [108, 150, 219], [89, 131, 193], [97, 133, 187],
[78, 111, 163], [81, 99, 126], [77, 94, 124], [75, 99, 126],
[83, 96, 116], [190, 179, 163], [217, 203, 182], [113, 117, 117],
[129, 134, 125], [215, 199, 186], [154, 161, 191], [104, 150, 220],
[100, 152, 227], [105, 143, 204], [92, 114, 136], [98, 108, 113],
[194, 186, 174], [204, 177, 163], [204, 186, 168], [154, 164, 200],
[103, 147, 222], [96, 147, 224], [98, 146, 225], [97, 145, 224],
[96, 145, 224], [96, 145, 224], [96, 145, 224], [93, 144, 223],
[92, 143, 222], [91, 143, 222], [90, 142, 220], [89, 140, 219],
[89, 141, 220], [87, 142, 220], [88, 143, 221], [88, 140, 222],
[88, 139, 223], [88, 138, 224], [87, 139, 226], [85, 139, 227],
[83, 139, 226], [83, 140, 226], [82, 138, 224], [82, 138, 223]])
'''
End of colormap from file landscape256.png
'''
