#!/usr/bin/env python3
"""
Drone Team Coding Assessment
Task: Convert GPS coordinates to a readable format
"""

def convert_to_readable_format(coordinate, is_latitude):
    """
    TODO: Implement this helper function
    
    This function should:
    1. Take a coordinate (like 37.77) and determine if it's latitude or longitude
    2. Figure out the direction (North/South for latitude, East/West for longitude)  
    3. Convert negative numbers to positive (absolute value)
    4. Split the number into whole degrees and decimal minutes
    5. Return a formatted string like "37 degrees 46.2 minutes North"
    
    Parameters:
    - coordinate: A decimal number like 37.77 or -122.41
    - is_latitude: True if this is latitude, False if longitude
    
    Returns:
    - A string with the readable format
    """
    # Your code here
    abs_value = abs(coordinate)

    if is_latitude: 
        if coordinate >= 0: 
            direction = "North"
        else: 
            direction = "South"
    else: 
        if coordinate >= 0: 
            direction = "East"
        else: 
            direction = "West"

    whole_num = int(abs_value)
    decimal_value = abs_value - whole_num
    minutes = 60*decimal_value

    result = f"{whole_num} degrees {minutes:.1f} minutes {direction}"
    return result

def show_drone_locations():
    """Show where the drones are located"""

    """
    TODO: Refactor this code where needed! Hint: DRY
    """

    # GPS coordinates for drone locations
    places = [
        (37.77, -122.41),  # San Francisco
        (40.71, -74.00),   # New York
        (51.50, -0.12),    # London
    ]
   
    print("Drone GPS Locations")
    print("==================")
    
    for i in range(len(places)):
        x = places[i][0]
        y = places[i][1]

        lat_result = convert_to_readable_format(x, True)
        long_result = convert_to_readable_format(y, False)
        
        print(f"Drone {i+1}:")
        print(f"  GPS: ({x}, {y})")
        print(f"  Latitude: {lat_result}")
        print(f"  Longitude: {long_result}")
        print()

def test_convert_to_readable_format():
    """Test cases for the convert_to_readable_format function"""
    print("Running Tests...")
    print("================")
    
    # Test 1: Positive latitude
    result1 = convert_to_readable_format(37.77, True)
    expected1 = "37 degrees 46.2 minutes North"
    print(f"Test 1 - Positive Latitude:")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  Result:   {'PASS' if result1 == expected1 else 'FAIL'}")
    print()
    
    # Test 2: Negative longitude
    result2 = convert_to_readable_format(-122.41, False)
    expected2 = "122 degrees 24.6 minutes West"
    print(f"Test 2 - Negative Longitude:")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  Result:   {'PASS' if result2 == expected2 else 'FAIL'}")
    print()
    
    # Test 3: Negative latitude
    result3 = convert_to_readable_format(-33.86, True)
    expected3 = "33 degrees 51.6 minutes South"
    print(f"Test 3 - Negative Latitude:")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  Result:   {'PASS' if result3 == expected3 else 'FAIL'}")
    print()
    
    # Test 4: Zero coordinate
    result4 = convert_to_readable_format(0.0, True)
    expected4 = "0 degrees 0.0 minutes North"
    print(f"Test 4 - Zero Coordinate:")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  Result:   {'PASS' if result4 == expected4 else 'FAIL'}")
    print()

def test_show_drone_locations_integration():
    """Integration test to verify show_drone_locations works with helper function"""
    import io
    import sys
    from contextlib import redirect_stdout
    
    print("Integration Test - show_drone_locations():")
    print("==========================================")
    
    # Capture output
    f = io.StringIO()
    with redirect_stdout(f):
        show_drone_locations()
    output = f.getvalue()
    
    # Check if output contains expected converted coordinates
    expected_parts = [
        "37 degrees 46.2 minutes North",
        "122 degrees 24.6 minutes West",
        "40 degrees 42.6 minutes North", 
        "74 degrees 0.0 minutes West"
    ]
    
    passes = 0
    total = len(expected_parts)
    
    for part in expected_parts:
        if part in output:
            passes += 1
            print(f"  ✓ Found: {part}")
        else:
            print(f"  ✗ Missing: {part}")
    
    print(f"\nIntegration Test Result: {passes}/{total} checks passed")
    print(f"Status: {'PASS' if passes == total else 'FAIL'}")
    print()

if __name__ == "__main__":
    print("=== BEFORE IMPLEMENTATION ===")
    print("These tests should FAIL until you implement the functions correctly\n")
    
    test_convert_to_readable_format()

    print("=== These test should still pass after you refactored! ===")
    test_show_drone_locations_integration()
    