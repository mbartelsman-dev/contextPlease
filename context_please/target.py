class Target:
    value: str

    def __init__(self, value: str):
        """
        :param value: Registry sub-key as a string
        :type value: str
        :rtype: Target
        """
        self.value = value

    def to_path(self):
        return "HKEY_CLASSES_ROOT\\" + self.value


class Background(Target):
    def __init__(self):
        super(Background, self).__init__(r"Directory\Background")


class Directory(Target):
    def __init__(self):
        super(Directory, self).__init__(r"Directory")


class Everything(Target):
    def __init__(self):
        super(Everything, self).__init__(r"*")


class CustomTarget(Target):
    def __init__(self, target: str):
        if target is None:
            raise ValueError("A target has not been specified")

        super(CustomTarget, self).__init__(target)
