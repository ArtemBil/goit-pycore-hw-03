import random;

def get_numbers_ticket(min: int, max: int, quantity: int):
  try:
    validate_number_ticket_params(min, max, quantity);
    result = set();

    # generate numbers until set contains unique numbers with length of quantity
    while len(result) != quantity:
      result.add(random.randint(min, max));

    return sorted(result);
  except ValueError as e:
    return e;

# Function validator
def validate_number_ticket_params(min: int, max: int, quantity: int):
  if min < 1:
    raise ValueError(f"The min property should not be less than 1. Provided: {min}");
  
  if max > 1000:
    raise ValueError(f"The max property should not be greater than 1000. Provided: {max}");
  
  if (max - min + 1) <= quantity:
    raise ValueError(f"The quantity property is bigger than possible values. Provided: {quantity}");



print(get_numbers_ticket(1, 49, 3));