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
