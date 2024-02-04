#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import maya.cmds as cmds


def toggle_lock_vertex():
    list_selected_vertex = cmds.ls(sl=True, flatten=True, type="float3")
    cmds.undoInfo(openChunk=True)
    for selected_vertex in list_selected_vertex:
        cmds.setAttr(selected_vertex + ".px", lock=not (cmds.getAttr(selected_vertex + ".px", lock=True)))
        cmds.setAttr(selected_vertex + ".py", lock=not (cmds.getAttr(selected_vertex + ".py", lock=True)))
        cmds.setAttr(selected_vertex + ".pz", lock=not (cmds.getAttr(selected_vertex + ".pz", lock=True)))
    cmds.undoInfo(closeChunk=True)


def lock_vertex_lock():
    list_selected_vertex = cmds.ls(sl=True, flatten=True, type="float3")
    cmds.undoInfo(openChunk=True)
    for selected_vertex in list_selected_vertex:
        cmds.setAttr(selected_vertex + ".px", lock=True)
        cmds.setAttr(selected_vertex + ".py", lock=True)
        cmds.setAttr(selected_vertex + ".pz", lock=True)
    cmds.undoInfo(closeChunk=True)


def unlock_vertex_lock():
    list_selected_vertex = cmds.ls(sl=True, flatten=True, type="float3")
    cmds.undoInfo(openChunk=True)
    for selVtx in list_selected_vertex:
        cmds.setAttr(selVtx + ".px", lock=False)
        cmds.setAttr(selVtx + ".py", lock=False)
        cmds.setAttr(selVtx + ".pz", lock=False)
    cmds.undoInfo(closeChunk=True)

