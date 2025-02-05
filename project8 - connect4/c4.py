from game import Game
from board import RED, YELLOW
from llm import LLM
import gradio as gr

all_model_names = LLM.all_model_names()

css = "footer{display:none !important}"

js = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

def message_html(game):
    return f'<div style="text-align: center;font-size:18px">{game.board.message()}</div>'

def load_callback(red_llm, yellow_llm):
    game = Game(red_llm, yellow_llm)
    enabled = gr.Button(interactive=True)
    message = message_html(game)
    return game, game.board.svg(), message, "", "", enabled, enabled, enabled

def move_callback(game):
    game.move()
    if_active = gr.Button(interactive=game.board.is_active())
    return game, game.board.svg(), game.thoughts(RED), game.thoughts(YELLOW), if_active, if_active

def run_callback(game):
    enabled = gr.Button(interactive=True)
    disabled = gr.Button(interactive=False)
    yield game, game.board.svg(), game.thoughts(RED), game.thoughts(YELLOW), disabled, disabled, disabled
    while game.board.is_active():
        game.move()
        yield game, game.board.svg(), game.thoughts(RED), game.thoughts(YELLOW), disabled, disabled, disabled
    yield game, game.board.svg(), game.thoughts(RED), game.thoughts(YELLOW), disabled, disabled, enabled

def model_callback(player_name, game, new_model_name):
    player = game.players[player_name]
    player.switch_model(new_model_name)
    return game

def red_model_callback(game, new_model_name):
    return model_callback(RED, game, new_model_name)

def yellow_model_callback(game, new_model_name):
    return model_callback(YELLOW, game, new_model_name)

def player_section(name, default):
    with gr.Row():
        gr.Markdown(f'<div style="text-align: center;font-size:18px">{name} Player</div>')
    with gr.Row():
        dropdown = gr.Dropdown(all_model_names, value=default, label="LLM", interactive=True)
    with gr.Row():
        gr.Markdown(f'<div style="text-align: center;font-size:16px">Inner thoughts</div>')
    with gr.Row():
        thoughts = gr.Markdown(label="Thoughts")
    return thoughts, dropdown
    
with gr.Blocks(title="C4 Battle", css=css, js=js, theme=gr.themes.Default(primary_hue="sky")) as blocks:

    game = gr.State()
    
    with gr.Row():
        gr.Markdown('<div style="text-align: center;font-size:24px">Four-in-a-row LLM Showdown</div>')
    with gr.Row():
        with gr.Column(scale=1):
            red_thoughts, red_dropdown = player_section("Red", "gpt-4o")
        with gr.Column(scale=2):
            with gr.Row():
                message = gr.Markdown('<div style="text-align: center;font-size:18px">The Board</div>')
            with gr.Row():
                board_display = gr.HTML()
            with gr.Row():
                with gr.Column(scale=1):
                    move_button = gr.Button("Next move")
                with gr.Column(scale=1):
                    run_button = gr.Button("Run game", variant="primary")
                with gr.Column(scale=1):
                    reset_button = gr.Button("Start Over", variant="stop")
        with gr.Column(scale=1):
            yellow_thoughts, yellow_dropdown = player_section("Yellow", "claude-3-5-sonnet-latest")
            

    blocks.load(load_callback, inputs=[red_dropdown, yellow_dropdown], outputs=[game, board_display, message, red_thoughts, yellow_thoughts, move_button, run_button, reset_button])
    move_button.click(move_callback, inputs=[game], outputs=[game, board_display, red_thoughts, yellow_thoughts, move_button, run_button])
    red_dropdown.change(red_model_callback, inputs=[game, red_dropdown], outputs=[game])
    yellow_dropdown.change(yellow_model_callback, inputs=[game, yellow_dropdown], outputs=[game])
    run_button.click(run_callback, inputs=[game], outputs=[game, board_display, red_thoughts, yellow_thoughts, move_button, run_button, reset_button])
    reset_button.click(load_callback, inputs=[red_dropdown, yellow_dropdown], outputs=[game, board_display, red_thoughts, yellow_thoughts, move_button, run_button, reset_button])
    

blocks.launch(share=False, inbrowser=True)

