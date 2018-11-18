from PersistentData.BuildLoad import BuildLoad
from PersistentData.NewPreset import NewPreset
from PersistentData.LoadPreset import LoadPreset

class Begin:

    def __init__(self):

        choice = BuildLoad()
        choice.setBuildLoad()
        if (choice.getBuildLoad() == 1):
            NewPreset()
        elif (choice.getBuildLoad() == 2):
            LoadPreset()
