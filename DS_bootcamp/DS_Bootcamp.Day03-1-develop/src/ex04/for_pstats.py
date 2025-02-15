import pstats

stats = pstats.Stats("profiling-http.prof")
stats.sort_stats("cumulative")
with open("pstats-cumulative.txt", "w") as f:
    stats.stream = f
    stats.print_stats(5)
