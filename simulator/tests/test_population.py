from simulator.animal.create_population import *
import pytest


def test_generate_animal():
    assert type(generate_animal()) == dict
