# Copyright (C) 2019 Runway AI, Inc.

# This file is part of Runway-Model-Template

# Runway-Model-Template is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Runway-Model-Template is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with RunwayML.  If not, see <http://www.gnu.org/licenses/>.

# =========================================================================

# This example contains the minimum specifications and requirements
# to port a machine learning model to Runway.

# RUNWAY
# www.runwayapp.ai
# hello@runwayapp.ai

# =========================================================================

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
    model = load_your_model() # Placeholder
    return model

# Every model needs to have at least one command. Every command allows to send inputs and process outputs. 
# Check https://docs.runwayapp.ai/#/python-sdk to see a complete list of supported inputs and outputs.
@my_model.command('generate', inputs={'caption': 'text'}, outputs={'result': 'image'})
def generate(model, inp):
    output = model.run_on_input(inp) # Placeholder
    return dict(image=output)

# Run the model
if __name__ == "__main__":
    my_model.run()