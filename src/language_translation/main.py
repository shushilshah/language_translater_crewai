# #!/usr/bin/env python
import sys
from language_translation.crew import LanguageTranslationCrew


def run():
    """
#     Run the crew.
#     """

    topic = input("Enter the topic: ")
    language_mode = input("Enter the language mode: ")

    inputs = {
        'topic': topic,
        'language_mode': language_mode,
    }
    LanguageTranslationCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    topic = input("Enter the topic: ")
    language_mode = input("Enter the language mode: ")

    inputs = {
        'topic': topic,
        'language_mode': language_mode,
    }
    try:
        LanguageTranslationCrew().crew().train(n_iterations=int(
            sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LanguageTranslationCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    topic = input("Enter the topic: ")
    language_mode = input("Enter the language mode: ")

    inputs = {
        'topic': topic,
        'language_mode': language_mode,
    }
    try:
        LanguageTranslationCrew().crew().test(n_iterations=int(
            sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
