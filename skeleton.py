import abc
from datetime import date
from typing import List, Dict
from collections.abc import Mapping

class ReturnsData(Mapping):
    """ Dictionary implementation of returns."""
    def __init__(self):
        self._returns = []  # List[date, float]
        pass
    def __getitem__(self, item):
        pass
    def __iter__(self):
        pass
    def __len__(self):
        pass

class IDataRetrievalPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def load_data(self) -> bool:
        pass

class RetrieveFromJson(IDataRetrievalPolicy):
    def load_data(self) -> bool:
        return False

class RetrieveFromDatabase(IDataRetrievalPolicy):
    def load_data(self) -> bool:
        return False

class RetrieveFromFile(IDataRetrievalPolicy):
    def load_data(self) -> bool:
        return False

class IFilteringPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def filter(self, *args, **kwargs) -> None:
        pass

class FilterFromTo(IFilteringPolicy):
    def filter(self, from_date: date, to_date: date) -> None:
        pass

class FilterCalendar(IFilteringPolicy):
    def filter(self, calendar_type: str) -> None:
        pass

class IAggregationPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def set_frequency(self, frequency: str) -> None:
        pass

class DataAggregator(IAggregationPolicy):
    def set_frequency(self, frequency: str) -> None:
        pass

class IValidationPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def validate_input(self) -> None:
        pass

class IMissingDataPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def sanitize(self) -> None:
        pass

class DataValidator(IValidationPolicy, IMissingDataPolicy):
    def validate_input(self) -> None:
        pass
    def sanitize(self) -> None:
        pass

class IPersistInputPolicy(abc.ABCMeta):
    @abc.abstractmethod
    def save_inputs(sef) -> bool:
        pass
    @abc.abstractmethod
    def get_input_id(self) -> int:
        pass

class DatabasePersistor(IPersistInputPolicy):
    def save_inputs(sef) -> bool:
        pass
    def get_input_id(self) -> int:
        pass

class IInputLayer(abc.ABCMeta):
    @abc.abstractmethod
    def get_returns(self) -> ReturnsData:
        pass

    @abc.abstractmethod
    def add_filtering_policy(self) -> None:
        pass

    @abc.abstractmethod
    def add_validation_policy(self) -> None:
        pass

    @abc.abstractmethod
    def add_aggregator(self) -> None:
        pass

    @abc.abstractmethod
    def add_persistor(self) -> None:
        pass

class InputDataRetriever(IInputLayer):
    def __init__(self, accounts: List[str]) -> None:
        super().__init__()

    def get_returns(self) -> ReturnsData:
        pass
    def add_filtering_policy(self) -> None:
        pass
    def add_validation_policy(self) -> None:
        pass
    def add_aggregation(self) -> None:
        pass
    def add_persistor(self) -> None:
        pass
