import ConfigParser

class RangeConfig:
    config = ConfigParser.ConfigParser()
    filename = "./config.ini"
    section = "ColorRange"
    lowRange = [0, 0, 0]
    highRange = [0, 0, 0]

    def __init__(self, filename):
        self.filename = filename
        settings = self.config.read(filename)

        if len(settings) == 0:
            self.set_low_range(0,0,0)
            self.set_high_range(0,0,0)
        else:
            #load low range
            self.lowRange[0] = self.config.getint(self.section, "h1")
            self.lowRange[1] = self.config.getint(self.section, "s1")
            self.lowRange[2] = self.config.getint(self.section, "v1")
            #load high range
            self.highRange[0] = self.config.getint(self.section, "h2")
            self.highRange[1] = self.config.getint(self.section, "s2")
            self.highRange[2] = self.config.getint(self.section, "v2")



    def set_low_range(self, h, s, v):
        if self.config.has_section(self.section) == False:
            self.config.add_section(self.section)
        self.lowRange[0] = h
        self.lowRange[1] = s
        self.lowRange[2] = v
        self.config.set(self.section, "h1", h)
        self.config.set(self.section, "s1", s)
        self.config.set(self.section, "v1", v)
        cfg_file = open(self.filename, "w")
        self.config.write(cfg_file)
        cfg_file.close()

    def set_high_range(self, h, s, v):
        if self.config.has_section(self.section) == False:
            self.config.add_section(self.section)
        self.highRange[0] = h
        self.highRange[1] = s
        self.highRange[2] = v
        self.config.set(self.section, "h2", h)
        self.config.set(self.section, "s2", s)
        self.config.set(self.section, "v2", v)
        cfg_file = open(self.filename, "w")
        self.config.write(cfg_file)
        cfg_file.close()

    def print_ranges(self):
        print self.lowRange
        print self.highRange