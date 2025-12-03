ranges_raw = "26803-38596,161-351,37-56,9945663-10044587,350019-413817,5252508299-5252534634,38145069-38162596,1747127-1881019,609816-640411,207466-230638,18904-25781,131637-190261,438347308-438525264,5124157617-5124298820,68670991-68710448,8282798062-8282867198,2942-5251,659813-676399,57-99,5857600742-5857691960,9898925025-9899040061,745821-835116,2056-2782,686588904-686792094,5487438-5622255,325224-347154,352-630,244657-315699,459409-500499,639-918,78943-106934,3260856-3442902,3-20,887467-1022885,975-1863,5897-13354,43667065-43786338"

ranges = ranges_raw.split(",")

invalid_ids = []

def check_number_repeat_pattern(pattern_str, num):
  str_check = str(num).replace(pattern_str, 'x')
  return len("x" * len(str_check)) == str_check.count("x")

def is_valid_id(num):
  num_len = len(str(num))
  for next_digit_offset in range(num_len - 1):
    digit = str(num)[0:next_digit_offset+1]

    if check_number_repeat_pattern(digit, num):
      return False
  return True

# loop through all ranges and check validity of id
for r in ranges:
  id_start = int(r.split("-")[0])
  id_end = int(r.split("-")[1])

  print(f'Checking range {id_start}-{id_end}')
  for i in range(id_start, id_end + 1):
    if not is_valid_id(i):
      invalid_ids.append(i)

print(f"Found {len(invalid_ids)} invalid ids")

print(invalid_ids)

# get solution
ids_sum = 0
for id in invalid_ids:
  ids_sum += id

print(f"Solution is {ids_sum}")
