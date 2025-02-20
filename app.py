import chainlit as cl


@cl.set_chat_profiles
async def chat_profiles():
    return [
        cl.ChatProfile(
            name="Agent1",
            markdown_description="Test1"
        ),
        cl.ChatProfile(
            name="Agent2",
            markdown_description="Test2"            
        )
    ]

@cl.on_message
async def on_message(msg: cl.Message):
    return await cl.Message(content="Hello, world!").send()
