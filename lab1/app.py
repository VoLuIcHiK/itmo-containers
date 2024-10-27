import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Определяем функцию, которая будет вызываться при нажатии кнопки "ask"
def ask(prompt) -> str:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.5,
        max_length=100,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    print(gen_text)
    return gen_text


# Создаем интерфейс
with gr.Blocks() as demo:
    # Создаем текстовые поля и кнопку
    input_text = gr.Textbox(label="Введите текст")
    output_text = gr.Textbox(label="Результат")
    ask_button = gr.Button("ask")
    
    # Определяем действие при нажатии кнопки
    ask_button.click(fn=ask, inputs=input_text, outputs=output_text)

# Запускаем интерфейс
demo.launch(server_name='0.0.0.0', server_port=1337)