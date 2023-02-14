import sys
import math

x = float(sys.argv[1])
μ = float(sys.argv[2])
σ = float(sys.argv[3])

f = (1 / (σ * math.sqrt(2 * math.pi))) * math.exp(-(x - μ) ** 2 / (2 * σ ** 2))


print f
