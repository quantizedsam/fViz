#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""Class to plot figures."""

__name__    = 'fViz.ui.Figure'
__authors__ = ['Sampreet Kalita']
__created__ = '2020-10-23'
__updated__ = '2020-10-23'

# dependencies
import logging

# dev dependencies
from fViz.ui.plotters import *

# module logger
logger = logging.getLogger(__name__)

# TODO: Rename to Figure.

class Figure():
    """Class to plot figures.
    
    Properties
    ----------
        plotter : :class:`fViz.ui.plotters.*`
            Plotter class. 
    """

    @property
    def plotter(self):
        """Property plotter.

        Returns
        -------
            plotter : :class:`fViz.ui.plotters.*`
                Plotter class.
        """

        return self.__plotter
    
    @plotter.setter
    def plotter(self, plotter):
        """Setter for plotter.

        Parameters
        ----------
            plotter : :class:`fViz.ui.plotters.*`
                Plotter class.
        """

        self.__plotter = plotter

    def __init__(self, plot_params, X, Y=None, Z=None):
        """Class constructor for Figure.
        
        Parameters
        ----------
            plot_params : dict
                Parameters of the plot.

            X : list or dict or :class:`fViz.ui.axes.*`
                X-axis data.

            Y : list or dict or :class:`fViz.ui.axes.*`, optional
                Y-axis data.

            Z : list or dict or :class:`fViz.ui.axes.*`, optional
                Z-axis data.
        """
        
        # initialize plot
        Axes = {
            'X': X,
            'Y': Y,
            'Z': Z
        }
        
        # matplotlib plotter
        self.plotter = MPLPlotter(plot_params, Axes) 

        # display initialization
        logger.info('----------------------------Figure Initialized-------------------\t\n')

    def update(self, xs=None, ys=None, zs=None, head=False, hold=True):
        """Function to update plot.
        
        Parameters
        ----------
            xs : list or numpy.ndarray, optional
                X-axis data.
                
            ys : list or numpy.ndarray, optional
                Y-axis data.
                
            zs : list or numpy.ndarray, optional
                Z-axis data.

            head : boolean, optional
                Option to display the head for line-type plots. Default is False.

            hold : boolean, optional
                Option to hold the plot. Default is True.
        """

        # update plot
        self.__plotter.update(xs, ys, zs, head)
            
        # update log
        logger.info('------------------------------Figure Updated---------------------\t\n')

        # show plot
        self.__plotter.show(hold)