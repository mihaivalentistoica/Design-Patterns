class PachetTransport:
    def __init__(self, hasWiFi, hasAnimale, isFumator, hasAC, hasTV):
        self.hasWifi = hasWiFi
        self.hasAnimale = hasAnimale
        self.isFumator = isFumator
        self.hasAC = hasAC
        self.hasTV = hasTV


class PachetTransportBuilder:
    def __init__(self):
        self.pachet_transport = PachetTransport(False, False, False, False, False)

    def set_hasWifi(self):
        self.pachet_transport.hasTV = True
        return self

    def set_hasAnimale(self):
        self.pachet_transport.hasAnimale = True
        return self

    def set_isFumator(self):
        self.pachet_transport.isFumator = True
        return self

    def build(self):
        return self.pachet_transport


builder = PachetTransportBuilder()
pachet = builder.set_hasAnimale().set_hasWifi().build()
print(pachet.isFumator)
