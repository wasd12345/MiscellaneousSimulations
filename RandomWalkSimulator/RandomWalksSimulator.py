# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:05:29 2018

@author: GK
"""




#Random Walk simulator

# What I want you to do:
# 1. finish the methods below
# 2. make some graphs / histograms etc. to visualize reults
# 3. add tracking for other things you think would be interesting to look at.
# 4. confirm time to 0 return follows arcsine distribution (beta ) when:
#the probability for the time of the last visit to the origin in a random walk is distributed as the arcsine distribution Beta(1/2, 1/2)

# feel free to add anything else you want.



import numpy as np
import matplotlib.pyplot as plt

import scipy.stats




class RandomWalks():
    
    def __init__(self):
        self.random_seed = 123
        np.random.seed(self.random_seed)
        
        #example dict of {stepsize:probability}
        self.steps_probabilities = {-2:.25, -1:.20, 0:.05, +1:.25, +2:.25}#
        self.walk_max_length = 1e4
        self.N_walks = None
        #other thigns to track...
        
        
    def SingleRandomWalk(self):
        """
        Single simulation of one random walk
        """
        #simulate the walk w random draws: from categorical distribution:
        x = np.random.choice(self.steps_probabilities.keys(),
                             p=self.steps_probabilities.values(),
                             size=self.walk_max_length)
        pass        
        
        
    def Get_Returns_to_zero(self,random_walk):
        """
        Get the timesteps at which walk returned to 0.
        (includes 1st timestep 0)
        """
        np.where(asdasd ==0)
        return zero_inds
    
    
    def Get_Time_btwn_zeros(self,zero_inds):
        """
        Get the distribution of times between 0 returns
        """
        np.bincount(np.diff(zero_inds,n=1))
        
        
    def Get_1_walk_summary_stats(self,random_walk):
        """
        Get summary statistics of this random walk
        """
        #mean, median, SD, min, max
        pass
    
    
    

    
    
    
    
    def ManyRandomWalks(selfm,N_walks):
        """
        Perform N random walk simulations
        """
        self.N_walks = N_walks
        for N in xrange(self.N_walks):
            self.SingleRandomWalk(...)
            self.Get_1_walk_summary_stats(...)
            self.Get_Returns_to_zero(random_walk)
            self.Get_Time_btwn_zeros(...)
            self.Visualize_results()
    
    
    def Visualize_results(self):
        """
        Some graphs of time series, histograms of distributions, etc.
        """
        x = 
        y =
        plt.figure()
        plt.bars(x,y,align='center')
        plt.show()
        pass
    
    def SaveResults(self):
        """
        save out csv of results and summary statistcis
        """
        pass
    
    
    
    
if __name__ == '__main__':
    
    N_walks = 1e6
    RW = RandomWalks()
    RW.ManyRandomWalks(N_walks)