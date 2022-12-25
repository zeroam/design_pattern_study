from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class WeatherData:
    temperature: float
    humidity: float
    pressure: float

    current_condition_display: Display
    statistic_display: Display
    forecast_display: Display

    def measurements_changed(self):
        temperature = self.temperature
        humidity = self.humidity
        pressure = self.pressure

        self.current_condition_display.display(temperature, humidity, pressure)
        self.statistic_display.display(temperature, humidity, pressure)
        self.forecast_display.display(temperature, humidity, pressure)


class Display(Protocol):
    def display(self, temperature: float, humidity: float, pressure: float):
        ...


class CurrentConditionDisplay(Display):
    def display(self, temperature: float, humidity: float, pressure: float):
        print(f"current condition: {temperature}, {humidity}, {pressure}")


class StatisticDisplay(Display):
    def display(self, temperature: float, humidity: float, pressure: float):
        print(f"statistic condition: {temperature}, {humidity}, {pressure}")


class ForecastDisplay(Display):
    def display(self, temperature: float, humidity: float, pressure: float):
        print(f"forecast condition: {temperature}, {humidity}, {pressure}")


def main():
    weather_data = WeatherData(
        temperature=56.2,
        humidity=10.1,
        pressure=1.5,
        current_condition_display=CurrentConditionDisplay(),
        statistic_display=StatisticDisplay(),
        forecast_display=ForecastDisplay(),
    )
    weather_data.measurements_changed()


if __name__ == "__main__":
    main()
