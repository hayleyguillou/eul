import itertools
def eul205():
    """Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg"""
    p = range(1, 5)
    c = range(1, 7)
    p_len = 0
    c_len = 0
    
    p_totals = dict()
    for i in range(9, 37):
      p_totals[i] = 0
    c_totals = dict()
    for i in range(6, 37):
      c_totals[i] = 0

    for roll in itertools.product(p, repeat=9):
      p_len += 1
      p_totals[sum(roll)] += 1
    for roll in itertools.product(c, repeat=6):
      c_len += 1
      c_totals[sum(roll)] += 1

    for i in range(9, 37):
      p_totals[i] /= p_len
    for i in range(6, 37):
      c_totals[i] /= c_len
    
    total_prob = 0
    for i in range(6, 37):
      c_prob = c_totals[i]
      for j in range(i+1, 37):
        if j < 9:
          continue
        p_prob = p_totals[j]
        total_prob += (c_prob * p_prob)
    
    return round(total_prob, 7)

print(eul205())
# 0.5731441
