# Fuente

A simple and elegant source/fountain implementation in Python.

## Description

**Fuente** (Spanish for "source" or "fountain") is a lightweight Python class that provides a clean interface for managing and accessing data sources. It can be used as a data container, queue, or simple data store.

## Features

- Add items to the source
- Retrieve all items or the last item
- Clear the source
- Check the size of the source
- Simple and intuitive API

## Installation

No installation required. Simply copy `fuente.py` to your project.

## Usage

```python
from fuente import Fuente

# Create a new source
my_source = Fuente("My Source")

# Add items
my_source.add("Hello")
my_source.add("World")

# Get all items
items = my_source.get_all()  # Returns: ["Hello", "World"]

# Get the last item
last = my_source.get_last()  # Returns: "World"

# Check size
size = my_source.size()  # Returns: 2

# Clear the source
my_source.clear()
```

## Example

Run the included example:

```bash
python example.py
```

Or run the module directly:

```bash
python fuente.py
```

## Author

lenik

## License

Open source - feel free to use and modify.
