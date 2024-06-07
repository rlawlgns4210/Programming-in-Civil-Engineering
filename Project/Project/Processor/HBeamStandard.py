class HBeamStandard:
    def __init__(self, loader):
        self.loader = loader

    def load_h_beam_spec(self):
        last_row = self.loader.load_data()
        if last_row is not None:
            _, _, _, h_beam_spec, _ = self.loader.process_data(last_row)
            return h_beam_spec
        else:
            return None

    def calculate_specs(self, h_beam_spec):
        cross_section_area = 0
        linear_density = 0
        if h_beam_spec == "['100×50', '5', '7', '8']":
            cross_section_area = 11.85
            linear_density = 9.3
            section_modulus = 37.5
        elif h_beam_spec == "['100×100', '6', '8', '10']":
            cross_section_area = 21.9
            linear_density = 17.2
            section_modulus = 76.5
        elif h_beam_spec == "['125×60', '6', '8', '9']":
            cross_section_area = 16.84
            linear_density = 13.2
            section_modulus = 66.1
        elif h_beam_spec == "['125×125', '6.5', '9', '10']":
            cross_section_area = 30.31
            linear_density = 23.8
            section_modulus = 136
        elif h_beam_spec == "['150×75', '5', '7', '8']":
            cross_section_area = 17.85
            linear_density = 14
            section_modulus = 88.8
        elif h_beam_spec == "['148×100', '6', '9', '11']":
            cross_section_area = 26.84
            linear_density = 21.1
            section_modulus = 138
        elif h_beam_spec == "['150×150', '7', '10', '11']":
            cross_section_area = 40.14
            linear_density = 31.5
            section_modulus = 219
        elif h_beam_spec == "['175×90', '5', '8', '9']":
            cross_section_area = 23.04
            linear_density = 18.1
            section_modulus = 139
        elif h_beam_spec == "['175×175', '7.5', '11', '12']":
            cross_section_area = 51.21
            linear_density = 40.2
            section_modulus = 330
        elif h_beam_spec == "['198×99', '4.5', '7', '11']":
            cross_section_area = 23.18
            linear_density = 18.2
            section_modulus = 160
        elif h_beam_spec == "['200×100', '5.5', '8', '11']":
            cross_section_area = 27.16
            linear_density = 21.3
            section_modulus = 184
        elif h_beam_spec == "['194×150', '6', '9', '13']":
            cross_section_area = 39.01
            linear_density = 30.6
            section_modulus = 277
        elif h_beam_spec == "['200×200', '8', '12', '13']":
            cross_section_area = 63.53
            linear_density = 49.9
            section_modulus = 472
        elif h_beam_spec == "['200×204', '12', '12', '13']":
            cross_section_area = 71.53
            linear_density = 56.2
            section_modulus = 498
        elif h_beam_spec == "['208×202', '10', '16', '13']":
            cross_section_area = 83.69
            linear_density = 65.7
            section_modulus = 628
        elif h_beam_spec == "['248×124', '5', '8', '12']":
            cross_section_area = 32.68
            linear_density = 25.7
            section_modulus = 285
        elif h_beam_spec == "['250×125', '6', '9', '12']":
            cross_section_area = 37.66
            linear_density = 29.6
            section_modulus = 324
        elif h_beam_spec == "['244×175', '7', '11', '16']":
            cross_section_area = 56.24
            linear_density = 44.1
            section_modulus = 502
        elif h_beam_spec == "['244×252', '11', '11', '16']":
            cross_section_area = 82.06
            linear_density = 64.4
            section_modulus = 720
        elif h_beam_spec == "['248×249', '8', '13', '16']":
            cross_section_area = 84.7
            linear_density = 66.5
            section_modulus = 801
        elif h_beam_spec == "['250×250', '9', '14', '16']":
            cross_section_area = 92.18
            linear_density = 72.4
            section_modulus = 867
        elif h_beam_spec == "['250×255', '14', '14', '16']":
            cross_section_area = 104.7
            linear_density = 82.2
            section_modulus = 919
        elif h_beam_spec == "['298×149', '5.5', '8', '13']":
            cross_section_area = 40.8
            linear_density = 32
            section_modulus = 424
        elif h_beam_spec == "['300×150', '6.5', '9', '13']":
            cross_section_area = 46.78
            linear_density = 36.7
            section_modulus = 481
        elif h_beam_spec == "['294×200', '8', '12', '18']":
            cross_section_area = 72.38
            linear_density = 56.8
            section_modulus = 771
        elif h_beam_spec == "['298×201', '9', '14', '18']":
            cross_section_area = 83.36
            linear_density = 65.4
            section_modulus = 893
        elif h_beam_spec == "['294×302', '12', '12', '18']":
            cross_section_area = 107.7
            linear_density = 84.5
            section_modulus = 1150
        elif h_beam_spec == "['298×299', '9', '14', '18']":
            cross_section_area = 110.8
            linear_density = 87
            section_modulus = 1270
        elif h_beam_spec == "['300×300', '10', '15', '18']":
            cross_section_area = 119.8
            linear_density = 94
            section_modulus = 1360
        elif h_beam_spec == "['300×305', '15', '15', '18']":
            cross_section_area = 134.8
            linear_density = 106
            section_modulus = 1440
        elif h_beam_spec == "['304×301', '11', '17', '18']":
            cross_section_area = 134.8
            linear_density = 106
            section_modulus = 1540
        elif h_beam_spec == "['310×305', '15', '20', '18']":
            cross_section_area = 165.3
            linear_density = 130
            section_modulus = 1850
        elif h_beam_spec == "['310×310', '20', '20', '18']":
            cross_section_area = 180.8
            linear_density = 142
            section_modulus = 1930
        elif h_beam_spec == "['346×174', '6', '9', '14']":
            cross_section_area = 52.68
            linear_density = 41.4
            section_modulus = 641
        elif h_beam_spec == "['350×175', '7', '11', '14']":
            cross_section_area = 63.14
            linear_density = 49.6
            section_modulus = 775
        elif h_beam_spec == "['354×176', '8', '13', '14']":
            cross_section_area = 73.68
            linear_density = 57.8
            section_modulus = 909
        elif h_beam_spec == "['336×249', '8', '12', '20']":
            cross_section_area = 88.15
            linear_density = 69.2
            section_modulus = 1100
        elif h_beam_spec == "['340×250', '9', '14', '20']":
            cross_section_area = 146
            linear_density = 115
            section_modulus = 1940
        elif h_beam_spec == "['338×351', '13', '13', '20']":
            cross_section_area = 135.3
            linear_density = 106
            section_modulus = 1670
        elif h_beam_spec == "['344×348', '10', '16', '20']":
            cross_section_area = 146
            linear_density = 115
            section_modulus = 1940
        elif h_beam_spec == "['344×354', '16', '16', '20']":
            cross_section_area = 166.6
            linear_density = 131
            section_modulus = 2050
        elif h_beam_spec == "['350×350', '12', '19', '20']":
            cross_section_area = 173.9
            linear_density = 137
            section_modulus = 2300
        elif h_beam_spec == "['350×357', '19', '19', '20']":
            cross_section_area = 198.4
            linear_density = 156
            section_modulus = 2450
        elif h_beam_spec == "['396×199', '7', '11', '16']":
            cross_section_area = 72.16
            linear_density = 56.6
            section_modulus = 1010
        elif h_beam_spec == "['400×200', '8', '13', '16']":
            cross_section_area = 84.12
            linear_density = 66
            section_modulus = 1190
        elif h_beam_spec == "['390×300', '10', '16', '22']":
            cross_section_area = 136
            linear_density = 107
            section_modulus = 1980
        elif h_beam_spec == "['388×402', '15', '15', '22']":
            cross_section_area = 178.5
            linear_density = 140
            section_modulus = 2520
        elif h_beam_spec == "['394×398', '11', '18', '22']":
            cross_section_area = 186.8
            linear_density = 147
            section_modulus = 2850
        elif h_beam_spec == "['394×405', '18', '18', '22']":
            cross_section_area = 214.4
            linear_density = 168
            section_modulus = 3030
        elif h_beam_spec == "['400×400', '13', '21', '22']":
            cross_section_area = 218.7
            linear_density = 172
            section_modulus = 3330
        elif h_beam_spec == "['400×408', '21', '21', '22']":
            cross_section_area = 250.7
            linear_density = 197
            section_modulus = 3540
        elif h_beam_spec == "['406×403', '16', '24', '22']":
            cross_section_area = 254.9
            linear_density = 200
            section_modulus = 3840
        elif h_beam_spec == "['414×405', '18', '28', '22']":
            cross_section_area = 295.4
            linear_density = 232
            section_modulus = 4480
        elif h_beam_spec == "['428×407', '20', '35', '22']":
            cross_section_area = 360.7
            linear_density = 283
            section_modulus = 5570
        elif h_beam_spec == "['442×413', '26', '42', '22']":
            cross_section_area = 444.2
            linear_density = 349
            section_modulus = 6810
        elif h_beam_spec == "['452×416', '29', '47', '22']":
            cross_section_area = 499
            linear_density = 392
            section_modulus = 7670
        elif h_beam_spec == "['458×417', '30', '50', '22']":
            cross_section_area = 528.6
            linear_density = 415
            section_modulus = 8170
        elif h_beam_spec == "['462×419', '32', '52', '22']":
            cross_section_area = 554.5
            linear_density = 435
            section_modulus = 8550
        elif h_beam_spec == "['472×422', '35', '57', '22']":
            cross_section_area = 610.5
            linear_density = 479
            section_modulus = 9450
        elif h_beam_spec == "['484×426', '39', '63', '22']":
            cross_section_area = 680.5
            linear_density = 534
            section_modulus = 10600
        elif h_beam_spec == "['498×432', '45', '70', '22']":
            cross_section_area = 770.1
            linear_density = 605
            section_modulus = 12000
        elif h_beam_spec == "['446×199', '8', '12', '18']":
            cross_section_area = 84.3
            linear_density = 66.2
            section_modulus = 1290
        elif h_beam_spec == "['450×200', '9', '14', '18']":
            cross_section_area = 96.76
            linear_density = 76
            section_modulus = 1490
        elif h_beam_spec == "['434×299', '10', '15', '24']":
            cross_section_area = 135
            linear_density = 106
            section_modulus = 2160
        elif h_beam_spec == "['440×300', '11', '18', '24']":
            cross_section_area = 157.4
            linear_density = 124
            section_modulus = 2550
        elif h_beam_spec == "['496×199', '9', '14', '20']":
            cross_section_area = 101.3
            linear_density = 79.5
            section_modulus = 1690
        elif h_beam_spec == "['500×200', '10', '16', '20']":
            cross_section_area = 114.2
            linear_density = 89.6
            section_modulus = 1910
        elif h_beam_spec == "['506×201', '11', '19', '20']":
            cross_section_area = 131.3
            linear_density = 103
            section_modulus = 2230
        elif h_beam_spec == "['482×300', '11', '15', '26']":
            cross_section_area = 145.5
            linear_density = 114
            section_modulus = 2500
        elif h_beam_spec == "['488×300', '11', '18', '26']":
            cross_section_area = 163.5
            linear_density = 128
            section_modulus = 2910
        elif h_beam_spec == "['596×199', '10', '15', '22']":
            cross_section_area = 120.5
            linear_density = 94.6
            section_modulus = 2310
        elif h_beam_spec == "['600×200', '11', '17', '22']":
            cross_section_area = 134.4
            linear_density = 106
            section_modulus = 2590
        elif h_beam_spec == "['606×201', '12', '20', '22']":
            cross_section_area = 152.5
            linear_density = 120
            section_modulus = 2980
        elif h_beam_spec == "['612×202', '13', '23', '22']":
            cross_section_area = 170.7
            linear_density = 134
            section_modulus = 3380
        elif h_beam_spec == "['582×300', '12', '17', '28']":
            cross_section_area = 174.5
            linear_density = 137
            section_modulus = 3530
        elif h_beam_spec == "['588×300', '12', '20', '28']":
            cross_section_area = 192.5
            linear_density = 151
            section_modulus = 4020
        elif h_beam_spec == "['594×302', '14', '23', '28']":
            cross_section_area = 222.4
            linear_density = 175
            section_modulus = 4620
        elif h_beam_spec == "['692×300', '13', '20', '28']":
            cross_section_area = 211.5
            linear_density = 166
            section_modulus = 4980
        elif h_beam_spec == "['696×300', '13', '22', '28']":
            cross_section_area = 223.5
            linear_density = 175
            section_modulus = 5370
        elif h_beam_spec == "['700×300', '13', '24', '28']":
            cross_section_area = 235.5
            linear_density = 185
            section_modulus = 5760
        elif h_beam_spec == "['702×301', '14', '25', '28']":
            cross_section_area = 248.5
            linear_density = 195
            section_modulus = 6030
        elif h_beam_spec == "['708×302', '15', '28', '28']":
            cross_section_area = 273.6
            linear_density = 215
            section_modulus = 6700
        elif h_beam_spec == "['714×303', '16', '31', '28']":
            cross_section_area = 298.9
            linear_density = 235
            section_modulus = 7370
        elif h_beam_spec == "['792×300', '14', '22', '28']":
            cross_section_area = 243.4
            linear_density = 191
            section_modulus = 6410
        elif h_beam_spec == "['796×300', '14', '24', '28']":
            cross_section_area = 255.4
            linear_density = 200
            section_modulus = 6850
        elif h_beam_spec == "['800×300', '14', '26', '28']":
            cross_section_area = 267.4
            linear_density = 210
            section_modulus = 7290
        elif h_beam_spec == "['802×301', '15', '27', '28']":
            cross_section_area = 281.5
            linear_density = 221
            section_modulus = 7620
        elif h_beam_spec == "['808×302', '16', '30', '28']":
            cross_section_area = 307.6
            linear_density = 241
            section_modulus = 8400
        elif h_beam_spec == "['814×303', '17', '33', '28']":
            cross_section_area = 333.9
            linear_density = 262
            section_modulus = 9180
        elif h_beam_spec == "['890×299', '15', '23', '28']":
            cross_section_area = 270.9
            linear_density = 213
            section_modulus = 7760
        elif h_beam_spec == "['894×299', '15', '25', '28']":
            cross_section_area = 282.8
            linear_density = 222
            section_modulus = 8260
        elif h_beam_spec == "['900×300', '16', '28', '28']":
            cross_section_area = 309.8
            linear_density = 243
            section_modulus = 9140
        elif h_beam_spec == "['906×301', '17', '31', '28']":
            cross_section_area = 336.8
            linear_density = 264
            section_modulus = 10000
        elif h_beam_spec == "['912×302', '18', '34', '28']":
            cross_section_area = 364
            linear_density = 286
            section_modulus = 10900
        elif h_beam_spec == "['918×303', '19', '37', '28']":
            cross_section_area = 391.3
            linear_density = 307
            section_modulus = 11800

        cross_section_area *= 100  # cm^2 to mm^2
        return cross_section_area, linear_density, section_modulus
