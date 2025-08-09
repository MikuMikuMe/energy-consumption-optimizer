To create a comprehensive Python program for an "energy-consumption-optimizer", we'll need to structure the program to: 

1. Collect and input data on energy consumption.
2. Analyze the data to identify patterns and areas for potential optimization.
3. Provide personalized recommendations for reducing energy consumption.
4. Ensure the program includes error handling, clear comments, and is user-friendly.

Here’s a sample framework for such a project:

```python
import numpy as np

class EnergyConsumptionOptimizer:
    def __init__(self, data):
        """
        Initializes the optimizer with energy consumption data.
        
        :param data: List of tuples containing (day, usage_in_kWh), e.g., [("Monday", 34), ("Tuesday", 28), ...]
        """
        self.data = data
        self.daily_usage = {}
        self.analyze_data()

    def analyze_data(self):
        """
        Analyzes the data provided to calculate daily usage averages.
        """
        try:
            for day, usage in self.data:
                if day in self.daily_usage:
                    self.daily_usage[day].append(usage)
                else:
                    self.daily_usage[day] = [usage]

            # Calculate average usage per day
            for day in self.daily_usage:
                self.daily_usage[day] = np.mean(self.daily_usage[day])

        except Exception as e:
            print(f"Error occurred during analysis: {str(e)}")

    def generate_recommendations(self):
        """
        Generates recommendations based on the average daily usage.
        """
        recommendations = []
        try:
            # Example rules for generating recommendations
            if self.daily_usage.get("Monday", 0) > 30:
                recommendations.append("Consider using energy saving mode on appliances on Monday.")
            
            if self.daily_usage.get("Sunday", 0) > 25:
                recommendations.append("Reduce the use of heating/cooling systems on Sunday.")

            if not recommendations:
                recommendations.append("Your energy usage is optimal. Keep it up!")

        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")

        return recommendations

    def get_insights(self):
        """
        Provides data-driven insights into the energy usage patterns.
        """
        try:
            total_usage = sum(self.daily_usage.values())
            print(f"Total weekly energy consumption: {total_usage} kWh")
            print("Average daily consumption:")
            for day, avg_usage in self.daily_usage.items():
                print(f"{day}: {avg_usage:.2f} kWh")

            recommendations = self.generate_recommendations()
            print("\nPersonalized Recommendations:")
            for rec in recommendations:
                print(f"- {rec}")

        except Exception as e:
            print(f"Error in retrieving insights: {str(e)}")

# Sample data
energy_data = [
    ("Monday", 34), ("Monday", 30),
    ("Tuesday", 28), ("Tuesday", 26),
    ("Wednesday", 22), ("Wednesday", 24),
    ("Thursday", 25), ("Thursday", 27),
    ("Friday", 30), ("Friday", 34),
    ("Saturday", 35), ("Saturday", 29),
    ("Sunday", 25), ("Sunday", 28)
]

if __name__ == "__main__":
    optimizer = EnergyConsumptionOptimizer(energy_data)
    optimizer.get_insights()
```

### Key Components:

1. **Initialization and Data Storage:**
   - The data is stored and analyzed upon initializing the class.

2. **Data Analysis:**
   - Calculate average daily usage of energy.
   - `analyze_data()` handles this stage of processing.

3. **Recommendation Generation:**
   - Based on the usage analysis, generate recommendations to optimize energy usage.

4. **Error Handling:**
   - Errors during data analysis and recommendation generation are caught and logged for debugging.

5. **User Interaction:**
   - Generate and print insights and recommendations based on the analysis.

This framework provides a basic model that can be expanded with further refined data inputs and more sophisticated analysis and recommendations.