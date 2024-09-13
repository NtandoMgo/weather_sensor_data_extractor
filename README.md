### 1. **weather_sensor_data_extractor**

```md
# Weather Sensor Data Extractor

## Description
This Python program processes weather data from a sensor. The raw data block is extracted and broken down into useful components like temperature, pressure, coordinates, and location, which are then formatted for human-readable output.

## Features
- Extracts data between `BEGIN` and `END` tags.
- Converts the reversed location name back to readable form.
- Outputs the temperature, pressure, and coordinates.

## Functions
- `get_block(raw_data)`: Extracts a substring starting with 'BEGIN' and ending with 'END'.
- `location(block)`: Converts and returns the location in title case.
- `temperature(block)`: Extracts and returns the temperature as a real number.
- `pressure(block)`: Extracts and returns the pressure as a real number.
- `y_coordinate(block)`: Extracts and returns the Y-coordinate (latitude).
- `x_coordinate(block)`: Extracts and returns the X-coordinate (longitude).

## Sample Input
```
Enter the raw data: fbkjf kfjkdb fds BEGIN 12.2_1014:18.6E,34.0S NWOT EPAC END fdfdfds
```

## Sample Output
```
Location: Cape Town
Coordinates: 34.0S 18.6E
Temperature: 12.2 C
Pressure: 1014.0 hPa
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/NtandoMgo/weather_sensor_data_extractor.git
   ```
2. Navigate to the directory:
   ```bash
   cd weather_sensor_data_extractor
   ```
3. Run the script:
   ```bash
   python extract.py
   ```
