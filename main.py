def calculate_soh(present_capacity,rated_capacity=120):
  return(present_capacity/rated_capacity)*100 # for calculating soh
def classify(soh):
  return "healthy" if soh>80 else "exchange" if 62<=soh<=80 else "failed" #classifiy based on condition
def count_batteries_by_health(present_capacities):
  counts={"healthy": 0,
  "exchange": 0,
  "failed": 0}
  for present_capacity in present_capacities:
    soh=calculate_soh(present_capacity)
    classification=classify(soh)
    counts[classification]+=1
  return counts
    
def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70] 
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
