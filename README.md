# Nested Piechart Generator

Generates nested (multi-ring) donut charts using matplotlib. Each ring can contain multiple sections with configurable weights and element distributions.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Usage

```bash
# Install dependencies and run
make

# Or step by step:
make sync   # install/sync dependencies
make run    # generate and display the chart
```

## Configuration

Edit `chart_config.py` to customize:

- **chart_colors** – color palette for rings/sections
- **chart_config** – sections, weights, donut element distribution, start angle, and coloring mode
