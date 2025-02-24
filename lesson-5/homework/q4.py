def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    length = len(sorted_data)
    mid = length // 2
    return (sorted_data[mid] if length % 2 != 0 else (sorted_data[mid - 1] + sorted_data[mid]) / 2)

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments, tuitions = enrollment_stats(universities)
print("******************************")
print(f"Total students: {sum(enrollments):,}")
print(f"Total tuition: $ {sum(tuitions):,}\n")
print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Student median: {median(enrollments):,}")
print(f"\nTuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")
print("******************************")
