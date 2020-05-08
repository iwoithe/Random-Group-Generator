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

def generate_groups(names, names_shuffled=False, num_groups=None, people_per_group=None):
    if (people_per_group == None) and (num_groups != None):
        people_per_group = get_people_per_group(num_groups)
    else:
        people_per_group = 1

    if !(names_shuffled):
        random.shuffle()

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
    people_per_group = int(num_people / num_groups) # Maybe a bug. If
                                                    # there is an
                                                    # incorrect number
                                                    # of groups, try
                                                    # rounding down.
    return people_per_group
