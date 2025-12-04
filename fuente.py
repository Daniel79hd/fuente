"""
Fuente - A simple source/fountain implementation
"""


class Fuente:
    """
    A source/fountain class that can generate and provide data.
    """
    
    def __init__(self, name="Fuente"):
        """
        Initialize a new Fuente instance.
        
        Args:
            name (str): The name of this source/fountain
        """
        self.name = name
        self._data = []
    
    def add(self, item):
        """
        Add an item to the source.
        
        Args:
            item: The item to add to the source
        """
        self._data.append(item)
    
    def get_all(self):
        """
        Get all items from the source.
        
        Returns:
            list: All items in the source
        """
        return self._data.copy()
    
    def get_last(self):
        """
        Get the last item from the source.
        
        Returns:
            The last item, or None if the source is empty
        """
        return self._data[-1] if self._data else None
    
    def clear(self):
        """
        Clear all items from the source.
        """
        self._data.clear()
    
    def size(self):
        """
        Get the number of items in the source.
        
        Returns:
            int: The number of items
        """
        return len(self._data)
    
    def __str__(self):
        """
        String representation of the Fuente.
        
        Returns:
            str: A string representation
        """
        return f"Fuente(name='{self.name}', size={self.size()})"
    
    def __repr__(self):
        """
        Detailed representation of the Fuente.
        
        Returns:
            str: A detailed string representation
        """
        return f"Fuente(name='{self.name}', data={self._data})"


if __name__ == "__main__":
    # Simple demonstration
    fuente = Fuente("Mi Fuente")
    print(f"Created: {fuente}")
    
    fuente.add("Hola")
    fuente.add("Mundo")
    print(f"After adding items: {fuente}")
    print(f"All items: {fuente.get_all()}")
    print(f"Last item: {fuente.get_last()}")
