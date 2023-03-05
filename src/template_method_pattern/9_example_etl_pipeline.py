from abc import ABC, abstractmethod


class ETLPipeline(ABC):
    def run(self):
        self.extract()
        self.transform()
        self.load()

    @abstractmethod
    def extract(self):
        ...

    @abstractmethod
    def transform(self):
        ...

    @abstractmethod
    def load(self):
        ...


class SalesETLPipeline(ETLPipeline):
    def extract(self):
        print("Extracting sales data")

    def transform(self):
        print("Transforming sales data")

    def load(self):
        print("Loading sales data")


class CustomerETLPipeline(ETLPipeline):
    def extract(self):
        print("Extracting customer data")

    def transform(self):
        print("Transforming customer data")

    def load(self):
        print("Loading customer data")


if __name__ == "__main__":
    salesETLPipeline = SalesETLPipeline()
    salesETLPipeline.run()

    customerETLPipeline = CustomerETLPipeline()
    customerETLPipeline.run()
