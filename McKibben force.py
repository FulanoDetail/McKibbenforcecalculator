import math

# Function to calculate the force generated by a McKibben muscle
def calculate_force(S, N, θ, P):
  # Calculate r
  r = (S / (2 * math.pi * N)) * math.sin(math.degrees(θ))
  
  # Calculate cot^2θ
  cot_2θ = (1 / math.tan(math.degrees(θ)))**2
  
  # Calculate csc^2θ
  csc_2θ = (1 / math.sin(math.degrees(θ)))**2
  
  # Calculate the force
  F = P * math.pi * r**2 * (3 * cot_2θ * (1 - 1.30 * 0.05)**2 - csc_2θ)
  
  return F

# Get user input for each variable
while True:
  try:
    S = float(input("Enter the length of the filaments in the braided sleeve cylinder (S) in mm: "))
    N = float(input("Enter the number of times the filaments wrap around the cylinder (N): "))
    θ = float(input("Enter the angle at which the filaments are positioned in the cylinder (θ) in degrees: "))
    P = float(input("Enter the pressure of the gas or fluid inside the muscle (P) in kPa: "))
    break
  except ValueError:
    print("Invalid input. Please enter a valid number.")

# Calculate and print the force
force = calculate_force(S, N, θ, P)
print("The force generated by the McKibben muscle is:", force, "newtons")
