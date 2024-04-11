import info

class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["master"]:
            self.svnTargets[ver] = f"[git]https://github.com/cryollyne/craft-blueprints-cryollyne.git|{ver}|"
        self.defaultTarget = "master"
    def setDependencies(self):
        self.buildDependencies["craft/craft-core"] = "default"

from Package.BlueprintRepositoryPackageBase import *
class Package(BlueprintRepositoryPackageBase):
    def __init__(self):
        BlueprintRepositoryPackageBase.__init__(self)
