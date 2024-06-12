# ZedShaw Python Exercise #29
# This Exercise is all about...If statements not the elif

def always_true():
    return True

def always_false():
    return False

if always_true() != always_false():
    print("always_true() != always_false()")

if always_true() == always_true():
    print("always_true() == always_true()")
