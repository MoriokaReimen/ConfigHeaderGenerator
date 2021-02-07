import pytest
from Control import Control

def test_toml_loading():
    control = Control.Control()
    control.loadFile()
    configs = control.getConfigs()
    assert configs[0].symbol == "DEBUG"
    assert configs[0].description == "My Config"
    assert configs[0].detail == "my first config"
    assert configs[0].enable == True

    assert configs[1].symbol == "DEBUG2"
    assert configs[1].description == "My Config2"
    assert configs[1].detail == "my second config"
    assert configs[1].enable == False
