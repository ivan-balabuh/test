class Figure:
    def __init__(self, figure_type: str):
        self.figure_type = figure_type.lower()

    @property
    def get_angles(self):
        if self.figure_type == "triangle":
            return 3
        elif self.figure_type == "square":
            return 4
        elif self.figure_type == "rectangle":
            return 4
        else:
            return None


def main():  # pragma: no cover
    fig = Figure("triangle")
    print(f"Angles: {fig.get_angles}")


if __name__ == "__main__":  # pragma: no cover
    main()
