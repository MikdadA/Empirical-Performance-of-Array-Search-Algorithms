One of the most basic programming problems is "search", that is finding an item ("key") in a structure. The structure may be linear (array) or hierarchical (tree), ordered (e.g. alphabetical or numerical order) or unordered (no particular order). There are several search algorithms available; in this assignment, we consider a sorted list of random data and compare several algorithmic approaches to finding a key in it. 

Our goals in this project include understanding and coding the search algorithms themselves, developing a methodology and infrastructure for comparing any set of related algorithms, and visualizing how the theoretical time complexities manifest in practice. 


[1] Define a function random_list(size) that  returns a sorted list of random numbers.

[2] Define a function native_search(list, key) that wraps the built-in index function

[3] Define the following functions utilizing the code from the references provided. Ensure that signatures are consistent.:
linear_search(arr, key) - see https://www.geeksforgeeks.org/linear-search/
binary_search_recursive(arr, key) - see https://www.geeksforgeeks.org/binary-search/ 
binary_search_iterative(arr, key) - see  https://www.geeksforgeeks.org/the-ubiquitous-binary-search-set-1/ 
binary_search_better(arr, key) - see  https://www.geeksforgeeks.org/the-ubiquitous-binary-search-set-1/  (down) 
binary_search_randomized(arr, key) - see  https://www.geeksforgeeks.org/randomized-binary-search-algorithm/ 
ternary_search_iterative(arr, key) - https://www.geeksforgeeks.org/ternary-search/  
ternary_search_recursive(arr, key) - https://www.geeksforgeeks.org/ternary-search/  
ternary_search_randomized(arr, key) -combine ternary recursive with binary randomzied  
exponential_search(arr, key) - see https://www.geeksforgeeks.org/exponential-search/
interpolation_search(arr, key) - https://www.geeksforgeeks.org/interpolation-search/ 
jump_search(arr, key) - https://www.geeksforgeeks.org/jump-search/
fibonacci_search(arr, key) - https://www.geeksforgeeks.org/fibonacci-search/ 

[4] Add code to verify that the current search determines the correct position

[5] Add code to time each of the search functions

[6] Add code to run each search multiple times for different random keys

[7] Add code to plot the timings for the algorithms. See https://www.geeksforgeeks.org/matplotlib-tutorial/ 

def plot_times(dict_algs, sizes, trials, algs, file_name):
    alg_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for alg in algs:
        alg_num += 1
        d = dict_algs[alg.__name__]
        x_axis = [j + 0.05 * alg_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=alg.__name__)
    plt.legend()
    plt.title("Runtime of Algorithms")
    plt.xlabel("Size of elements")
    plt.ylabel(f"Time for {trials} trials (ms)")
    plt.savefig(file_name)
    plt.show()
 
[8] Add code to print the timings in a table 

def print_times(dict_algs)
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_algs).T
    print(df)

Use this code as a starting point for running the searches:

def run_algs(algs, sizes, trials)
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = random_list(size)
            idx = random.randint(0, size-1)
            key = arr[idx]
            for alg in algs:
                start_time = time.time()
                idx_found = alg(arr, key)
                end_time = time.time()
                if idx_found != idx:
                    print(alg.__name__, "wrong index found", arr, idx, idx_found)
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
      return dict_algs

def main():
    sizes = [10, 100, 1000, 10000]
    searches = [native_search, linear_search, binary_search, interpolation_search, etc.]
    trials = 1000
    dict_searches = run_algs(searches, sizes, trials)
    print_times(dict_searches)
    plot_times(dict_searches, sizes, trials, searches)
