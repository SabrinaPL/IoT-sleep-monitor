class SleepScoreCalculator:
    def __init__ (self, temperature, humidity, light_level):
        self.temperature = temperature
        self.humidity = humidity
        self.light_level = light_level

    def calculate_sleep_score(self):
        score = 10  # Start with a perfect score

        # Temperature scoring (optimal: 15-20°C)
        if self.temperature < 15 or self.temperature > 20:
            score -= 3.3333

        # Humidity scoring (optimal: 30-60%)
        if self.humidity < 30 or self.humidity > 60:
            score -= 3.3333

        # Light scoring (optimal: > 1400, darker is better)
        if self.light_level < 1400:
            score -= 3.3333

        return max(0, score)  # Ensure score does not go below 0
