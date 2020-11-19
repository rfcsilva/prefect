from prefect import Task


class HelloWorldTask(Task):

    def __init__(self, msg, **kwargs):
        self.msg = msg
        super().__init__(**kwargs)

    def run(self, distanatary="World", hashtag="Swag"):
        return f"{self.msg}, {distanatary}! #{hashtag}"
