def sizeof_fmt(num, suffix="B"):
    """
    Formats a number into a human-readable string with binary prefix (e.g. KiB, MiB).
    Matches the custom format request.
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, "Yi", suffix)

def format_size(bytes_count):
    """Alias for sizeof_fmt to maintain compatibility."""
    return sizeof_fmt(bytes_count)

def format_speed(bytes_per_second):
    """Formats speed (bytes per second) using the custom sizeof_fmt."""
    return f"{sizeof_fmt(bytes_per_second, suffix='')}/s"
