from prefect.core import Task


class DummyTask(Task):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        pass
