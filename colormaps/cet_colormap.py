'''
Some of these RGB colormaps are derived from HoloViz Colorcet color maps, 
available under Creative Commons Attribution (CC_BY) license.
https://github.com/holoviz/colorcet

For full license terms see https://github.com/holoviz/colorcet/blob/master/LICENSE.txt
'''

from numpy import array
    
BlueBrown16 = array([ \
[66, 30, 15], [25, 7, 26], [9, 1, 47], [4, 4, 73],
[0, 7, 100], [12, 44, 138], [24, 82, 177], [57, 125, 209],
[134, 181, 229], [211, 236, 248], [241, 233, 191], [248, 201, 95],
[255, 170, 0], [204, 128, 0], [153, 87, 0], [106, 52, 3]]) 

cet_CBC1 = array([[62, 135, 234],
[65, 136, 236],
[68, 138, 237],
[71, 139, 238],
[75, 141, 239],
[79, 142, 239],
[83, 144, 240],
[86, 145, 240],
[90, 147, 240],
[94, 148, 240],
[98, 150, 241],
[102, 151, 241],
[105, 153, 241],
[109, 155, 241],
[112, 156, 241],
[115, 158, 241],
[119, 159, 241],
[122, 161, 241],
[125, 163, 242],
[128, 164, 242],
[131, 166, 242],
[134, 168, 242],
[137, 169, 242],
[140, 171, 242],
[143, 173, 242],
[146, 174, 242],
[149, 176, 242],
[151, 178, 242],
[154, 179, 242],
[157, 181, 243],
[160, 183, 243],
[162, 184, 243],
[165, 186, 243],
[167, 188, 243],
[170, 189, 243],
[173, 191, 243],
[175, 193, 243],
[178, 194, 243],
[180, 196, 243],
[183, 198, 243],
[185, 200, 243],
[188, 201, 243],
[190, 203, 243],
[193, 205, 243],
[195, 207, 243],
[197, 208, 244],
[200, 210, 244],
[202, 212, 244],
[205, 214, 244],
[207, 215, 244],
[209, 217, 244],
[212, 219, 244],
[214, 221, 244],
[216, 222, 244],
[219, 224, 244],
[221, 226, 243],
[223, 227, 243],
[225, 229, 243],
[227, 230, 242],
[229, 231, 241],
[231, 233, 240],
[232, 233, 239],
[234, 234, 238],
[235, 234, 236],
[236, 234, 234],
[236, 234, 231],
[236, 234, 229],
[236, 233, 226],
[236, 232, 223],
[236, 231, 220],
[235, 229, 216],
[234, 228, 213],
[233, 226, 210],
[232, 225, 206],
[231, 223, 203],
[230, 221, 199],
[229, 219, 196],
[228, 218, 192],
[227, 216, 189],
[226, 214, 185],
[224, 212, 182],
[223, 211, 178],
[222, 209, 175],
[221, 207, 171],
[219, 205, 168],
[218, 204, 165],
[217, 202, 161],
[216, 200, 158],
[214, 198, 154],
[213, 197, 151],
[212, 195, 148],
[210, 193, 144],
[209, 191, 141],
[208, 190, 137],
[206, 188, 134],
[205, 186, 131],
[204, 185, 127],
[202, 183, 124],
[201, 181, 120],
[200, 180, 117],
[198, 178, 114],
[197, 176, 110],
[195, 174, 107],
[194, 173, 104],
[192, 171, 100],
[191, 169, 97],
[190, 168, 93],
[188, 166, 90],
[187, 164, 87],
[185, 163, 83],
[184, 161, 80],
[182, 160, 76],
[181, 158, 73],
[179, 156, 69],
[177, 155, 66],
[176, 153, 62],
[174, 151, 58],
[173, 150, 55],
[171, 148, 51],
[170, 147, 47],
[168, 145, 44],
[166, 143, 40],
[165, 142, 36],
[163, 140, 32],
[161, 139, 29],
[160, 137, 26],
[158, 135, 23],
[156, 134, 20],
[154, 132, 18],
[153, 131, 16],
[151, 129, 15],
[149, 128, 14],
[147, 126, 14],
[145, 124, 14],
[144, 123, 15],
[142, 121, 16],
[140, 120, 17],
[138, 118, 18],
[136, 117, 19],
[134, 115, 20],
[133, 114, 21],
[131, 112, 22],
[129, 110, 23],
[127, 109, 24],
[125, 107, 25],
[124, 106, 26],
[122, 104, 26],
[120, 103, 27],
[118, 101, 28],
[116, 100, 28],
[115, 98, 29],
[113, 97, 30],
[111, 95, 30],
[109, 94, 31],
[107, 92, 31],
[106, 91, 32],
[104, 89, 32],
[102, 88, 33],
[100, 87, 33],
[98, 85, 33],
[97, 84, 34],
[95, 82, 34],
[93, 81, 35],
[91, 79, 35],
[90, 78, 35],
[88, 76, 36],
[86, 75, 36],
[84, 74, 36],
[83, 72, 36],
[81, 71, 37],
[79, 69, 37],
[77, 68, 37],
[76, 67, 37],
[74, 65, 37],
[72, 64, 38],
[70, 62, 38],
[69, 61, 38],
[67, 60, 38],
[65, 58, 38],
[63, 57, 38],
[62, 56, 39],
[60, 54, 39],
[58, 53, 39],
[56, 52, 39],
[55, 51, 40],
[53, 50, 40],
[52, 49, 41],
[51, 48, 41],
[49, 47, 42],
[48, 46, 43],
[47, 46, 44],
[47, 46, 46],
[46, 46, 48],
[46, 46, 49],
[46, 47, 52],
[46, 47, 54],
[46, 48, 56],
[47, 49, 59],
[47, 50, 61],
[48, 51, 64],
[48, 53, 66],
[49, 54, 69],
[49, 55, 72],
[50, 57, 75],
[51, 58, 78],
[51, 59, 80],
[52, 61, 83],
[53, 62, 86],
[53, 63, 89],
[54, 65, 92],
[54, 66, 95],
[55, 68, 98],
[55, 69, 101],
[56, 70, 104],
[56, 72, 107],
[57, 73, 110],
[57, 75, 113],
[58, 76, 116],
[58, 78, 119],
[58, 79, 122],
[59, 80, 125],
[59, 82, 128],
[59, 83, 131],
[59, 85, 134],
[60, 86, 137],
[60, 88, 140],
[60, 89, 144],
[60, 91, 147],
[60, 92, 150],
[60, 94, 153],
[60, 95, 156],
[60, 97, 159],
[60, 98, 163],
[60, 100, 166],
[60, 101, 169],
[60, 103, 172],
[60, 104, 176],
[60, 106, 179],
[59, 107, 182],
[59, 109, 185],
[59, 110, 189],
[58, 112, 192],
[58, 114, 195],
[58, 115, 199],
[57, 117, 202],
[57, 118, 205],
[56, 120, 209],
[56, 121, 212],
[55, 123, 215],
[55, 124, 218],
[55, 126, 221],
[55, 127, 224],
[56, 129, 226],
[56, 130, 229],
[58, 132, 231],
[60, 133, 233]])

cet_CBTC1 = array([[41, 188, 215],
[45, 189, 216],
[50, 190, 217],
[55, 191, 218],
[60, 192, 219],
[65, 193, 220],
[70, 195, 220],
[75, 196, 221],
[80, 197, 221],
[84, 198, 222],
[89, 199, 223],
[93, 200, 223],
[98, 201, 224],
[102, 202, 224],
[106, 203, 225],
[110, 204, 226],
[113, 205, 226],
[117, 206, 227],
[121, 207, 227],
[124, 208, 228],
[128, 209, 229],
[131, 210, 229],
[134, 211, 230],
[138, 212, 230],
[141, 213, 231],
[144, 214, 232],
[147, 215, 232],
[151, 216, 233],
[154, 217, 233],
[157, 218, 234],
[160, 219, 234],
[163, 220, 235],
[166, 222, 236],
[169, 223, 236],
[172, 224, 237],
[175, 225, 237],
[178, 226, 238],
[181, 227, 239],
[184, 228, 239],
[186, 229, 240],
[189, 230, 240],
[192, 231, 241],
[195, 232, 242],
[198, 233, 242],
[201, 234, 243],
[203, 235, 243],
[206, 236, 244],
[209, 237, 245],
[212, 238, 245],
[214, 239, 246],
[217, 240, 246],
[220, 241, 247],
[222, 242, 247],
[225, 243, 248],
[228, 244, 248],
[230, 245, 249],
[233, 246, 249],
[236, 246, 249],
[238, 247, 249],
[240, 247, 249],
[243, 248, 249],
[245, 248, 249],
[247, 248, 248],
[248, 247, 248],
[250, 247, 247],
[251, 246, 245],
[252, 245, 244],
[252, 244, 243],
[253, 243, 241],
[253, 241, 239],
[254, 240, 238],
[254, 238, 236],
[254, 237, 234],
[254, 235, 232],
[254, 233, 230],
[254, 232, 228],
[254, 230, 226],
[253, 228, 224],
[253, 227, 223],
[253, 225, 221],
[253, 223, 219],
[253, 222, 217],
[253, 220, 215],
[252, 218, 213],
[252, 217, 211],
[252, 215, 209],
[252, 213, 207],
[252, 212, 206],
[251, 210, 204],
[251, 208, 202],
[251, 207, 200],
[251, 205, 198],
[250, 203, 196],
[250, 202, 194],
[250, 200, 193],
[250, 198, 191],
[249, 197, 189],
[249, 195, 187],
[249, 194, 185],
[248, 192, 183],
[248, 190, 182],
[248, 189, 180],
[248, 187, 178],
[247, 185, 176],
[247, 184, 174],
[246, 182, 172],
[246, 180, 171],
[246, 179, 169],
[245, 177, 167],
[245, 175, 165],
[245, 174, 163],
[244, 172, 162],
[244, 170, 160],
[243, 169, 158],
[243, 167, 156],
[243, 165, 154],
[242, 164, 153],
[242, 162, 151],
[241, 160, 149],
[241, 159, 148],
[240, 157, 146],
[239, 156, 144],
[238, 154, 143],
[238, 153, 141],
[237, 151, 140],
[236, 150, 138],
[234, 149, 137],
[233, 147, 136],
[231, 146, 135],
[230, 145, 134],
[228, 144, 133],
[226, 143, 132],
[224, 142, 131],
[222, 141, 130],
[220, 140, 130],
[218, 140, 129],
[216, 139, 128],
[213, 138, 128],
[211, 137, 127],
[209, 136, 126],
[207, 136, 126],
[204, 135, 125],
[202, 134, 125],
[200, 133, 124],
[198, 132, 123],
[196, 132, 123],
[193, 131, 122],
[191, 130, 121],
[189, 129, 121],
[187, 128, 120],
[184, 128, 119],
[182, 127, 119],
[180, 126, 118],
[178, 125, 118],
[176, 124, 117],
[173, 124, 116],
[171, 123, 116],
[169, 122, 115],
[167, 121, 114],
[165, 120, 114],
[162, 119, 113],
[160, 119, 113],
[158, 118, 112],
[156, 117, 111],
[154, 116, 111],
[152, 115, 110],
[149, 115, 109],
[147, 114, 109],
[145, 113, 108],
[143, 112, 108],
[141, 111, 107],
[138, 111, 106],
[136, 110, 106],
[134, 109, 105],
[132, 108, 104],
[130, 107, 104],
[127, 106, 103],
[125, 106, 103],
[123, 105, 102],
[121, 104, 101],
[119, 103, 101],
[117, 102, 100],
[114, 102, 100],
[112, 101, 99],
[110, 100, 99],
[108, 100, 99],
[106, 100, 99],
[104, 99, 99],
[103, 99, 99],
[101, 99, 99],
[100, 99, 100],
[98, 100, 100],
[97, 100, 101],
[96, 101, 102],
[96, 102, 104],
[95, 103, 105],
[94, 104, 107],
[94, 105, 108],
[94, 106, 110],
[93, 108, 112],
[93, 109, 113],
[93, 110, 115],
[93, 112, 117],
[92, 113, 119],
[92, 115, 120],
[92, 116, 122],
[92, 117, 124],
[91, 119, 126],
[91, 120, 128],
[91, 122, 130],
[90, 123, 131],
[90, 124, 133],
[89, 126, 135],
[89, 127, 137],
[88, 129, 139],
[88, 130, 141],
[87, 132, 142],
[87, 133, 144],
[86, 134, 146],
[85, 136, 148],
[85, 137, 150],
[84, 139, 152],
[83, 140, 154],
[82, 142, 156],
[82, 143, 158],
[81, 144, 159],
[80, 146, 161],
[79, 147, 163],
[78, 149, 165],
[77, 150, 167],
[76, 152, 169],
[74, 153, 171],
[73, 155, 173],
[72, 156, 175],
[70, 158, 177],
[69, 159, 179],
[67, 160, 181],
[66, 162, 183],
[64, 163, 184],
[62, 165, 186],
[60, 166, 188],
[58, 168, 190],
[56, 169, 192],
[54, 171, 194],
[51, 172, 196],
[49, 174, 198],
[46, 175, 200],
[43, 177, 202],
[40, 178, 204],
[38, 179, 206],
[36, 181, 207],
[34, 182, 209],
[33, 183, 210],
[34, 185, 212],
[35, 186, 213],
[35, 186, 213]])

cet_C1 = array([[248, 132, 247],
[249, 131, 245],
[250, 130, 243],
[251, 129, 240],
[252, 128, 238],
[252, 127, 235],
[252, 125, 232],
[253, 123, 229],
[253, 122, 225],
[252, 120, 222],
[252, 118, 218],
[252, 115, 215],
[251, 113, 211],
[251, 111, 207],
[250, 109, 204],
[250, 107, 200],
[249, 104, 196],
[248, 102, 192],
[248, 100, 188],
[247, 97, 185],
[246, 95, 181],
[245, 93, 177],
[245, 90, 173],
[244, 88, 170],
[243, 85, 166],
[242, 83, 162],
[241, 81, 158],
[240, 78, 155],
[239, 76, 151],
[238, 74, 147],
[236, 71, 143],
[235, 69, 139],
[234, 67, 136],
[233, 65, 132],
[231, 63, 128],
[230, 60, 124],
[228, 58, 120],
[227, 56, 117],
[225, 54, 113],
[223, 52, 109],
[222, 50, 105],
[220, 49, 101],
[218, 47, 97],
[216, 45, 94],
[214, 43, 90],
[212, 41, 86],
[211, 39, 82],
[209, 38, 78],
[207, 36, 75],
[205, 34, 71],
[203, 32, 67],
[201, 31, 63],
[199, 29, 60],
[197, 27, 56],
[195, 26, 53],
[193, 25, 49],
[192, 24, 46],
[190, 23, 42],
[188, 22, 39],
[187, 22, 36],
[185, 22, 33],
[184, 23, 30],
[183, 24, 27],
[182, 25, 24],
[181, 26, 21],
[181, 28, 19],
[181, 30, 17],
[180, 33, 15],
[180, 35, 13],
[180, 38, 11],
[181, 40, 9],
[181, 43, 8],
[182, 45, 7],
[182, 48, 6],
[183, 51, 5],
[184, 53, 5],
[185, 56, 4],
[186, 59, 4],
[187, 61, 4],
[188, 64, 4],
[189, 67, 4],
[190, 69, 4],
[191, 72, 4],
[192, 74, 4],
[193, 77, 4],
[194, 79, 4],
[195, 82, 4],
[196, 84, 4],
[197, 86, 4],
[198, 89, 4],
[199, 91, 4],
[199, 93, 4],
[200, 96, 4],
[201, 98, 4],
[202, 101, 4],
[203, 103, 4],
[204, 105, 4],
[204, 108, 4],
[205, 110, 4],
[206, 112, 4],
[206, 115, 4],
[207, 117, 4],
[208, 120, 4],
[208, 122, 4],
[209, 124, 4],
[209, 127, 4],
[210, 129, 4],
[210, 131, 4],
[211, 134, 4],
[211, 136, 4],
[212, 138, 4],
[212, 141, 4],
[213, 143, 4],
[213, 145, 4],
[213, 147, 4],
[214, 150, 5],
[214, 152, 5],
[214, 154, 6],
[214, 156, 8],
[214, 158, 10],
[214, 160, 12],
[214, 162, 15],
[213, 163, 17],
[213, 165, 21],
[212, 166, 24],
[211, 167, 27],
[210, 168, 31],
[209, 169, 35],
[207, 170, 39],
[205, 170, 42],
[203, 170, 46],
[201, 170, 50],
[199, 170, 54],
[196, 169, 58],
[194, 169, 62],
[191, 168, 66],
[188, 167, 70],
[185, 166, 74],
[182, 165, 77],
[178, 164, 81],
[175, 163, 85],
[172, 162, 88],
[168, 161, 92],
[164, 160, 95],
[161, 159, 98],
[157, 157, 102],
[153, 156, 105],
[149, 155, 108],
[145, 154, 111],
[141, 152, 114],
[137, 151, 117],
[133, 150, 121],
[128, 149, 124],
[124, 147, 127],
[119, 146, 130],
[114, 145, 133],
[109, 144, 135],
[104, 142, 138],
[99, 141, 141],
[94, 140, 144],
[88, 138, 147],
[83, 137, 150],
[77, 135, 153],
[72, 134, 156],
[67, 132, 159],
[61, 130, 162],
[56, 128, 165],
[51, 126, 168],
[47, 124, 171],
[43, 122, 174],
[40, 120, 177],
[37, 118, 180],
[35, 115, 184],
[34, 113, 187],
[33, 110, 190],
[33, 108, 193],
[34, 105, 196],
[35, 102, 199],
[36, 99, 202],
[38, 96, 206],
[39, 93, 209],
[41, 90, 212],
[43, 87, 215],
[44, 84, 218],
[46, 81, 221],
[47, 78, 224],
[49, 75, 226],
[51, 72, 229],
[53, 70, 231],
[55, 67, 234],
[57, 65, 236],
[59, 63, 238],
[62, 62, 240],
[64, 61, 241],
[67, 60, 243],
[70, 60, 244],
[73, 60, 245],
[76, 61, 246],
[79, 61, 246],
[82, 62, 247],
[85, 64, 247],
[88, 65, 248],
[91, 67, 248],
[93, 68, 248],
[96, 70, 249],
[99, 72, 249],
[102, 74, 249],
[104, 76, 249],
[107, 78, 249],
[109, 80, 249],
[112, 82, 249],
[114, 84, 249],
[117, 86, 249],
[119, 88, 249],
[121, 90, 249],
[124, 92, 249],
[126, 94, 249],
[129, 96, 249],
[132, 97, 249],
[134, 99, 249],
[137, 101, 249],
[140, 102, 250],
[143, 104, 250],
[146, 106, 250],
[149, 107, 250],
[153, 108, 250],
[156, 110, 250],
[159, 111, 251],
[163, 112, 251],
[166, 113, 251],
[170, 115, 251],
[173, 116, 252],
[177, 117, 252],
[180, 118, 252],
[184, 119, 253],
[188, 120, 253],
[191, 121, 253],
[195, 122, 253],
[198, 123, 254],
[202, 124, 254],
[205, 125, 254],
[209, 126, 255],
[212, 127, 255],
[216, 128, 255],
[219, 129, 255],
[222, 130, 255],
[225, 130, 255],
[228, 131, 255],
[231, 132, 255],
[234, 132, 255],
[237, 133, 254],
[239, 133, 253],
[241, 133, 253],
[243, 133, 252],
[245, 133, 250],
[247, 133, 249]])

cet_C4s = array([[26, 99, 229],
[28, 100, 229],
[32, 100, 229],
[36, 101, 229],
[41, 102, 229],
[46, 103, 229],
[51, 104, 229],
[56, 106, 229],
[61, 107, 229],
[66, 109, 229],
[71, 111, 229],
[75, 113, 229],
[80, 114, 229],
[84, 116, 230],
[89, 118, 230],
[93, 120, 230],
[97, 122, 230],
[101, 124, 230],
[104, 126, 230],
[108, 128, 230],
[112, 131, 230],
[115, 133, 230],
[118, 135, 230],
[122, 137, 230],
[125, 139, 230],
[128, 141, 230],
[131, 143, 230],
[134, 145, 230],
[137, 147, 230],
[140, 150, 230],
[143, 152, 230],
[146, 154, 230],
[149, 156, 230],
[152, 158, 230],
[155, 161, 230],
[157, 163, 229],
[160, 165, 229],
[163, 167, 229],
[166, 169, 229],
[168, 172, 229],
[171, 174, 229],
[173, 176, 229],
[176, 178, 229],
[179, 181, 229],
[181, 183, 229],
[184, 185, 229],
[186, 187, 229],
[189, 190, 229],
[191, 192, 229],
[193, 194, 228],
[196, 196, 228],
[198, 198, 228],
[201, 200, 228],
[203, 202, 228],
[205, 204, 227],
[207, 206, 227],
[209, 208, 226],
[211, 209, 226],
[213, 211, 225],
[215, 212, 224],
[217, 213, 223],
[219, 213, 222],
[220, 214, 220],
[222, 214, 219],
[223, 213, 217],
[224, 213, 215],
[225, 212, 212],
[226, 211, 210],
[227, 210, 207],
[228, 208, 205],
[228, 206, 202],
[229, 204, 199],
[230, 202, 196],
[230, 200, 192],
[230, 197, 189],
[230, 195, 186],
[231, 192, 182],
[231, 190, 179],
[231, 187, 175],
[231, 184, 172],
[231, 181, 168],
[231, 179, 164],
[231, 176, 161],
[230, 173, 157],
[230, 170, 154],
[230, 167, 150],
[230, 165, 147],
[230, 162, 143],
[229, 159, 140],
[229, 156, 136],
[229, 153, 133],
[228, 150, 129],
[228, 148, 126],
[227, 145, 122],
[227, 142, 119],
[226, 139, 116],
[226, 136, 112],
[225, 133, 109],
[225, 130, 105],
[224, 127, 102],
[223, 124, 99],
[223, 122, 95],
[222, 119, 92],
[221, 116, 89],
[220, 113, 85],
[220, 110, 82],
[219, 107, 79],
[218, 104, 76],
[217, 101, 72],
[216, 97, 69],
[215, 94, 66],
[214, 91, 62],
[213, 88, 59],
[212, 85, 56],
[211, 82, 53],
[210, 79, 50],
[209, 75, 47],
[208, 72, 44],
[208, 69, 41],
[207, 66, 38],
[206, 63, 35],
[205, 60, 33],
[204, 57, 30],
[203, 55, 28],
[203, 53, 26],
[202, 51, 25],
[202, 50, 24],
[202, 49, 23],
[202, 48, 23],
[202, 48, 23],
[202, 49, 23],
[202, 50, 24],
[202, 52, 25],
[203, 53, 27],
[204, 56, 29],
[204, 58, 31],
[205, 61, 33],
[206, 64, 36],
[207, 67, 39],
[208, 70, 41],
[209, 73, 44],
[210, 76, 47],
[211, 79, 51],
[212, 83, 54],
[213, 86, 57],
[214, 89, 60],
[215, 92, 63],
[215, 95, 67],
[216, 98, 70],
[217, 101, 73],
[218, 104, 76],
[219, 107, 80],
[220, 110, 83],
[221, 113, 86],
[221, 116, 90],
[222, 119, 93],
[223, 122, 96],
[223, 125, 100],
[224, 128, 103],
[225, 131, 106],
[225, 134, 110],
[226, 137, 113],
[226, 140, 117],
[227, 143, 120],
[227, 145, 123],
[228, 148, 127],
[228, 151, 130],
[229, 154, 134],
[229, 157, 137],
[229, 160, 141],
[230, 163, 144],
[230, 165, 148],
[230, 168, 151],
[230, 171, 155],
[231, 174, 158],
[231, 177, 162],
[231, 179, 165],
[231, 182, 169],
[231, 185, 173],
[231, 188, 176],
[230, 190, 180],
[230, 193, 183],
[230, 195, 187],
[230, 198, 190],
[229, 200, 193],
[228, 202, 197],
[228, 204, 200],
[227, 205, 203],
[226, 207, 206],
[225, 208, 208],
[224, 209, 211],
[222, 210, 213],
[221, 210, 216],
[219, 210, 218],
[217, 210, 219],
[215, 209, 221],
[213, 208, 222],
[211, 207, 224],
[209, 206, 225],
[207, 205, 225],
[205, 203, 226],
[203, 201, 227],
[200, 199, 227],
[198, 197, 228],
[195, 195, 228],
[193, 193, 228],
[191, 191, 228],
[188, 189, 229],
[186, 187, 229],
[183, 185, 229],
[181, 182, 229],
[178, 180, 229],
[175, 178, 229],
[173, 176, 229],
[170, 173, 229],
[168, 171, 229],
[165, 169, 229],
[162, 167, 229],
[160, 164, 229],
[157, 162, 230],
[154, 160, 230],
[151, 158, 230],
[148, 156, 230],
[146, 154, 230],
[143, 151, 230],
[140, 149, 230],
[137, 147, 230],
[134, 145, 230],
[131, 143, 230],
[127, 141, 230],
[124, 138, 230],
[121, 136, 230],
[118, 134, 230],
[114, 132, 230],
[111, 130, 230],
[107, 128, 230],
[104, 126, 230],
[100, 124, 230],
[96, 122, 230],
[92, 120, 230],
[88, 118, 230],
[83, 116, 230],
[79, 114, 229],
[74, 112, 229],
[70, 110, 229],
[65, 109, 229],
[60, 107, 229],
[55, 106, 229],
[50, 104, 229],
[45, 103, 229],
[40, 102, 229],
[35, 101, 229],
[31, 100, 229],
[28, 100, 229],
[25, 99, 229],
[25, 99, 229]])
