import math
from typing import Tuple



class Dataset:
  def __init__():
    pass







# calculating the entropy
def calc_entropy(p_vks: list[int]) -> int:
  entropy = 0
  for p_vk in p_vks:
    entropy += ( (-1)*p_vk*math.log(p_vk, 2) )
  
  return entropy

# calculating the entropy of a boolean random variable
def calc_entropy_bool(p: int):
  return calc_entropy([p, 1-p])

# expected entropy remaining after testing attribute A
"""
params:
n_examples: list[Tuple(positive_examples, negative_examples)]
"""
def calc_remainder(n_examples: list[Tuple(int, int)], total_pos, total_neg):
  remainder = 0
  for n_pos, n_neg in n_examples:
    remainder += ( (n_pos + n_neg) / (total_pos + total_neg) ) * calc_entropy_bool( (n_pos) / (n_pos + n_neg) )

  return remainder

# calculate information gain
def calc_gain(n_examples: list[Tuple(int, int)], total_pos, total_neg):
  gain = calc_entropy_bool( (total_pos) / (total_pos + total_neg) ) - calc_remainder(n_examples, total_pos, total_neg)
  return gain
