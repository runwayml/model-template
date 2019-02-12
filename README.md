# Template Structure for a Runway Model

This repository contains a template structure to serve as a reference when porting machine learning models to [Runway](https://runwayapp.ai/). This references is written for python based models.

> If you are looking for a tutorial on how to port your own model, see: [https://docs.runwayapp.ai/#/importing](https://docs.runwayapp.ai/#/importing)

Every Runway model should have:
- An **entrypoint** with the Runway specifications. In this case, [`model.py`](model.py).
- A [`runway.yml`](runway.yml) file with meta-data.

## Entrypoint

The [entrypoint](model.py) file is the file Runway will use to query the model. This file can have any name you want, but we recommend calling it `model.py`.

### Basic Structure

```python
# Import the Runway SDK. Please install it first (pip install runway-python).
from runway import RunwayModels

# Create a new Runway Model.
my_model = RunwayModel()

# Setup the model, initialize weights, set the configs of the model, etc.
# Every model will have a different set of configurations and requirements.
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of supported configs.
# The setup function should return the model ready to be used.
@my_model.setup(options={'some_config_as_slider': 'float'})
def setup(opts):
    model = load_your_model()
    return model

# Every model needs to have at least one command. Every command allows to send inputs and process outputs. 
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of supported inputs and outputs.
@my_model.command('generate', inputs={'caption': 'text'}, outputs={'result': 'image'})
def generate(model, inp):
    output = model.run_on_input(inp)
    return dict(image=output)

# Run the model
if __name__ == "__main__":
    my_model.run()
```

## runway.yml

The Runway `runway.yml` contains all related meta-data of the model as well as the instructions and build process. The bare minimum requirements for a model using CUDA is the following:

```yaml
name: My_Model
description: A template model structure for Runway
license: MIT
python: 3.6
cuda: 9.2
entrypoint: python model.py
build_steps:
  - pip install -r requirements.txt  
```