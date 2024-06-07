class IBeamStandard:
    def __init__(self, loader):
        self.loader = loader

    def load_i_beam_spec(self):
        last_row = self.loader.load_data()
        if last_row is not None:
            _, _, i_beam_spec, _, _ = self.loader.process_data(last_row)
            return i_beam_spec
        else:
            return None

    def calculate_specs(self, i_beam_spec):
        cross_section_area = 0
        linear_density = 0
        if i_beam_spec == "['100×75', '5', '8', '7', '3.5']":
            cross_section_area = 16.43
            linear_density = 12.9
            section_modulus = 56.2
        elif i_beam_spec == "['125×75', '5.5', '9.5', '9', '4.5']":
            cross_section_area = 20.45
            linear_density = 16.1
            section_modulus = 86
        elif i_beam_spec == "['150×75', '5.5', '9.5', '9', '4.5']":
            cross_section_area = 21.83
            linear_density = 17.1
            section_modulus = 109
        elif i_beam_spec == "['150×125', '8.5', '14', '13', '6.5']":
            cross_section_area = 46.15
            linear_density = 36.2
            section_modulus = 235
        elif i_beam_spec == "['180×100', '6', '10', '10', '5']":
            cross_section_area = 30.06
            linear_density = 23.6
            section_modulus = 186
        elif i_beam_spec == "['200×100', '7', '10', '10', '5']":
            cross_section_area = 33.06
            linear_density = 26
            section_modulus = 217
        elif i_beam_spec == "['200×150', '9', '16', '15', '7.5']":
            cross_section_area = 64.16
            linear_density = 50.4
            section_modulus = 446
        elif i_beam_spec == "['250×125', '7.5', '12.5', '12', '6']":
            cross_section_area = 48.79
            linear_density = 38.3
            section_modulus = 414
        elif i_beam_spec == "['250×125', '10', '19', '21', '10.5']":
            cross_section_area = 70.73
            linear_density = 55.5
            section_modulus = 585
        elif i_beam_spec == "['300×150', '8', '13', '12', '6']":
            cross_section_area = 61.58
            linear_density = 48.3
            section_modulus = 632
        elif i_beam_spec == "['300×150', '10', '18.5', '19', '9.5']":
            cross_section_area = 83.47
            linear_density = 65.5
            section_modulus = 849
        elif i_beam_spec == "['300×150', '11.5', '22', '23', '11.5']":
            cross_section_area = 97.88
            linear_density = 76.8
            section_modulus = 978
        elif i_beam_spec == "['350×150', '9', '15', '13', '6.5']":
            cross_section_area = 74.58
            linear_density = 58.5
            section_modulus = 870
        elif i_beam_spec == "['350×150', '12', '24', '25', '12.5']":
            cross_section_area = 111.1
            linear_density = 87.2
            section_modulus = 1280
        elif i_beam_spec == "['400×150', '10', '18', '17', '8.5']":
            cross_section_area = 91.73
            linear_density = 72
            section_modulus = 1200
        elif i_beam_spec == "['400×150', '12.5', '25', '27', '13.5']":
            cross_section_area = 122.1
            linear_density = 95.8
            section_modulus = 1580
        elif i_beam_spec == "['450×175', '11', '20', '19', '9.5']":
            cross_section_area = 116.8
            linear_density = 91.7
            section_modulus = 1740
        elif i_beam_spec == "['450×175', '13', '26', '27', '13.5']":
            cross_section_area = 146.1
            linear_density = 115
            section_modulus = 2170
        elif i_beam_spec == "['600×190', '13', '25', '25', '12.5']":
            cross_section_area = 169.4
            linear_density = 133
            section_modulus = 3280
        elif i_beam_spec == "['600×190', '16', '35', '38', '19']":
            cross_section_area = 224.5
            linear_density = 176
            section_modulus = 4330
        cross_section_area *= 100  # cm^2 to mm^2
        return cross_section_area, linear_density, section_modulus
