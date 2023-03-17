import os
import gradio as gr


def greet(name):
    return f"Hello {name}!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(server_port=os.environ.get("GRADIO_SERVER_PORT", 8080))
