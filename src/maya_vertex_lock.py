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
    print("Vertex Lock Toggled({}): {}".format(len(list_selected_vertex), list_selected_vertex))
    cmds.undoInfo(closeChunk=True)


def lock_vertex_lock():
    list_selected_vertex = cmds.ls(sl=True, flatten=True, type="float3")
    cmds.undoInfo(openChunk=True)
    for selected_vertex in list_selected_vertex:
        cmds.setAttr(selected_vertex + ".px", lock=True)
        cmds.setAttr(selected_vertex + ".py", lock=True)
        cmds.setAttr(selected_vertex + ".pz", lock=True)
    print("Vertex Locked({}): {}".format(len(list_selected_vertex), list_selected_vertex))
    cmds.undoInfo(closeChunk=True)


def lock_all_vertex_lock():
    list_all_object = cmds.ls(dag=True, long=True, type="mesh")
    list_all_vertex = []
    for obj in list_all_object:
        list_all_vertex.extend(cmds.ls(obj + ".vtx[*]", flatten=True))
    cmds.undoInfo(openChunk=True)
    for vertex in list_all_vertex:
        cmds.setAttr(vertex + ".px", lock=True)
        cmds.setAttr(vertex + ".py", lock=True)
        cmds.setAttr(vertex + ".pz", lock=True)
    print("All Vertex Locked({}): {}".format(len(list_all_vertex), list_all_vertex))
    cmds.undoInfo(closeChunk=True)


def unlock_vertex_lock():
    list_selected_vertex = cmds.ls(sl=True, flatten=True, type="float3")
    cmds.undoInfo(openChunk=True)
    for selVtx in list_selected_vertex:
        cmds.setAttr(selVtx + ".px", lock=False)
        cmds.setAttr(selVtx + ".py", lock=False)
        cmds.setAttr(selVtx + ".pz", lock=False)
    print("Vertex Unlocked({}): {}".format(len(list_selected_vertex), list_selected_vertex))
    cmds.undoInfo(closeChunk=True)


def unlock_all_vertex_lock():
    list_all_object = cmds.ls(dag=True, long=True, type="mesh")
    list_all_vertex = []
    for obj in list_all_object:
        list_all_vertex.extend(cmds.ls(obj + ".vtx[*]", flatten=True))
    cmds.undoInfo(openChunk=True)
    for vertex in list_all_vertex:
        cmds.setAttr(vertex + ".px", lock=False)
        cmds.setAttr(vertex + ".py", lock=False)
        cmds.setAttr(vertex + ".pz", lock=False)
    print("All Vertex Unlocked({}): {}".format(len(list_all_vertex), list_all_vertex))
    cmds.undoInfo(closeChunk=True)

