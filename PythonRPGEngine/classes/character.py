class Character:

    def __init__(self, **kwargs):

        if "load_from_id" in kwargs and kwargs["load_from_id"]:
            self.load_from_id( **kwargs )
        else:
            self.load_from_kwargs( **kwargs )

    def load_from_id(self, id, level):
        pass

    def load_from_kwargs(self, **kwargs):
        # At this point, assume kwargs contains all of what's needed
        # Crashes indicate incomplete info
        
        self.level = kwargs["level"]
        
