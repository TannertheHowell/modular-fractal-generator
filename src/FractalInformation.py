def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary  	  	  
    contains a key by the name of 'name'  	  	  

    When the key 'name' is present in the fractal configuration data repository  	  	  
    dictionary, return its value.  	  	  

    Return False otherwise  	  	  
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key


patternDict = {
        # The full Phoenix set
        'phoenix': {
            'type': 'phoenix',
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'type': 'phoenix',
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'type': 'phoenix',
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'type': 'phoenix',
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },

        'mandelbrot': {
            'type': 'mandelbrot',
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLength': 2.5,
        },

        'mandelbrot-zoomed': {
            'type': 'mandelbrot',
            'centerX': -1.0,
            'centerY': 0.0,
            'axisLength': 1.0,
        },

        'spiral0': {
            'type': 'mandelbrot',
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLength': 0.004978179931102462,
        },

        'spiral1': {
            'type': 'mandelbrot',
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLength': 0.002,
        },

        'seahorse': {
            'type': 'mandelbrot',
            'centerX': -0.748,
            'centerY': -0.102,
            'axisLength': 0.008,
        },

        'elephants': {
            'type': 'mandelbrot',
            'centerX': 0.3015,
            'centerY': -0.0200,
            'axisLength': 0.03,
        },

        'leaf': {
            'type': 'mandelbrot',
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLength': 0.000051248888,
        },

        'starfish': {
            'type': 'mandelbrot',
            'centerX': -0.463595023481762,
            'centerY': 0.598380871135558,
            'axisLength': 0.00128413675654471,
        },
    }
