import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class FutureWarningIgnore:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"": ("", ),}
                }

    RETURN_TYPES = ()
    FUNCTION = "ignore"

    OUTPUT_NODE = True

    CATEGORY = ""

    def ignore(self):
        pass

NODE_CLASS_MAPPINGS = {
    "FutureWarningIgnore": FutureWarningIgnore,
}
