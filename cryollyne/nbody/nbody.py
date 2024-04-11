import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Gravity Simulator"
        self.description = "A simple program that simulates gravity"
        for ver in ["master"]:
            self.svnTargets[ver] = f"[git]https://github.com/cryollyne/nbody.git|{ver}|"
        self.defaultTarget = "master"
    def setDependencies(self):
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["kde/plasma/breeze"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = "default"

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        CMakePackageBase.buildTests = False
    def createPackage(self):
        return super().createPackage()
