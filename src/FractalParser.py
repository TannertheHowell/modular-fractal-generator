from pathlib import Path


class FractalParser:
    def __init__(self):
        pass

    def get_frac_dic(self, file_name):

        param_info = {
            'type': {
                'required_by': ['all'],
                'object_type': str
            },
            'centerx': {
                'required_by': ['all'],
                'object_type': float
            },
            'centery': {
                'required_by': ['all'],
                'object_type': float
            },
            'axislength': {
                'required_by': ['all'],
                'object_type': float
            },
            'pixels': {
                'required_by': ['all'],
                'object_type': int
            },
            'iterations': {
                'required_by': ['all'],
                'object_type': int
            },
            'creal': {
                'required_by': ['julia', 'phoenix'],
                'object_type': float
            },
            'cimag': {
                'required_by': ['julia', 'phoenix'],
                'object_type': float
            },
            'preal': {
                'required_by': ['phoenix'],
                'object_type': float
            },
            'pimag': {
                'required_by': ['phoenix'],
                'object_type': float
            }
        }

        fractal_white_list = ['phoenix', 'mandelbrot', 'julia', 'mandlebrot3']
        raw_dict = {}

        try:
            file = open(file_name)

            for line in file:
                line = line.strip().lower()
                # No more lines, continue on
                if not line:
                    continue

                # Skip the comments
                if line.startswith('#'):
                    continue

                split_line = line.split(":")

                if len(split_line) != 2:
                    raise RuntimeError("Line does not contain a correct format for a key value pair")

                key = split_line[0].strip()
                value = split_line[1].strip()

                if key in param_info.keys():
                    if key != 'type':
                        value = safe_convert(value, param_info[key]['object_type'])

                    if value is None:
                        raise RuntimeError("Invalid key value of: " + key + " was given")

                    if key == 'type' and value not in fractal_white_list:
                        raise NotImplementedError("An invalid fractal type was entered")

                    raw_dict[key] = value

        except FileNotFoundError:
            raise FileNotFoundError("File not found")

        for param_name, param_specs in param_info.items():
            if 'all' in param_specs['required_by']:
                if param_name not in raw_dict:
                    raise RuntimeError("Missing required parameter " + param_name + " in the fractal configuration file")
            elif raw_dict['type'] in param_specs['required_by']:
                if param_name not in raw_dict:
                    raise RuntimeError("Missing required parameter " + param_name + " in the fractal configuration file because it is a " + raw_dict['type'] + " type")

        final_dict = {}
        final_dict['min'] = {}
        final_dict['max'] = {}

        for key, value in raw_dict.items():
            if key == 'centerx':
                final_dict['min']['x'] = value - .5 * raw_dict['axislength']
                final_dict['max']['x'] = value + .5 * raw_dict['axislength']
            elif key == 'centery':
                final_dict['min']['y'] = value - .5 * raw_dict['axislength']
                final_dict['max']['y'] = value + .5 * raw_dict['axislength']
            elif key == 'pixels':
                final_dict['pixelsize'] = raw_dict['axislength'] / value
            else:
                final_dict[key] = value

        # Getting the file name from the full path and setting up the .png file naming
        p = Path(file_name)
        imagename = p.stem + ".png"
        final_dict['imagename'] = imagename

        return final_dict


def safe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' without crashing.

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or None if the conversion is not possible
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None


my_fractal_parser = FractalParser()

coral = my_fractal_parser.get_frac_dic('../data/coral.frac')
print(coral)

fjords = my_fractal_parser.get_frac_dic('../data/fjords.frac')
print(fjords)

minibrot = my_fractal_parser.get_frac_dic('../data/minibrot.frac')
print(minibrot)

mandelbrot = my_fractal_parser.get_frac_dic('../data/mandelbrot.frac')
print(mandelbrot)

phoenix = my_fractal_parser.get_frac_dic('../data/phoenix.frac')
print(phoenix)

invalid = my_fractal_parser.get_frac_dic('../data/invalid.frac')
print(invalid)
