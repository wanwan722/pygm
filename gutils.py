def error_rate(real, ideal):
    """ Calculate the error rate between real and ideal value"""
    if ideal == 0:
        return real;
    else:
        return float(real - ideal) / ideal * 100;