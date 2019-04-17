# Template Structure for a Runway Model

<img src="https://i.imgur.com/OWb3FhB.png" width=100/>

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
import runway

# Setup the model, initialize weights, set the configs of the model, etc.
# Every model will have a different set of configurations and requirements.
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of supported configs.
# The setup function should return the model ready to be used.
@runway.setup(options={'truncation': 'float', 'seed': 'integer'})
def setup(opts):
    model = init_model(opts)
    return model

# Every model needs to have at least one command. Every command allows to send inputs and process outputs. 
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of supported inputs and outputs.
@runway.command(name='generate', inputs={'caption': 'text'}, outputs={'result': 'image'})
def generate(model, inputs):
    output = model.run_on_input(inp) # Placeholder
    return {
        'image': output
    }
```

## runway.yml

The Runway `runway.yml` contains all related meta-data of the model as well as the instructions and build process. The bare minimum requirements for a model using CUDA is the following:

```yaml
python: 3.6
cuda: 9.2
files:
  ignore:
    - tests/*
```
