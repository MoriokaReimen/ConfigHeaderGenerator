from dataclasses import dataclass

@dataclass
class ConfigData:
        symbol : str
        description : str
        detail : str
        enable : bool

@dataclass
class ValConfigData:
        symbol : str
        description : str
        detail : str
        value : str
        enable : bool

@dataclass
class HeaderConfig:
    path : str
    header : str
    footer : str
