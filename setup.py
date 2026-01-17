from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Boktiar Ahmed Bappy",
    author_email="entbappy73@gmail.com",
    description="Medical Chatbot using LangChain and HuggingFace",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "langchain",
        "langchain-community",
        "langchain-huggingface",
        "huggingface-hub",
        "pypdf",
        "faiss-cpu",
        "numpy",
        "tqdm"
    ],
    python_requires=">=3.10"
)
