def transportation():

    print("\n===== TRANSPORTATION DETAILS =====")

    # Transportation emission factors (sample values in kg CO2e/km)
    emission_factors = {
        "Car": 0.17,
        "Motorcycle": 0.08,
        "Jeepney": 0.07,
        "Bus": 0.05,
        "Train": 0.04,
        "Bicycle": 0.00,
        "Walking": 0.00
    }

    total_emissions = 0

    trips = []

    while True:

        print("\nTransportation Options:")
        print("1. Car")
        print("2. Motorcycle")
        print("3. Jeepney")
        print("4. Bus")
        print("5. Train")
        print("6. Bicycle")
        print("7. Walking")

        choice = input("\nSelect transportation (1-7): ")

        if choice == "1":
            transport = "Car"
        elif choice == "2":
            transport = "Motorcycle"
        elif choice == "3":
            transport = "Jeepney"
        elif choice == "4":
            transport = "Bus"
        elif choice == "5":
            transport = "Train"
        elif choice == "6":
            transport = "Bicycle"
        elif choice == "7":
            transport = "Walking"
        else:
            print("Invalid choice. Please try again.")
            continue

        distance = float(input("Enter daily travel distance (km): "))

        if distance < 0:
            print("Distance cannot be negative.")
            continue

        emissions = distance * emission_factors[transport]

        total_emissions += emissions

        trips.append({
            "transportation": transport,
            "distance": distance,
            "emissions": emissions
        })

        print("\nTrip Recorded!")
        print("Transportation:", transport)
        print("Distance:", distance, "km")
        print("Estimated Emissions:", round(emissions, 3), "kg CO2e")

        another = input("\nAdd another trip? (yes/no): ").lower()

        if another != "yes":
            break

    print("\n===== TRANSPORTATION SUMMARY =====")

    for trip in trips:
        print(
            trip["transportation"],
            "-",
            trip["distance"], "km -",
            round(trip["emissions"], 3), "kg CO2e"
        )

    print("\nTotal Transportation Emissions:",
          round(total_emissions, 3), "kg CO2e")

    return total_emissions
def electricity_consumption():
    print("\n===== ELECTRICITY CONSUMPTION DETAILS =====")
    
    # Electricity emission sa part na to
    #  average grid emission factor
    emission_factor = 0.71  # kg CO2e per kWh  
    
    appliances = []
    total_electricity_emissions = 0
    
    while True:
        print("\nElectricity / Appliance Tracking:")
        print("1. Record Monthly Electricity Bill (kWh)")
        print("2. Record Individual Appliance Usage")
        print("3. Finish / Done")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == "1":
            try:
                kwh = float(input("Enter total monthly electricity consumption (kWh): "))
                if kwh < 0:
                    print("Consumption cannot be negative.")
                    continue
                
                emissions = kwh * emission_factor
                total_electricity_emissions += emissions
                
                appliances.append({
                    "source": "Total Monthly Bill",
                    "usage": f"{kwh} kWh",
                    "emissions": emissions
                })
                print("\nMonthly Bill Recorded!")
                print("Estimated Emissions:", round(emissions, 3), "kg CO2e")
                
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == "2":
            appliance_name = input("Enter appliance name (e.g., Aircon, Refrigerator): ")
            try:
                kwh = float(input(f"Enter monthly energy consumption for {appliance_name} (kWh): "))
                if kwh < 0:
                    print("Consumption cannot be negative.")
                    continue
                
                emissions = kwh * emission_factor
                total_electricity_emissions += emissions
                
                appliances.append({
                    "source": appliance_name,
                    "usage": f"{kwh} kWh",
                    "emissions": emissions
                })
                print(f"\n{appliance_name} Recorded!")
                print("Estimated Emissions:", round(emissions, 3), "kg CO2e")
                
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            continue
            
        another = input("\nAdd another electricity entry? (yes/no): ").lower()
        if another != "yes":
            break
