'''
This script compares three different recommendation algorithms for generation
of missing/expected movie ratings and displays the results to the user.

Author: Kushal Agrawal
Date of Completion: 30/09/2017

The dataset containing the movie ratings was obtained from www.movielens.org
and the following paper is responsible for its creation:

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History
and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4,
Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872
'''

import numpy
import scipy.sparse
import tkinter as tk


class RecommenderSystems(tk.Frame):
    '''
    This is the master application defining class and encapsulates
    everything from the GUI widgets to the core search implementation.
    '''

    def __init__(self, master=None):
        ''' Constructor for the RecommenderSystem class. '''
        tk.Frame.__init__(self, master)
        self.entry = tk.StringVar()
        self.msg = tk.StringVar()
        self.grid()
        self.configureGrid()
        self.createWidgets()
        self.setMessage('Loading, please wait...')

    def configureGrid(self):
        ''' Configure the Tkinter grid layout. '''
        self.rowconfigure(0, minsize=50)
        self.columnconfigure(0, minsize=80)
        self.rowconfigure(1, minsize=50)
        self.columnconfigure(1, minsize=80)
        self.rowconfigure(2, minsize=50)
        self.columnconfigure(2, minsize=80)
        self.rowconfigure(3, minsize=50)
        self.columnconfigure(3, minsize=80)
        self.rowconfigure(4, minsize=50)
        self.columnconfigure(4, minsize=80)
        self.rowconfigure(5, minsize=50)
        self.columnconfigure(5, minsize=80)
        self.rowconfigure(6, minsize=50)
        self.columnconfigure(6, minsize=80)
        self.rowconfigure(7, minsize=50)
        self.columnconfigure(7, minsize=80)
        self.rowconfigure(8, minsize=50)

    def createWidgets(self):
        ''' Define the attributes of the GUI elements. '''

        # The Quit Button
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=8, column=7, rowspan=1, columnspan=1, padx=15, pady=25,
                             sticky=tk.N + tk.E + tk.S + tk.W)

        # The Message Box to display the output
        self.messageBox = tk.Message(self, anchor=tk.NW, padx=25, pady=25, width=500, justify=tk.LEFT, relief=tk.RIDGE,
                                     bd=3, textvariable=self.msg)
        self.messageBox.grid(row=0, column=0, rowspan=8, columnspan=8, padx=20, pady=25,
                             sticky=tk.N + tk.E + tk.S + tk.W)

    def setMessage(self, message):
        ''' Set messageBox to display "message". '''
        self.msg.set(message)


    #############################################
    ########### Data Loading Function ###########
    #############################################

    def loadData(self):
        ''' Load the ratings data. '''

        # File with the ratings data
        self.ratings_file = open('./ratings/ratings.dat', 'r')

        # Dictionary of keys format sparse matrix
        self.ratings_matrix = scipy.sparse.dok_matrix((4000, 6100))

        for rating in self.ratings_file:
            data = rating.strip().split('::')
            self.ratings_matrix[int(data[1]) - 1, int(data[0]) - 1] = float(data[2])

        self.ratings_file.close()

        self.ratings_matrix = self.ratings_matrix.asformat('coo').asformat('csr')

        self.setMessage('Loading Complete.')

    #############################################





###############################################################################

root = tk.Tk()
app = RecommenderSystems(root)
app.master.title('Recommender Systems Comparison')
app.after(500, app.loadData)
app.mainloop()
