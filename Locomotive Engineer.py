"""Functions which helps the locomotive engineer to keep track of the train."""
# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    """Return a list of wagons.
 
    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)
# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
 
    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return   [each_wagons_id[each_wagons_id.index(1)]] + missing_wagons + each_wagons_id[each_wagons_id.index(1) + 1:] + each_wagons_id[:each_wagons_id.index(1)]
# TODO: define the 'add_missing_stops()' function
def add_missing_stops(adict, **kwargs):
    """Add missing stops to route dict.
 
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    adict["stops"] = [x for x in kwargs.values()]
    return adict
# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.
 
    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return dict(list(route.items()) + list(more_route_information.items()))
# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.
 
    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [[wagons_rows[0][0], wagons_rows[1][0], wagons_rows[2][0]], [wagons_rows[0][1], wagons_rows[1][1], wagons_rows[2][1]], [wagons_rows[0][2], wagons_rows[1][2], wagons_rows[2][2]]]
