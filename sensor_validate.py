
def  _give_me_a_good_name(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_soc_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not _give_me_a_good_name(values[i], values[i + 1], 0.05)):
      return False
  return True

def validate_current_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not _give_me_a_good_name(values[i], values[i + 1], 0.1)):
      return False
  return True
