import matplotlib.pyplot as plt
from chart_config import chart_config as cfg
from chart_config import chart_colors

def calculate_total_section_weight(sections):
    sections_total_weight = 0
    for section in sections:
        sections_total_weight += section["weight"]
    return sections_total_weight

def calculate_donut_count(sections):
    number_of_donuts = 0
    for section in sections:
        donuts_in_section = len(section["donuts"])
        number_of_donuts  = max(donuts_in_section, number_of_donuts)
    return number_of_donuts

def calculate_donut_section_weight(section, donut_number):
    total_weight = 0
    element_list = section["donuts"][donut_number]["elements"]
    for element in range(0, len(element_list)):
        total_weight = total_weight + element_list[element]
    return total_weight

def generate_donut_elements(sections, donut_number, sections_total_weight):
    element_sizes  = []
    element_colors = []
    element_labels = []
    donut_color   = chart_colors[donut_number]

    for section in sections:
        donuts_in_section         = len(section["donuts"])
        donut_in_section_is_empty = (donuts_in_section <= donut_number)
        section_size              = section["weight"] / sections_total_weight
        section_color             = chart_colors[sections.index(section)]

        if donut_in_section_is_empty:
            element_sizes.append(section_size)
            element_colors.append(empty_color)
        else:
            elements_in_donut_section = len(section["donuts"][donut_number]["elements"])
            element_total_weight = calculate_donut_section_weight(section, donut_number)
            for element in section["donuts"][donut_number]["elements"]:
                element_color = donut_color if cfg["color_by_ring"] else section_color
                element_size  = section_size * element / element_total_weight
                element_sizes.append(element_size)
                element_colors.append(element_color)
    return (element_sizes, element_colors)

def add_donut_to_plot(axis, donuts, donut_number, donut_radius):
    donut_radius_next =  donut_radius + 0.8 / (donut_number + 1) + 0.2
    donut_width = donut_radius_next - donut_radius
    donut_drawing, _ = axis.pie(
                        donuts["element_sizes"][donut_number],
                        radius = donut_radius, 
                        startangle = cfg["start_angle"],
                        colors = donuts["element_colors"][donut_number]
                    )
    return donut_drawing, donut_width

if __name__ == "__main__":
    fig, ax      = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    donut_radius = 0
    colors       = chart_colors
    empty_color  = (0,0,0,0)
    donuts       = dict()
    donuts["element_sizes"]  = []
    donuts["element_colors"] = []

    number_of_donuts     = calculate_donut_count(cfg["sections"])
    total_section_weight = calculate_total_section_weight(cfg["sections"])

    for donut_number in range(0, number_of_donuts):
        element_sizes, element_colors = generate_donut_elements(
                                            cfg["sections"], 
                                            donut_number, 
                                            total_section_weight
                                            )
        donuts["element_sizes" ].append(element_sizes)
        donuts["element_colors"].append(element_colors)

        donut_radius = donut_radius + 0.8 / (donut_number + 1) + 0.2
        donut_drawing, donut_width = add_donut_to_plot(ax, donuts, donut_number, donut_radius)
        plt.setp( donut_drawing, width = donut_width, edgecolor = 'white')

    ax.set_xlim(-donut_radius * 1.05, donut_radius * 1.05)
    ax.set_ylim(-donut_radius * 1.05, donut_radius * 1.05)
    plt.tight_layout()
    plt.show()
