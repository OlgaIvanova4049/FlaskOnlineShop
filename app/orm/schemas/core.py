from enum import Enum


class EnvironmentSchema(str, Enum):
    dev = "dev"
    test = "test"
    prod = "prod"
