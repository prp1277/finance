FV = []
PV = []
tV = []
PMT = []
rV = []

FV = PV * (1 - rV) ^ tV + (PMT / rV) * ((1 + rV) ^ tV - 1 * (1 + rV))
