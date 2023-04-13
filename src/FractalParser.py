from pathlib import Path


class FractalParser:
    def __init__(self):
        pass

    def get_frac_dic(self, file_name):
        # this function will grab the .frac file
        file = open(file_name)
        white_list = ['type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations', 'creal', 'cimag']
        fractal_white_list = ['phoenix', 'mandelbrot', 'julia', 'spider']
        raw_dict = {}

        try:
            for line in file:
                line = line.strip().lower()
                # No more lines, continue on
                if not line:
                    continue

                # Skip the comments
                if line.startswith('#'):
                    continue

                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if key in white_list:
                    if key in ['centerx', 'centery', 'axislength', 'creal', 'cimag']:
                        value = safe_convert(value, float)
                    elif key in ['pixels', 'iterations']:
                        value = safe_convert(value, int)

                    if value is None:
                        raise RuntimeError("Invalid key value of: " + key)

                    if key == 'type' and value not in fractal_white_list:
                        raise NotImplementedError("There is an invalid fractal type")

                    raw_dict[key] = value

        except FileNotFoundError:
            raise FileNotFoundError("File not found")

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

# invalid = my_fractal_parser.get_frac_dic('../data/invalid.frac')
# print(invalid)
