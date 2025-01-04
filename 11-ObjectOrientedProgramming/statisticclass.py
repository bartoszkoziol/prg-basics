class Statistics:
    def __init__(self):
      self.numbers=[]

    def add_number(self, number):
       self.numbers.append(number)

    def display_numbers(self):
       print(f"Numbers: ", ", ".join(map(str, self.numbers)))

    def calculate_max(self):
       return max(self.numbers) if self.numbers else None
    
    def calculate_min(self):
       return min(self.numbers) if self.numbers else None
    
    def calculate_arithmetic_mean(self):
       return sum(self.numbers)/len(self.numbers) if self.numbers else None
    
    def calculate_median(self):
       if not self.numbers:
          return None
       sorted_numbers=sorted(self.numbers)
       n=len(sorted_numbers)
       mid=n//2
       if n%2==0:
          return (sorted_numbers[mid-1]+sorted_numbers[mid])/2
       else:
          return sorted_numbers[mid]
       
    def print_statistics(self):
       print(f"The smallest num: {self.calculate_min()}")
       print(f"The greatest num: {self.calculate_max()}")
       print(f"Arithmetic meean: {self.calculate_arithmetic_mean()}")
       print(f"Median: {self.calculate_median()}")
