# %%


# %%
%matplotlib inline
# Dependencies
# Import the dependencies.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from citipy import citipy
# Import the requests library.
import requests

# Import the API key.
from config import weather_api_key
from datetime import datetime
import time
from scipy.stats import linregress
