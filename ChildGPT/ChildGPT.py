"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

from ChildGPT.ai.llm import ChildGPT

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

childGPT = ChildGPT()


class State(pc.State):
    question: str
    answer: str

    def update_question(self, text):
        self.question = text

    def update_answer(self, text):
        self.answer = self.answer

    def clear_question(self):
        self.question = ""

    def clear_answer(self):
        self.answer = ""

    def submit(self):
        self.answer = childGPT.answer(self.question)


def index():
    return pc.container(
            pc.vstack(
            pc.heading("ChildGPT", font_size="2em"),
            pc.text_area(
                value=State.question,
                on_change=State.update_question,
            ),
            pc.hstack(
                pc.button(
                    "Clear Question", 
                    on_click=State.clear_question, 
                    bg="orange",
                    color="black",
                ),
                pc.button(
                    "Submit Question", 
                    on_click=State.submit, 
                    bg="lightgreen", 
                    color="black",
                ),
            ),
            pc.text_area(
                value=State.answer,
                on_change=State.update_answer,
            ),
            pc.button(
                "Clear Answer", 
                on_click=State.clear_answer,
                bg="orange",
                color="black",
            )
        ),
        width="75%",
        height="50%",
    )

app = pc.App(state=State)
app.add_page(index, route="/", title="ChildGPT")
app.compile()
