import numpy as np



'''

P1: Iterables, and creating them in the generic way?

'''

# such as... list, tuples, dictionaries
list_ = [1, 2, 3, 4, 5]
tuple_ = (1, 2, 3, 4, 5)
dict_ = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}



# list example
list_ = []
for i in range(10):
    list_.append(i)


# tuple example
tuple = ()
for i in range(10):
    tuple_ = (*tuple_, i)


# dict example
dict_ = {}
for i in range(10):
    dict_[str(i)] = i




'''

P2: Instead, comprehensions? And how to create them?

'''



# list_ revisited
list_ = [i for i in range(10)]


# tuple_ revisited
tuple_ = (i for i in range(10))


# dict_ revisited
dict_ = {str(i): i for i in range(10)}




'''

P3: Two caveats: single-line items only & structure has to match

'''

# i.e. won't work for this...
list_ = []
for i in range(10):
    x = np.linspace(0, i, 10)
    y = np.sin(x)
    v = np.vstack((x, y)).T # array of coordinate (Nx2)
    
    list_.append(v)
    
# cuz how??
list_ = ['insert lines ???' for i in range(10)]



# take lists
list_ = [i for i in range(10)]


# take dictionaries
dict_ = {str(i): i for i in range(10)}
dict_ = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8
}




'''

P4: items can expand to any one-line (i.e. if/else)

'''

list_ = []
for i in range(10):
    list_.append(np.vstack(np.sin(np.linspace(0, i, 10), np.linspace(0, i, 10))).T)


list_ = []
for i in range(10):
    list_.append(2*i if i<5 else 3*i)


# in front
list_ = [2*i if i<5 else 3*i for i in range(10)]




'''

P5: comprehensions can expand to nested loops

'''


# 2-level nested
tuple_=()
for i in range(10):
    for j in range(10):
        tuple_ = (*tuple_, i*j)

tuple_ = (
    i*j
    for i in range(10)
    for j in range(10)
)



# 3-level nested
tuple_=()
for i in range(10):
    for j in range(10):
        for k in range(10):
            tuple_ = (*tuple_, i*j*k)

tuple_ = (
    i*j*k
    for i in range(10)
    for j in range(10)
    for k in range(10)
)


# 4-level nested
tuple_=()
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                tuple_ = (*tuple_, i*j*k*l)

tuple_ = (
    i*j*k*l
    for i in range(10)
    for j in range(10)
    for k in range(10)
    for l in range(10)
)





