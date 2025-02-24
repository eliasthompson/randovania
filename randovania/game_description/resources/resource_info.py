import typing
from typing import Union, Tuple, Iterator

from randovania.game_description.resources.item_resource_info import ItemResourceInfo
from randovania.game_description.resources.pickup_index import PickupIndex
from randovania.game_description.resources.simple_resource_info import SimpleResourceInfo
from randovania.game_description.resources.trick_resource_info import TrickResourceInfo
from randovania.game_description.world.node_identifier import NodeIdentifier

ResourceInfo = Union[SimpleResourceInfo, ItemResourceInfo, TrickResourceInfo,
                     PickupIndex, NodeIdentifier]
ResourceQuantity = Tuple[ResourceInfo, int]
ResourceGainTuple = Tuple[ResourceQuantity, ...]
ResourceGain = Iterator[ResourceQuantity]
CurrentResources = dict[ResourceInfo, int]


def add_resource_gain_to_current_resources(resource_gain: ResourceGain,
                                           resources: CurrentResources) -> CurrentResources:
    """
    Adds all resources from the given gain to the given CurrentResources
    :param resource_gain:
    :param resources:
    :return: resources
    """
    for resource, quantity in resource_gain:
        resources[resource] = resources.get(resource, 0) + quantity
    return resources


def add_resources_into_another(target: CurrentResources, source: CurrentResources) -> None:
    resource_gain = typing.cast(ResourceGain, source.items())
    add_resource_gain_to_current_resources(resource_gain, target)


def convert_resource_gain_to_current_resources(resource_gain: ResourceGain) -> CurrentResources:
    """
    Creates a CurrentResources with all resources of the given ResourceGain
    :param resource_gain:
    :return:
    """
    result = {}
    add_resource_gain_to_current_resources(resource_gain, result)
    return result
