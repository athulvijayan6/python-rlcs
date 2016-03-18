# A python implementation of Rough Longest Common Subsequence.
This a python-implementation of works.
1. Shrey Dutta, Krishnaraj Sekhar PV, Hema A. Murthy:   Raga Verification in Carnatic Music Using Longest Common Segment Set. ISMIR 2015: 605-611
2. S. Dutta and H. A. Murthy, "A modified rough longest common subsequence algorithm for   motif spotting in an Alapana of Carnatic Music," Communications (NCC), 2014 Twentieth   National Conference on, Kanpur, 2014, pp. 1-6.

### Install dependencies.

`sudo apt-get install python-numpy python-scipy python-matplotlib`

### Perform dynamic programming algorithm
#####def rlcs(X, Y, tau_dist=0.005, delta=0.5):
    '''Performs the dynamic programming for RLCS. And finally returns score matrices for further analysis.
    parameters:
        X - Query signal; Either a 1D numpy array or 2D array with columns as feature dim and rows as number of samples.
        Y - Reference signal; Either a 1D numpy array or 2D array with columns as feature dim and rows as number of samples
        tau_dist - with normalized distance below tau_dist, samples are considered similar.
        delta - penalty for gap.'''

### Bactrack to find common segments
#####def backtrack(X, Y, score, diag, cost):
    '''Backtracks through the score matrix produced to find the matching signals.
    Returns a variable segment which is a p x 3 matrix.
        p is the length of subsequence set.
        First column denotes index in query
        Second column denotes index in reference
        Third column denotes corresponding score
    Cut at zeros in scores column to find exact set of subsequences'''



### Plot the similarity between signals as heatmap
#####def plotLCS(segment, X, Y, ax):
    '''Plots the common subsequence with the score.
    From one sample to another, The following inferences can be drawn.
    1. Diagonal movement - next sample is a match - score increases.
    2. Right - A gap is fount, next sample of query is matched with current sample of reference. - score decreases due to penalty.
    3. Up = A gap is fount, current sample of query is matched with next sample of reference. - score decreases due to penalty.
    matplotlib axis and fig is returned.'''

Author: Athul Vijayan - Reach me at athulvijayan6@gmail.com