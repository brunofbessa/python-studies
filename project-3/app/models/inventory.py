"""Inventory models"""

from app.utils.validators import validate_integer

class Resource:
    """Base class for resources."""

    def __init__(self, name, manufacturer, total, allocated):
        """
        Args:
            name (str): display name of resource
            manufacturer (str) resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources

        Note:
            `allocated` cannot exceed `total`
        """
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer('allocated', allocated, 0, total, 
                         custom_max_message='Allocated inventory cannot exceed total inventory.')
        self._allocated = allocated

    @property
    def name(self):
        """
        Returns:
            str: the resource name
        """
        return self._name
    
    @property
    def manufacturer(self):
        """
        Returns:
            str: the resource manufacturer
        """
        return self._manufacturer
    
    @property
    def total(self):
        """
        Returns:
            int: number of resources in stock
        """
        return self._total
        
    @property
    def allocated(self):
        """
        Returns:
            int: number of resources in use
        """
        return self._allocated
    
    @property
    def category(self):
        """
        Returns:
            str: the resource category
        """
        return type(self).__name__.lower()
    
    @property
    def available(self):
        """
        Returns:
            int: number of resources available for use
        """
        return self.total - self.allocated
        
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return (f'{self.name} ({self.category} - {self.manufacturer}): total={self.total}, allocated={self.allocated}')
    
    def claim(self, num):
        """
        Claim num inventory items (if available)

        Args:
            num (int): Number of inventory itemsn to be claimed

        Returns:
        """

        validate_integer('num', num, 1, self.available, custom_max_message='Cannot claim more than available')
        self._allocated += num

    def freeup(self, num):
        """
        Return an inventory item to be available

        Args:
            num (int): Number of items to return (cannot exceed number in use)

        Returns:

        """
        validate_integer('num', num, 1, self._allocated, custom_max_message='Cannot return more than allocated')
        self._allocated -= num

    def died(self, num):
        """
        Number of items to deallocate and remove from the inventory pool altogether

        Args:
            num (int): Number of items that have died

        Returns:

        """
        validate_integer('num', num, 1, self.allocated, custom_max_message='Cannot retire more than allocated')
        self._allocated -= num
        self._total -= num

    def purchase(self, num):
        """
        Add a new inventory to the pool

        Args:
            num (int): Number of items to be added to the pool

        Returns:

        """
        validate_integer('num', num, 1)
        self._total += num

class CPU(Resource):
    """
    Resource subclass used to track specific CPU inventory pools
    """

    def __init__(self, name, manufacturer, total, allocated, 
                 cores, socket, power_watts):
        """
        Args:
            name (str): display name of resource
            manufacturer (str) resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            cores (int): number of cores
            socket (str): socket type
            powet_watts(int): CPU
        """

        super().__init__(name, manufacturer, total, allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        """
        Returns:
            int: the number of cores
        """
        return self._cores          

    @property
    def socket(self):
        """
        Returns:
            str: the socket type of this CPU
        """
        return self._socket
    
    @property
    def power_watts(self):
        """
        Returns:
            int: the rated wattage of thir CPU
        """
        return self._power_watts
    
    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'
        

class Storage(Resource):
    """
    Base class for storage devices
    """

    def __init__(self, name, manufacturer, total, allocated, 
                 capacity_gb):
        """
        Args:
            name (str): display name of resource
            manufacturer (str) resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity in GB
        """

        super().__init__(name, manufacturer, total, allocated)

        validate_integer('capacity_gb', capacity_gb, 1)

        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Returns:
            int: storage capacity in GB
        """
        return self._capacity_gb          
    
    def __repr__(self):
        return f'{self.category}: {self.name} ({self.capacity_gb} GB)'
    
class HDD(Storage):
    """
    Class for HDD storage devices
    """

    def __init__(self, name, manufacturer, total, allocated, 
                 capacity_gb, size, rpm):
        """
        Args:
            name (str): display name of resource
            manufacturer (str) resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity in GB
            size (str): indicates the device size
            rpm (int): disk rotation speed in rpm
        """

        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        alowed_hdd_sizes = ['2.5"', '3.5"']
        if size not in alowed_hdd_sizes:
            raise ValueError(f'Invalid HDD Size. Must be one of {", ".join(alowed_hdd_sizes)}')
 
        validate_integer('rpm', rpm, min_value=1_000, max_value=50_000)

        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        Returns:
            str: indicates the device size
        """
        return self._size

    @property
    def rpm(self):
        """
        Returns:
            int: disk rotation speed in rpm
        """
        return self._rpm
    
    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'
    
class SDD(Storage):
    """
    Class for SDD storage devices
    """

    def __init__(self, name, manufacturer, total, allocated, 
                 capacity_gb, interface):
        """
        Args:
            name (str): display name of resource
            manufacturer (str) resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity in GB
            interface (str): indicates the device interface
        """

        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        self._interface = interface

    @property
    def interface(self):
        """
        Returns:
            str: indicates the device interface
        """
        return self._interface
    
    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'