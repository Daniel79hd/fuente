#!/usr/bin/env python3
"""
Example usage of the Fuente class.
"""

from fuente import Fuente


def main():
    """
    Demonstrate the usage of Fuente.
    """
    print("=== Fuente Example ===\n")
    
    # Create a new fuente
    my_source = Fuente("Lenik Source")
    print(f"1. Created: {my_source}\n")
    
    # Add some data
    print("2. Adding data...")
    my_source.add("First item")
    my_source.add("Second item")
    my_source.add("Third item")
    print(f"   {my_source}\n")
    
    # Get all data
    print("3. Getting all data:")
    for item in my_source.get_all():
        print(f"   - {item}")
    print()
    
    # Get last item
    print(f"4. Last item: {my_source.get_last()}\n")
    
    # Check size
    print(f"5. Size: {my_source.size()}\n")
    
    # Clear the source
    print("6. Clearing the source...")
    my_source.clear()
    print(f"   {my_source}\n")


if __name__ == "__main__":
    main()
