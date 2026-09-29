def expanding_windows(values, min_train=4):
    for end in range(min_train, len(values)):
        yield values[:end], values[end]
