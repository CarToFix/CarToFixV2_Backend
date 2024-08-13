""" This module contains the class WhorkshopHolderMixin that contains the attribute
    workshop which all other classes must contain

Created by:
    Emanuel Trias
"""

from models.common import Common


class WhorkshopHolderMixin(Common):
    """ Defines a Holder Mixin """

    version = "1.0.0"

    def __init__(self, workshop):
        """ Initialises a WorkshopHolderMixin
            - workshop: Workshop assosiated with the instance
        """
        self.workshop = workshop

        super().__init__()
