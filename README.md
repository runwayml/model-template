# Runway Model Template

[![RunwayML Badge](https://open-app.runwayml.com/gh-badge.svg)](https://open-app.runwayml.com/)

This repository contains an example model template that can be used as reference when porting machine learning models to [Runway](https://runwayml.com/). This template uses the Runway Model SDK Python module, check out the [module documentation](https://sdk.runwayml.com) for more info.

> See the *Importing Models into Runway* [tutorial](https://learn.runwayml.com/#/how-to/import-models) for a walk-through illustrating how to port a model to Runway.

Each Runway model consists of two special files:

- [`runway_model.py`](runway_model.py): A Python script that imports the runway module (SDK) and exposes its interface via one or more `@runway.command()` functions. This file is used as the **entrypoint** to your model.
- [`runway.yml`](runway.yml): A configuration file that describes dependencies and build steps needed to build and run the model.

## The `runway_model.py` Entrypoint File

The [`runway_model.py`](runway_model.py) entrypoint file is the file the Runway app will use to query the model. This file can have any name you want, but we recommend calling it `runway_model.py`.

### Basic Structure

All Runway models expose a standard interface that allows the Runway desktop application to interact with them over HTTP. This is accomplished using three functions: `@runway.setup()`, `@runway.command()`, and `runway.run()`.

```python
import runway
from runway.data_types import number, text, image
from example_model import ExampleModel

# Setup the model, initialize weights, set the configs of the model, etc.
# Every model will have a different set of configurations and requirements.
# Check https://sdk.runwayml.com/en/latest/runway_module.html to see a complete
# list of supported configs. The setup function should return the model ready to
# be used.
setup_options = {
    'truncation': number(min=5, max=100, step=1, default=10),
    'seed': number(min=0, max=1000000)
}
@runway.setup(options=setup_options)
def setup(opts):
    msg = '[SETUP] Run with options: seed = {}, truncation = {}'
    print(msg.format(opts['seed'], opts['truncation']))
    model = ExampleModel(opts)
    return model

# Every model needs to have at least one command. Every command allows to send
# inputs and process outputs. To see a complete list of supported inputs and
# outputs data types: https://sdk.runwayml.com/en/latest/data_types.html
@runway.command(name='generate',
                inputs={ 'caption': text() },
                outputs={ 'image': image(width=512, height=512) })
def generate(model, args):
    print('[GENERATE] Ran with caption value "{}"'.format(args['caption']))
    # Generate a PIL or Numpy image based on the input caption, and return it
    output_image = model.run_on_input(args['caption'])
    return {
        'image': output_image
    }

if __name__ == '__main__':
    # run the model server using the default network interface and ports,
    # displayed here for convenience
    runway.run(host='0.0.0.0', port=8000)
```

See the [`example_model.py`](example_model.py) file for the simple `ExampleModel` class used in the example above.

## The `runway.yml` Config File

Each Runway model must have a [`runway.yml`](runway.yml) configuration file in its root directory. This file defines the steps needed to build and run your model for use with Runway. This file is written in YAML, a human-readable superset of JSON. Below is an example of a `runway.yml` file. This example file illustrates how you can provision your model’s environment.

```yaml
version: 0.1
python: 3.6
entrypoint: python runway_model.py
cuda: 9.2
framework: tensorflow
files:
    ignore:
        - image_dataset/*
build_steps:
    - pip install runway-python==0.1.0
    - pip install -r requirements.txt
```

## Testing your Model

While you're developing your model it's useful to run and test it locally.

```bash
## Optionally create and activate a Python 3 virtual environment
# virtualenv -p python3 venv && source venv/bin/activate

# Install the Runway Model SDK (`pip install runway-python`) and the Pillow
# image library, used in this example.
pip install -r requirements.txt

# Run the entrypoint script
python runway_model.py
```

You should see an output similar to this, indicating your model is running.

```
Setting up model...
[SETUP] Ran with options: seed = 0, truncation = 10
Starting model server at http://0.0.0.0:8000...
```

You can test your model once its running by POSTing a caption argument to the the `/generate` command.

```bash
curl \
    -H "content-type: application/json" \
    -d '{ "caption": "red" }' \
    http://localhost:8000/generate
```

You should receive a JSON object back, containing a cryptic base64 encoded URI string that represents a red image:

```
{"image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ..."}
```
