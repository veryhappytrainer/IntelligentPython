class EuropeanPlug:
 def plug_in(self):
     return "220V"
class USPlug:
 def connect(self):
    return "110V"
class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def plug_in(self):
        return self.plug.connect()


if __name__ == "__main__":
    european_plug = EuropeanPlug()
    us_plug = USPlug()

    # Using the adapter to connect a US plug to a European socket
    adapter = Adapter(us_plug)
    print(f"European Plug Output: {european_plug.plug_in()}")
    print(f"US Plug through Adapter Output: {adapter.plug_in()}")