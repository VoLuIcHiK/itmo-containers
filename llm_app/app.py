import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
from DAO import DAO
import os

model_path = os.getenv('LLM_MODEL')
model = AutoModelForCausalLM.from_pretrained(model_path)

tokenizer_path = os.getenv('TOKENIZER_MODEL')
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = (os.getenv('POSTGRES_PASSWORD'))
db_host = 'myapp_db'

dao = DAO(  
    db_name,
    db_user,
    db_password,
    db_host
)

print('DAO connected')

def write_to_db(request: str, answer: str):
    dao.log_conversation(request, answer)
    print('Data has been recorded')

# Определяем функцию, которая будет вызываться при нажатии кнопки "ask"
def ask(prompt) -> str:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.1,
        max_length=100,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    print(gen_text)
    write_to_db(prompt, gen_text)
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