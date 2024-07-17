"""===================================================================================
Helper function to render nested data structures recursively into one formatted string
Function considers outmost scope - that of the basic variable - to be lvl -0
For the moment we use a function, can be reworked to be a class.
There is no need, however.

Regarding collections (list, tupple, dict, set), function only handles
<list> and <dict>.
<set> and <tuple> type collections are returned undetailed, as(if) immutable items.

Description:
Variable is lvl:0
All nested layers below are numbered with integers. These integers can be printed in
front of each line, using: nrs (bool). If True, layer numbers will be shown.

symbols can be defined in advance, by "s"* -parameters.
lvl - defines the default level we start from. USE 1 by default.
lvl is a powerfull tool though: you can shift (flatten) higher lvl layers to the left,
by decreasing the lvl integer
Returned data is a fromatted string, meaning, you only need to print it.
==================================================================== by Sziller ==="""


def rdf(data,
        string: str = "",
        nrs: bool = False,
        lvl: int = 1,
        lvl_set: set or None = None,
        sf: str = '\u2502',
        sj: str = '\u251c' + '\u2500' + '\u2500',
        sc: str = '\u2514' + '\u2500' + '\u2500',
        sn: str = " ",
        sl: str = '\u2022',
        **kwargs):
    """ Function name: rdf =============================================================================================
    Template: rdap as in (R)ecursive (D)ata (F)ormatter
    This is a function to show a dictionary or list of any deepness in a tree structure.
    Keep it intact, only develop in general ways.
    :param data:        the list or dict (or any other datatype in fact) to be processed.
                        Can be any lvl deep. Values are distinguished: either...
                        - dict or
                        - list or
                        - any other types.
    :param string: str - default string to be added to. The string function returns.
    :param nrs:   way of numbering data:
                                True  - all items will be numbered
                                False - only lists having sublists will be numbered
                                None  - no line will be numbered
    :param lvl:           a 'static' type counter. By-default: 0. Can be modified if needed to.
                            It is defined, in order to avoid the usage of global parameters.
    :param sf: str - symbol for flow        - tree rendering graphics
    :param sj: str - symbol for juncture    - tree rendering graphics
    :param sc: str - symbol for closing     - tree rendering graphics
    :param sn: str - symbol for empty branch
    :param sl: str - symbol for list - prefix
    :param lvl_set: set - of levels actully in use, to indicate if flow symbol is used.
    :return: nothing as a template
    ============================================================================================== by Sziller ==="""
    # lvl = max(lvl, 1)
    symbols = {'sf': sf, 'sj': sj, 'sc': sc, 'sn': sn, 'sl': sl}
    if lvl_set is None: lvl_set = {lvl}
    if isinstance(data, list):
        for c, item in enumerate(data):
            is_end = c + 1 == len(data)
            if is_end: lvl_set.discard(lvl)
            if isinstance(item, list):
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + "{} [.] list\n".format(sl))
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
                lvl_set.add(lvl + 1)
                string = rdf(item, string, nrs, lvl + 1, lvl_set, **symbols)  # <-- recursive call
            elif isinstance(item, dict):
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + "{} {{.}} dict\n".format(sl))
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
                lvl_set.add(lvl + 1)
                string = rdf(item, string, nrs, lvl + 1, lvl_set, **symbols)  # <-- recursive call
            else:
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + "{} {}\n".format(sl, item))
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
        return string

    elif isinstance(data, dict):
        for c, key in enumerate(list(data.keys())):
            value = data[key]
            is_end = c + 1 == len(data)
            if is_end: lvl_set.discard(lvl)
            if isinstance(value, dict):
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + '{}: '.format(key) + "{...} dict\n")
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
                lvl_set.add(lvl + 1)
                string = rdf(value, string, nrs, lvl + 1, lvl_set, **symbols)  # <-- recursive call
            elif isinstance(value, list):
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + '{}: '.format(key) + "[...] list\n")
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
                lvl_set.add(lvl + 1)
                string = rdf(value, string, nrs, lvl + 1, lvl_set, **symbols)  # <-- recursive call
            else:
                txt = ("".join(["{:<4}".format({True: sf, False: sn}[_ in lvl_set]) for _ in range(1, lvl)]) +
                       "{:<4}".format({True: sc, False: sj}[is_end]) + "{}: {}\n".format(key, value))
                line = {False: txt, True: '{:>2}  '.format(lvl) + txt}
                string += line[nrs]
        return string
    else:
        line = {
            False:                          (lvl-1) * "{:<4}".format(sf) + "{:<4}".format(sj) + ">>> {}\n".format(data),
            True: '{:>2}  '.format(lvl) + (lvl-1) * "{:<4}".format(sf) + "{:<4}".format(sj) + ">>> {}\n".format(data)}
        string += line[nrs]
        return string


if __name__  == "__main__":
    temp = {
        "key_0": {
            "key_00": 0,
            'key_10': 'text_x',
            'key_20': ['item', {"key_200": "data_x", "key_201": "data_y"}, False, True, [0, 0, 3], 10.33],
            'key_30': ["item_x", "item_y"]},
        "key_1": {
            "key_01": 1,
            'key_11': 'text_y',
            'key_21': {},
            'key_31': ["item_x", "item_y", [0, 1, 2, 3, 4], "item_z"]},
        "key_2": {
            "key_02": 2,
            'key_12': None,
            'key_22': [],
            'key_32': [None, False, True, False],
            'key_42': {'key_042': [], 'key_142': None, 'key_242': [0, 1, 2]}},
        "key_4": True,
        "key_5": 
            [0, 1, 2, 3, ['a', 'b', 'c', 'd', {'k1': [True, False, {'k2': [0, [1, 1, {"kz": [0, 3]}], 2], 'kx': None}, 77 ] }, "f"], 5],
        "key_6": "sziller"
    }
    
    title = "temp - {}\n".format(type(temp))
    charset = {'sf': '\u2502',
               'sj': '\u251c' + '\u2500' + '\u2500',
               'sc': '\u2514' + '\u2500' + '\u2500',
               'sn': " ",
               'sl': '\u2022'}

    a = rdf(data=temp, string=title, **charset)
    print(a)

    temp = [[1, 2, 3, 4], True, {1, 2}, (3, 4, 5), ([1, 2, 4], True), {True}]
    
    a = rdf(data=temp, **charset)
    print(a)
