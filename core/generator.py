#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generator.py
#
#  Copyright 2020 iwoithe <iwoithe@just42.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import random
from math import ceil

def generate_groups(names, names_shuffled=False, num_groups=None, people_per_group=None):
    ''' Generates the groups. The parameters are as follows:
            names: the list of names
            names_shuffled: this states whether or not the names
                            list has been randomized or not
            num_groups: the number of groups to generate
            people_per_group: the number of people per group

        The groups are generated in the following format and then
        returned:
            [[1, ['a', 'b', 'c']],
             [2, ['d', 'e', 'f']],
             [3, ['g', 'h']]
        The first value is the group number (used more as a
        reference when debugging), and the second value is
        the people in the group.
        '''

    if (names_shuffled != True):
        random.shuffle(names)

    if (num_groups != None) and (people_per_group == None):
        people_per_group = get_people_per_group(len(names), num_groups)
    elif (num_groups == None) and (people_per_group != None):
        pass
    else:
        people_per_group = 1

    # In the future, see if using numpy arrays increase performance
    groups = []
    group_num = 1

    while len(names) > 0:
        people_names = []
        if len(names) > people_per_group:
            people_names = names[:people_per_group]
            del names[:people_per_group]
            groups.append([group_num, people_names])
            group_num += 1
        else:
            people_names = names.copy()
            del names[:len(people_names)]
            groups.append([group_num, people_names])

    return groups

def get_people_per_group(num_people, num_groups):
    ''' Converts the number of groups to people per group '''
    people_per_group = ceil(num_people / num_groups)
    return people_per_group
