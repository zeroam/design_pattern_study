from __future__ import annotations

from typing import Protocol


class Subject(Protocol):
    def register_object(self, obj: Observer):
        ...

    def remove_object(self, obj: Observer):
        ...

    def notify_observers(self):
        ...


class Observer(Protocol):
    def update(self):
        ...


class Display(Protocol):
    _temperature: float
    _humidity: float
    _pressure: float

    def display(self):
        ...


class WeatherData(Subject):
    temperature: float
    humidity: float
    pressure: float
    _observers: list[Observer]

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def register_object(self, obj: Observer) -> None:
        self._observers.append(obj)

    def remove_object(self, obj: Observer) -> None:
        self._observers.remove(obj)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurement(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionDisplay(Observer, Display):
    _weather_data: WeatherData

    def __init__(self, weather_data: WeatherData) -> None:
        self._weather_data = weather_data
        weather_data.register_object(self)

    def update(self):
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self._pressure = self._weather_data.pressure
        self.display()

    def display(self):
        print(f"current condition: {self._temperature}, {self._humidity}, {self._pressure}")


class StatisticDisplay(Observer, Display):
    _weather_data: WeatherData

    def __init__(self, weather_data: WeatherData) -> None:
        self._weather_data = weather_data
        weather_data.register_object(self)

    def update(self) -> None:
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self._pressure = self._weather_data.pressure
        self.display()

    def display(self) -> None:
        print(f"statistic condition: {self._temperature}, {self._humidity}, {self._pressure}")


class ForecastDisplay(Observer, Display):
    _weather_data: WeatherData

    def __init__(self, weather_data: WeatherData) -> None:
        self._weather_data = weather_data
        weather_data.register_object(self)

    def update(self) -> None:
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self._pressure = self._weather_data.pressure
        self.display()

    def display(self) -> None:
        print(f"forecast condition: {self._temperature}, {self._humidity}, {self._pressure}")


def main() -> None:
    weather_data = WeatherData()

    # register observers
    CurrentConditionDisplay(weather_data)
    StatisticDisplay(weather_data)
    ForecastDisplay(weather_data)

    weather_data.set_measurement(temperature=56.2, humidity=10.5, pressure=1.5)
    weather_data.set_measurement(temperature=80, humidity=70, pressure=20)


if __name__ == "__main__":
    main()
