from math import sqrt, tanh, cosh, pi
import warnings, getopt, sys

def wn_shallow(h, w):
    '''
    wn_shallow() returns shallow water approximation of wave number

    h: water depth
    w: angular frequency
    '''
    return w / sqrt(9.81 * h)

def wn(k, h, w, error):
    '''
    wn() recursively calculates and returns wave number 
    using Newton-Rhapsom method

    parameters
    k       (float): init wavenumber guess
    h       (float): water depth
    w       (float): angular frequency
    error   (float): margin of between guesses
    '''
    warnings.filterwarnings("ignore")       # cosh may reach some diverging condition, this is ok
    th = tanh(k * h)                     # encaps tanh operations
    sh = 1 / cosh(k * h)                 # encaps sech operations
    num = (9.81 * k * th - w ** 2)          # numerator
    den = (9.81) * (th + k * h * sh ** 2)   # denominator 
    k_next = k - num / den
    
    if abs(k_next - k) <= error:    # base case:
        return k
    else:                           # recursive case:
        return wn(k_next, h, w, error)

def main(argv):
    h = -1      # water depth
    w = -1      # angular frequency
    T = -1      # period
    e = 0.00001  # error
    try: 
        opts, _ = getopt.getopt(argv, 'h:w:T:e:')
    except getopt.GetoptError:
        print('Error: usage wavenumber.py -h -w/-t')
        sys.exit(2)
    for opt, arg in opts:
        if opt in '-h':
            h = float(arg)
        elif opt in '-w':
            w = float(arg)
        elif opt in '-T':
            T = float(arg)
        elif opt in '-e':
            e = float(arg)
    if h == -1:
        print('Error: no -h argument')
        sys.exit()
    if not w == -1 and not T == -1:
        print('Error: read both -w, -T')
        sys.exit()
    elif w == -1 and T == -1:
        print('Error: no -w or -T argument')
        sys.exit()
    
    print('---')
    print('PARAMETERS')
    print('water depth: {:f}'.format(h))
    if w == -1:
        print('period: {:f}'.format(T))
        w = 2 * pi / T
    print('angular frequency: {:f}'.format(w))
    print('error: {:f}'.format(e))
    print('---')
    print('OUTPUT')
    k_i = wn_shallow(h, w)
    print('initial guess (shallow water approximation): {:f}'.format(k_i))
    k = wn(k_i, h, w, e)
    print('final guess (recursive Newton-Raphson method): {:f}'.format(k))
    L = 1 / k
    print('wavelength: {:f}'.format(L))
    print('depth to wavelength ratio: {:f}'.format(h / L))
    print('---')

if __name__ == '__main__':
    main(sys.argv[1:])
