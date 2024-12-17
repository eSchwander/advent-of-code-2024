from utils.file_reader import convert_file_to_2d_array
from collections import defaultdict


class Plot:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord
        self.neighbors = []
        self.region = None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value and self.coord == other.coord


class Garden:
    def __init__(self, filename):
        self.filename = filename
        self.array = convert_file_to_2d_array(filename)
        self.plots = []
        self.region_count = 0
        self.region_map = defaultdict(list)

        for y, row in enumerate(self.array):
            plot_row = []
            for x, val in enumerate(row):
                plot_row.append(Plot(val, (x, y)))
            self.plots.append(plot_row)

        for y, row in enumerate(self.plots):
            for x, plot in enumerate(row):

                neighbors = plot.neighbors

                if y != 0:
                    neighbors.append(self.plots[y - 1][x])
                if y != len(self.plots) - 1:
                    neighbors.append(self.plots[y + 1][x])
                if x != 0:
                    neighbors.append(self.plots[y][x - 1])
                if x != len(self.plots[y]) - 1:
                    neighbors.append(self.plots[y][x + 1])

    def determine_plot_regions(self):
        for plot_row in self.plots:
            for plot in plot_row:
                if plot.region is None:
                    self.map_region(plot)

    def map_region(self, plot):
        region_number = self.get_region_number()
        plots_in_region = [plot]
        while plots_in_region:
            current_plot = plots_in_region.pop(0)
            if current_plot.region is not None:
                continue
            if current_plot.region is None:
                current_plot.region = region_number
            for neighbor in current_plot.neighbors:
                if neighbor.region is None and neighbor.value == current_plot.value:
                    plots_in_region.append(neighbor)

            if current_plot not in self.region_map[region_number]:
                self.region_map[region_number].append(current_plot)

    def get_region_number(self):
        region_count = self.region_count
        self.region_count += 1
        return region_count

    def get_day1_answer(self):
        total = 0

        for region, plots in self.region_map.items():
            area = 0
            perimeter = 0
            for plot in plots:
                area += 1
                for neighbor in plot.neighbors:
                    if neighbor.value != plot.value:
                        perimeter += 1
                    # handle edges
                perimeter += 4 - len(plot.neighbors)
            total += area * perimeter
            print(f"region: {region} plot.value: {plots[0].value} area: {area}, perimeter: {perimeter}")

        return total

if __name__ == '__main__':
    garden = Garden('input.txt')
    garden.determine_plot_regions()
    answer = garden.get_day1_answer()
    print(answer)