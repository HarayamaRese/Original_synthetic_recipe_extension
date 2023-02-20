# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModebcnfRlX", version="0.0.1")
class Script_NeteaseModebcnfRlX(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModebcnfRlXServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModebcnfRlXServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModebcnfRlXClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModebcnfRlXClientDestroy(self):
        pass
