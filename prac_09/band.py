class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a new musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make all the musicians play music."""
        return "\n".join(musician.play() for musician in self.musicians)
