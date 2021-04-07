# Avoid abbreviations
# i.e. Try to use descriptive variable, function and class names

# Not good 
def is_hed(dev):
    return dev.price > 10000 and dev.power > 500


# Better
def is_high_end_device(device_name):
    return device_name.price > 10000 and device_name.power > 500
