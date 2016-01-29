import subprocess
import time
import numpy as np
from config import *

def run_SBT(seq, rp, bSaveImage):
    x = seq.init_rect[0] - 1
    y = seq.init_rect[1] - 1
    w = seq.init_rect[2]
    h = seq.init_rect[3]

    path = './results/'

    if not os.path.exists(path):
        os.makedirs(path)

    command = map(str,['SemiBoostingTracker_d.exe', '100', '0.99', '2', 
        '0', '0', '0', seq.name, seq.path, seq.startFrame, seq.endFrame, 
        seq.nz, seq.ext, x, y, w, h])

    tic = time.clock()
    subprocess.call(command)
    duration = time.clock() - tic

    result = dict()
    res = np.loadtxt(path + '{0}_SBT.txt'.format(seq.name), dtype=int)
    result['res'] = res
    result['type'] = 'rect'
    result['fps'] = round(seq.len / duration, 3)

    return result