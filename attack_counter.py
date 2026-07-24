# attack_counter.py

attack_count = 0


def increment_attack():
    """Increase the attack counter by 1."""
    global attack_count
    attack_count += 1


def get_attack_count():
    """Return the current attack count."""
    return attack_count


def reset_attack_count():
    """Reset the attack counter (optional)."""
    global attack_count
    attack_count = 0