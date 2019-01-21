from django.db import models
import datetime
# Create your models here.


class Item(models.Model):
    WORKING = 'WK'
    OUT_OF_ORDER = 'OO'
    IN_MAINTENANCE = 'IM'
    STATUS_CHOICES = (
        (WORKING, 'Working'),
        (OUT_OF_ORDER, 'Out of Order'),
        (IN_MAINTENANCE, 'In Maintenance')
    )
    name = models.CharField(max_length=50, default='Generic', help_text='Enter the brand name of the item')
    model = models.CharField(max_length=50, default='Generic', help_text='Enter the model of the item')
    cost = models.DecimalField(decimal_places=2, max_digits=10, null=True, help_text='Enter the cost of the item')
    room = models.ForeignKey('Room', null=True, on_delete=models.SET_NULL, help_text='Select room where it is kept')
    date_of_acquire = models.DateField(default=datetime.date.today, help_text='Enter the date of acquire')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=WORKING)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}-{}".format(self.name, self.model)


class Floor(models.Model):

    floor = models.PositiveSmallIntegerField(help_text='Enter the floor',primary_key=True)
    def __str__(self):
        return str(self.floor)


class Room(models.Model):
    room_no = models.PositiveSmallIntegerField(primary_key=True, help_text='Enter the room number')
    floor = models.ForeignKey('Floor',help_text='In which floor is this room?',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.room_no)



class Computer(Item):
    pass


class Laptop(Item):
    pass


class NetworkSwitch(Item):
    no_of_ports = models.PositiveSmallIntegerField(help_text='Enter the number of ports')
    no_of_SFP_ports = models.PositiveSmallIntegerField(help_text='Enter the number of SFP ports')

    class Meta:
        verbose_name_plural = 'Network Switches'


class Printer(Item):
    ip_address = models.GenericIPAddressField(help_text='Enter the ip address for this printer')


class AdditionalItem(Item):
    pass
