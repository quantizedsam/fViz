#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""Class to handle a dynamic axis."""

__name__    = 'fViz.ui.axes.DynamicAxis'
__authors__ = ['Sampreet Kalita']
__created__ = '2020-10-23'
__updated__ = '2020-10-23'

# dependencies
import logging
import numpy as np

# dev dependencies
from fViz.ui.axes.BaseAxis import BaseAxis

# module logger
logger = logging.getLogger(__name__)

class DynamicAxis(BaseAxis):
    """Class to handle a dynamic axis.

    Inherits :class:`fViz.ui.axes.BaseAxis`.
    """

    def __init__(self, axis_data={}):
        """Class constructor for DynamicAxis.

        Parameters
        ----------
            axis_data : int or list or dict
                Data for the axis.
        """

        # initialize super class
        super().__init__(axis_data)

        # set var 
        self.var = axis_data.get('var', 'dynamic_axis')

        # set name
        self.name = axis_data.get('name', '')

        # set unit
        self.unit = axis_data.get('unit', '')

        # set label
        self.label = self.name + ' (' + self.unit + ')' if self.unit != '' else self.name