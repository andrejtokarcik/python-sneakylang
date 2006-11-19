# -*- coding: utf-8 -*-

""" Expanders for nodes
"""

###
# SneakyLang: Extensible WikiFramework
#Copyright (C) 2006 Lukas "Almad" Linhart http://www.almad.net/
# and contributors, for complete list see
# http://projects.almad.net/czechtile/wiki/Contributors
#
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 2.1 of the License, or (at your option) any later version.
#
#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#Lesser General Public License for more details.
#
#You should have received a copy of the GNU Lesser General Public
#License along with this library; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
###

class Expander:
    def expand(self, node, format, node_map):
        pass

class TextNodeExpander(Expander):
    def expand(self, node, *args, **kwargs):
        return node.content

def expand(node_list, format, node_map):
    if type(node_list) != type([]):
        node_list = [node_list]
    return ''.join([node_map[format][node.__class__]().expand(node, format, node_map) for node in node_list])