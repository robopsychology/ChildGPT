import ChildGPT.ai.api_keys as api_keys

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple


class ChildGPT:
    def __init__(self) -> None:
        llm = OpenAI(temperature=0, openai_api_key=api_keys.OPENAI_API_KEY)

        prompt = PromptTemplate(
            template="""You are friendly and only give child-appropriate answers.

        Question: {question}

        Answer:""",
            input_variables=["question"],
        )

        qa_chain = LLMChain(llm=llm, prompt=prompt)

        ethical_principle = ConstitutionalPrinciple(
            name="Ethical Principle",
            critique_request="The model should only talk about ethical and legal things.",
            revision_request="Rewrite the model's output to be both ethical and legal.",
        )

        child_friendly_principle = ConstitutionalPrinciple(
            name="Child Friendly Principle",
            critique_request="The model should only say age appropriate things to a child.",
            revision_request="Rewrite the model's output to be apprioriate for a child."
        )

        self.constitutional_chain = ConstitutionalChain.from_llm(
            chain=qa_chain,
            constitutional_principles=[ethical_principle, child_friendly_principle],
            llm=llm,
            verbose=True,
        )

    def answer(self, input_text: str) -> str:
        answer = self.constitutional_chain.run(question=input_text)
        return answer
