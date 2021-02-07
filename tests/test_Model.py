import pytest
import Model.TOMLParser


def test_parseHeaderConfig():
    toml_contents = """
    path = "./hoge.h"
    header = "header"
    footer = "footer"

    [[configs]]
    symbol = "DEBUG"
    description = "My Config"
    detail = "my first config"
    enable = true

    [[configs]]
    symbol = "DEBUG2"
    description = "My Config2"
    detail = "my second config"
    enable = false

    [[val_configs]]
    symbol = "DEBUG"
    description = "My Config"
    detail = "my first config"
    value = 1.5
    enable = true

    [[val_configs]]
    symbol = "DEBUG2"
    description = "My Config2"
    detail = "my second config"
    value = 30
    enable = false
    """
    toml_contents = toml_contents.lstrip()
    header_config = Model.TOMLParser.parseHeaderConfig(toml_contents)
    assert header_config.path == "./hoge.h"
    assert header_config.header == "header"
    assert header_config.footer == "footer"


def test_parseConfigData():
    toml_contents = """
    path = "./hoge.h"
    header = "#pragma once/* Generated:${DATE_TIME} */"
    footer = "/* End of hoge.h  Generated:${DATE_TIME} */"

    [[configs]]
    symbol = "DEBUG"
    description = "My Config"
    detail = "my first config"
    enable = true

    [[configs]]
    symbol = "DEBUG2"
    description = "My Config2"
    detail = "my second config"
    enable = false

    [[val_configs]]
    symbol = "DEBUG"
    description = "My Config"
    detail = "my first config"
    value = 1.5
    enable = true

    [[val_configs]]
    symbol = "DEBUG2"
    description = "My Config2"
    detail = "my second config"
    value = 30
    enable = false
    """
    toml_contents = toml_contents.lstrip()
    configs = Model.TOMLParser.parseConfigData(toml_contents)
    assert configs[0].symbol == "DEBUG"
    assert configs[0].description == "My Config"
    assert configs[0].detail == "my first config"
    assert configs[0].enable == True

    assert configs[1].symbol == "DEBUG2"
    assert configs[1].description == "My Config2"
    assert configs[1].detail == "my second config"
    assert configs[1].enable == False
