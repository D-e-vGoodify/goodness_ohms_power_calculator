print("Welcome to the Goodify Ohms Law & Power Calculator\n")
startOver = True

# calls raedings globally for extra re-assurement against errors
global voltage
global current
global resistance
global power

history = []

# function that checks the calculation and appends its properties to a list for later analysis
def record_details(type, method, read1, read2, answer):
    if type == "voltage":
        if method == "ohms":
            input = f"Current = {read1}A, Resistance = {read2}Ω"
            result = f"Voltage(IR) = {answer}V"
        elif method == "power":
            input = f"Power = {read1}W, Current = {read2}A"
            result = f"Voltage(P/I) = {answer}V"
    elif type == "current":
        if method == "ohms":
            input = f"Voltage = {read1}V, Resistance = {read2}Ω"
            result = f"Current(V/R) = {answer}A"
        elif method == "power":
            input = f"Power = {read1}W, Voltage = {read2}V"
            result = f"Current(P/V) = {answer}A"  
    elif type == "resistance":
        if method == "ohms":
            input = f"Voltage = {read1}V, Current = {read2}A"
            result = f"Resistance(V/I) = {answer}Ω"              
        elif method == "power":
            input = f"Power = {read1}W, Current = {read2}A"
            result = f"Resistance(P/I²) = {answer}Ω"
    elif type == "power":
        input = f"Current = {read1}A, Voltage = {read2}V"
        result = f"Power(IV) = {answer}W"
        
    record = {
        "type": type,
        "inputs": input,
        "result": result,
        "number_result": answer
    }
    
    history.append(record)

# gives quick analysis of immediate calculation, with option to update
def read_results(type, value):
    global choose
    if type == "voltage":
        if value < 1.0:
            print("ℹ️  Very low voltage. Seen in analog sensor signals or minor component drops")
        elif value <= 5.5:
            print("✅ Safe logical voltage. Perfect for microcontollers (e.g Arduino)")
        elif value <= 24.0:
            print("⚙️  DC voltage good for driving DC motors, relays or LED strips")
        else:
            print("⚠️ DANGER: High voltage (> 24V)! Severe shock hazard... Ensure proper insulation")
    elif type == "current":
        if value > 5.0:
            print("⚠️ Warning: High Current (> 5A)! Risk of overheating")
        elif value < 0.001:
            print("ℹ️  Note: Extremely low current! Circuit may be open or of high resistance")
        else:
            print("✅ Current is within a safe/normal operating range")
    elif type == "resistance":
        if value < 1.0:
            print("⚠️ Warning: Very low resistance. May cause short circuit")
        else:
            print("✅ Resistance value looks stable")
    elif type == "power":
        if value > 10.0:
            print("⚠️ Warning: High power dissipation. Ensure components have high power rating!")
        else:
            print("✅ Power level is safe for standard low-power components")
            
    response = input("Are you looking to change these values (yes/no)?: ")
    if response.lower() == "yes" or response.lower() == "y":
        choose = True
    elif response.lower() == "no" or response.lower() == "n":
        choose = False
    else:
        # when a different option from "yes/y" or "no/n" is inputed, it exits the update process
        print("Wrong Response. Exiting...")
        choose = False


while startOver:
    try:
        # asks the user what to find
        choose_action = int(input("What to find?\n1. Voltage\n2. Current\n3. Resistance\n4. Power\nReply: "))
        choose = True
        
        # ensures the "input readings" text only shows when an acceptable option is picked
        if choose_action <= 4:
        	print("\nINPUT READINGS")
        
        # a loop that manages option chosen; so re-entery is allowed when errors occur, and direct updates from the read_results() function is possible
        while choose:
            if choose_action == 1:
                # choosing what formula is used to find voltage
                source = int(input("\nfrom Power or Ohms Law?\n1. Power(P=IV)\n2. Ohms(V=IR)\nReply: "))
                if source == 1:
                    power = float(input("\nPower: "))
                    current = float(input("Current: "))
                    voltage = power / current
                    print(f"Voltage is {voltage}V\n")
                    read_results("voltage", voltage)
                    record_details("voltage", "power", power, current, voltage)
                elif source == 2:
                    resistance = float(input("\nResistance: "))
                    current = float(input("Current: "))
                    voltage = current * resistance
                    print(f"Voltage is {voltage}V\n")
                    read_results("voltage", voltage)
                    record_details("voltage", "ohms", current, resistance, voltage)
                else:
                    # handles wrong source input and re-runs
                    print("Wrong Input")
            elif choose_action == 2:
                # choosing what formula is used to find current
                source = int(input("\nfrom Power or Resistance?\n1. Power(P=IV)\n2. Ohms(V=IR)\nReply: "))
                if source == 1:
                    power = float(input("\nPower: "))
                    voltage = float(input("Voltage: "))
                    current = power / voltage
                    print(f"Current is {current}A\n")
                    read_results("current", current)
                    record_details("current", "power", power, voltage, current)
                elif source == 2:
                    voltage = float(input("\nVoltage: "))
                    resistance = float(input("Resistance: "))
                    current = voltage / resistance
                    print(f"Current is {current}A\n")
                    read_results("current", current)
                    record_details("current", "ohms", voltage, resistance, current)
                else:
                    print("Wrong Input")
            elif choose_action == 3:
                # choosing what formula is used to find resistance
                source = int(input("\nfrom Power or Resistance?\n1. Power(P=IV)\n2. Ohms(V=IR)\nReply: "))
                if source == 1:
                    power = float(input("\nPower: "))
                    current = float(input("Current: "))
                    resistance = power / current**2
                    print(f"Resistance is {resistance}Ω\n")
                    read_results("resistance", resistance)
                    record_details("resistance", "power", power, current, resistance)
                elif source == 2:
                    voltage = float(input("\nVoltage: "))
                    current = float(input("Current: "))
                    resistance = voltage / current
                    print(f"Resistance is {resistance}Ω\n")
                    read_results("resistance", resistance)
                    record_details("resistance", "ohms", voltage, current, resistance)
                else:
                    print("Wrong Input")
            elif choose_action == 4:
                current = float(input("Current: "))
                voltage = float(input("Voltage: "))
                power = current * voltage
                print(f"Power is {power}W\n")
                read_results("power", power)
                record_details("power", "power", current, voltage, power)
            else:
                # handles wrong choose_action input and re-runs
                print("Wrong Input")
                choose = False
                
        quit = input("Do yo want to quit(yes/no)?: ")
        if quit.lower() == "yes" or quit.lower() == "y":
            startOver = False
        elif quit.lower() not in ["no", "n"]:
            print("Wrong Response. Rerunning...")
            
    except ValueError:
        # prints error message with an advise of possible cause
        print("Error encountered (TIP: Don't include units when recording readings)")
        
# function that does after session analysis
def report_analysis(history):
    # checks for the voltage, current, resistance and power results. NB: Only results, inputs not included
    voltageResult = [item['number_result'] for item in history if item['type'] == 'voltage']
    currentResult = [item['number_result'] for item in history if item['type'] == 'current']
    resistanceResult = [item['number_result'] for item in history if item['type'] == 'resistance']
    powerResult = [item['number_result'] for item in history if item['type'] == 'power']
    
    # checks whether the results are increasing or decreasing values e.g volts = 2 < 4 < 8 (is_volt_increasing is True)
    is_volt_increasing = all(voltageResult[i] < voltageResult[i+1] for i in range(len(voltageResult) - 1))
    is_volt_decreasing = all(voltageResult[i] > voltageResult[i+1] for i in range(len(voltageResult) - 1))
    is_current_increasing = all(currentResult[i] < currentResult[i+1] for i in range(len(currentResult) - 1))
    is_current_decreasing = all(currentResult[i] > currentResult[i+1] for i in range(len(currentResult) - 1))
    is_resist_increasing = all(resistanceResult[i] < resistanceResult[i+1] for i in range(len(resistanceResult) - 1))
    is_resist_decreasing = all(resistanceResult[i] > resistanceResult[i+1] for i in range(len(resistanceResult) - 1))
    is_pow_increasing = all(powerResult[i] < powerResult[i+1] for i in range(len(powerResult) - 1))
    is_pow_decreasing = all(powerResult[i] > powerResult[i+1] for i in range(len(powerResult) - 1))
    
    # if the results are less than two in number, send a correspondig message. And if not, send an appropriate message showing the trend(increasing/decreasing)
    if len(voltageResult) < 2:
        print("ℹ️  Not enough voltage results for a report")
    else:
        if is_volt_increasing:
            print("📈 Trend: Voltage values are increasing!")
        elif is_volt_decreasing:
            print("📉 Trend: Voltage values are decreasing!")
        else:
            print("📊 Trend: Voltage values are fluctuating!")
    if len(currentResult) < 2:
        print("ℹ️  Not enough current results for a report")
    else:
        if is_current_increasing:
            print("📈 Trend: Current values are increasing!")
        elif is_current_decreasing:
            print("📉 Trend: Current values are decreasing!")
        else:
            print("📊 Trend: Current values are fluctuating!")
    if len(resistanceResult) < 2:
        print("ℹ️  Not enough resistance results for a report")
    else:
        if is_resist_increasing:
            print("📈 Trend: Resistance values are increasing!")
        elif is_resist_decreasing:
            print("📉 Trend: Resistance values are decreasing!")
        else:
            print("📊 Trend: Resistance values are fluctuating!")
    if len(powerResult) < 2:
        print("ℹ️  Not enough power results for a report")
    else:
        if is_pow_increasing:
            print("📈 Trend: Power values are increasing!")
        elif is_pow_decreasing :
            print("📉 Trend: Power values are decreasing!")
        else:
            print("📊 Trend: Power values are fluctuating!")
        
        
    print("\n")
    # Checks if there are at least 3 points to test for linear (constant step) progression
    if len(voltageResult) >= 3:
        # Step 1: Calculate the gap (difference) between consecutive voltage readings
        volt_differences = [round(voltageResult[i+1] - voltageResult[i], 4) for i in range(len(voltageResult) - 1)]
        print(f"    Step differences between readings: {volt_differences}")

        # Step 2: Grab the first step difference as our reference
        first_diff = volt_differences[0]
        # Step 3: Check if all step differences match (using a tiny tolerance for decimal accuracy)
        is_linear = all(abs(d - first_diff) < 0.0001 for d in volt_differences)

        # Step 4: Print whether the progression is linear or non-linear
        if is_linear:
            print(f"Linear Progression Detected! Voltage changes by a steady step of {first_diff}")
        else:
            print("Non-Linear Progression (step sizes change betweeen readings)\n")
    else:
        print("ℹ️  Tip: Enter 3 or more voltage calculations to test for a linear/constant step progression")
    if len(currentResult) >= 3:
        current_differences = [round(currentResult[i+1] - currentResult[i], 4) for i in range(len(currentResult) - 1)]
        print(f"    Step differences between readings: {current_differences}")

        first_diff = current_differences[0]
        is_linear = all(abs(d - first_diff) < 0.0001 for d in current_differences)

        if is_linear:
            print(f"Linear Progression Detected! Current changes by a steady step of {first_diff}")
        else:
            print("Non-Linear Progression (step sizes change betweeen readings)\n")
    else:
        print("ℹ️  Tip: Enter 3 or more current calculations to test for a linear/constant step progression")
    if len(resistanceResult) >= 3:
        resist_differences = [round(resistanceResult[i+1] - resistanceResult[i], 4) for i in range(len(resistanceResult) - 1)]
        print(f"    Step differences between readings: {resist_differences}")

        first_diff = resist_differences[0]
        is_linear = all(abs(d - first_diff) < 0.0001 for d in resist_differences)

        if is_linear:
            print(f"Linear Progression Detected! Resistance changes by a steady step of {first_diff}")
        else:
            print("Non-Linear Progression (step sizes change betweeen readings)\n")
    else:
        print("ℹ️  Tip: Enter 3 or more resistance calculations to test for a linear/constant step progression")
    if len(powerResult) >= 3:
        pow_differences = [round(powerResult[i+1] - powerResult[i], 4) for i in range(len(powerResult) - 1)]
        print(f"    Step differences between readings: {pow_differences}")

        first_diff = pow_differences[0]
        is_linear = all(abs(d - first_diff) < 0.0001 for d in pow_differences)

        if is_linear:
            print(f"Linear Progression Detected! Power changes by a steady step of {first_diff}")
        else:
            print("Non-Linear Progression (step sizes change betweeen readings)\n")
    else:
        print("ℹ️  Tip: Enter 3 or more power calculations to test for a linear/constant step progression")
    
# history analysis section after the user quits
if history:
    print("\n" + "=" * 40)
    print("       SESSION SUMMARY REPORT")
    print("=" * 40)
    # shows the total number of calculations done
    print(f"Total calculations performed: {len(history)}")
    # iterates through the history list and shows each calculation arranged line by line
    for i, item in enumerate(history, 1):
        print(f"{i}. Calculated {item['type']} | Inputs: {item['inputs']} | Result: {item['result']}")
    print("\n" + "=" * 10 + "      Analysis      " + "=" * 10)
    # calls the function for result analysis. NB: Just result analysis, not input analysis
    report_analysis(history)
    print("=" * 40)
else:
    # the message to show if the user quits without making any calculations
    print("No calculations were performed. Goodbye")
