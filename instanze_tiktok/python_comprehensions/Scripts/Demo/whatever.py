from instanim.scene import *




list_ = [1, 2, 3, 4, 5]

tuple_ = (1, 2, 3, 4, 5)

dict_ = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}





# list example
list_ = []
for i in range(10):
    list_.append(i)


# comprehensions
list_ = [i for i in range(10)]



# tuple example
tuple = ()
for i in range(10):
    tuple_ = (*tuple_, i)


# tuple_ revisited
tuple_ = (i for i in range(10))



# dict example
dict_ = {}
for i in range(10):
    dict_[str(i)] = i



# dict_ revisited
dict_ = {str(i): i for i in range(10)}






list_ = []
for i in range(10):
    x = np.linspace(0, i, 10)
    y = np.sin(x)
    v = np.vstack((x, y)).T

    list_.append(v)


list_ = [??? for i in range(10)]







dict_ = {str(i):i for i in range(10)}


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




list_ = []
for i in range(10):
    list_.append(2*i if i<5 else 3*i)


list_ = [2*i if i<5 else 3*i for i in range(10)]







tuple_ = ()
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


tuple_ = (i*j*k*l for i in range(10) for j in range(10) for k in range(10) for l in range(10))
