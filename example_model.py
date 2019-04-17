import random
from PIL import Image

class ExampleModel():

    def __init__(self, options):
        random.seed(options['seed'])
        self.truncation = options['truncation']

    # Generate an image based on some text.
    def run_on_input(self, caption_text):

        # This is an example of how you could use some input from
        # @runway.setup(), like options['truncation'], later inside a
        # function called by @runway.command().
        text = caption_text[0:self.truncation]

        # Return a red image if the input text is "red",
        # otherwise return a blue image.
        if text == 'red':
            return Image.new('RGB', (512, 512), color = 'red')
        else:
            return Image.new('RGB', (512, 512), color = 'blue')
