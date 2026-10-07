"""Utilities for keeping an AI conversation within a context budget."""

from typing import Literal, TypedDict


class Message(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


def trim_messages(messages: list[Message], max_characters: int) -> list[Message]:
    """Return messages whose total content fits within a character budget.

    System messages are retained because they define the assistant's behavior.
    Among the remaining messages, newer messages take priority over older ones.

    Args:
        messages: Messages ordered from oldest to newest.
        max_characters: Maximum combined length of the retained content.

    Returns:
        A new list in the same chronological order as the input.

    Raises:
        ValueError: If ``max_characters`` is negative or the system messages
            alone exceed the budget.
    """
    if max_characters < 0:
        raise ValueError("max_characters cannot be negative")

    system_indices = {
        index for index, message in enumerate(messages) if message["role"] == "system"
    }
    system_size = sum(len(messages[index]["content"]) for index in system_indices)

    if system_size > max_characters:
        raise ValueError("system messages exceed the character budget")

    remaining_budget = max_characters - system_size
    retained_indices = set(system_indices)

    # Keep a continuous suffix: skipping a large recent message and retaining an
    # older one would remove the context needed to understand the older message.
    for index in range(len(messages) - 1, -1, -1):
        if index in system_indices:
            continue
        message = messages[index]
        message_size = len(message["content"])
        if message_size > remaining_budget:
            break
        retained_indices.add(index)
        remaining_budget -= message_size

    return [
        message for index, message in enumerate(messages) if index in retained_indices
    ]


if __name__ == "__main__":
    sample_messages: list[Message] = [
        {"role": "system", "content": "你是一名简洁的 Python 教师。"},
        {"role": "user", "content": "什么是列表？"},
        {"role": "assistant", "content": "列表是一种有序、可变的容器。"},
        {"role": "user", "content": "它和元组有什么区别？"},
    ]

    for message in trim_messages(sample_messages, max_characters=20):
        print(f"{message['role']}: {message['content']}")
