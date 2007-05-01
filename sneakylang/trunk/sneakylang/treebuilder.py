# -*- coding: utf-8 -*-

###
# SneakyLang: Extensible WikiFramework
#Copyright (C) 2007 Lukas "Almad" Linhart http://www.almad.net/
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
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
###

class TreeBuilder(object):
    def __init__(self):
        self.tree = []
        # pointer to actual node
        self._actual_node = None
    
    def append(self, node, move_actual=False):
        if self._actual_node is None:
            self.tree.append(node)
        else:
            self._actual_node.add_child(node)
        if move_actual is True:
            self._actual_node = node
            
    def move_up(self):
        if self.actual_node.parent is None:
            raise ValueError, 'Cannot move up as there is no parent of current node'
        else:
            self._actual_node = self.actual_node.parent
        
    def get_actual_node(self):
        return self._actual_node
    
    actual_node = property(fget=get_actual_node)