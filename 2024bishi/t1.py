# def calories_burned(weight, ride):
#     total_calories = 0
#     for i in range(len(ride) - 1):
#         velocity_1, time_1 = ride[i]
#         velocity_2, time_2 = ride[i + 1]
#         time_difference = time_2 - time_1
#         calories = (2.5 * velocity_1 - 6) * weight * (time_difference / 3600)
#         total_calories += calories
#     return int(total_calories)

# # Example usage:
# print(calories_burned(60, [[6, 0], [4, 1800], [0, 3600]]))  # should return 390


# from collections import namedtuple
# def merge(*records):
#     Patient = namedtuple('Patient', [field for record in records for field in record._fields])
#     vs = [v for record in records for v in record]
#     ans = Patient(*vs)
#     return ans



# PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
# personal_details = PersonalDetails(date_of_birth='06-04-1972')
# Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
# complexion = Complexion(eye_color='Blue', hair_color='Black')
# print(merge(personal_details, complexion))
from collections import deque

class MovingTotal:
    def __init__(self):
        self.queue = deque(maxlen=3)
        self.totals = set()

    def append(self, numbers):
        for number in numbers:
            if len(self.queue) == 3:
                oldest_total = sum(self.queue)
                self.queue.popleft()  
            
            self.queue.append(number)
            if len(self.queue) == 3:
                self.totals.add(sum(self.queue))

    def contains(self, total):
        return total in self.totals

# Example usage
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))  
    print(movingtotal.contains(9))  
    print(movingtotal.contains(12)) 
    print(movingtotal.contains(7)) 
    
    movingtotal.append([5])
    print(movingtotal.contains(6)) 
    print(movingtotal.contains(9))  
    print(movingtotal.contains(12)) 
    print(movingtotal.contains(7)) 
