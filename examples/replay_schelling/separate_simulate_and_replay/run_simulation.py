import mesa

from examples.replay_schelling.server import (
    canvas_element,
    get_happy_agents,
    happy_chart,
    model_params,
)
from cachablemodel import CachableSchellingSimulate


server = mesa.visualization.ModularServer(
    # Note that Schelling was replaced by CachableSchellingSimulate here
    CachableSchellingSimulate,
    [canvas_element, get_happy_agents, happy_chart],
    "Schelling",
    model_params,
)

server.launch()