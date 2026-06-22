from ipywidgets import FloatSlider, FloatText, Button, VBox, HBox, Output, HTML, Layout, dlink, Checkbox
def create_gui():
    # konsistente Breite für die Regler
    slider_layout = Layout(width='250px')

    # --- Direktheit ---
    has_to_be_fast = FloatSlider(
        value=1000.0,#usedd to be 20
        min=1,
        max=10000.0,
        step=10.0,
        description='Direktheit:',
        layout=slider_layout,
        readout=False
    )
    has_to_be_fast_text = FloatText(
        value=has_to_be_fast.value,
        layout=Layout(width='80px')
    )
    # only slider -> text
    dlink((has_to_be_fast, 'value'), (has_to_be_fast_text, 'value'))
    has_to_be_fast_row = HBox([has_to_be_fast, has_to_be_fast_text])

    # --- Hausscheue ---
    big_nimby = FloatSlider(
        value=1000.0,
        min=1,
        max=10000.0,
        step=10.0,
        description='Hausscheue:',
        layout=slider_layout,
        readout=False
    )
    big_nimby_text = FloatText(
        value=big_nimby.value,
        layout=Layout(width='80px')
    )
    dlink((big_nimby, 'value'), (big_nimby_text, 'value'))
    big_nimby_row = HBox([big_nimby, big_nimby_text])

    # --- Anbindungswichtigkeit ---
    big_yimby = FloatSlider(
        value=1250.0,
        min=0.0,
        max=2000.0,
        step=10.0,
        description='Anbindungswichtigkeit:',
        layout=slider_layout,
        readout=False
    )
    big_yimby_text = FloatText(
        value=big_yimby.value,
        layout=Layout(width='80px')
    )
    dlink((big_yimby, 'value'), (big_yimby_text, 'value'))
    big_yimby_row = HBox([big_yimby, big_yimby_text])

    title = HTML("""
    <h3 style="margin:0; color:#2c3e50;">Trassenparameter</h3>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Clicke auf die Karte. 
    </p>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Nach 4 Clicks wird eine Trasse generiert
    </p>
    """)

    #out = Output(
    #    layout=Layout(
    #        width='250px',
    #        min_height='90px',
    #        border='1px solid #d1d5db',
    #        padding='8px'
    #    )
    #)

    reset_button = Button(
        description='Reset',
        button_style='warning',
        layout=Layout(width='140px')
    )

    status = HTML("<b>Ready</b>")

    #toggle options for optional map and calculation elements
    show_circle = Checkbox(
        value=True,
        description='Show search circle',
        indent=False
    )

    show_blue_line = Checkbox(
        value=True,
        description='Show angular curve',
        indent=False
    )
    
    ui = VBox(
        [
            title,
            has_to_be_fast_row,
            big_nimby_row,
            big_yimby_row,
            show_circle,
            show_blue_line,
            reset_button,
            status,
            #out
        ],
        layout=Layout(
            width='360px',
            padding='12px',
            border='1px solid #d1d5db',
            border_radius='10px',
            background_color='white'
        )
    )
    
    return{
        "has_to_be_fast": has_to_be_fast,
        "has_to_be_fast_text": has_to_be_fast_text,
        "big_nimby": big_nimby,
        "big_nimby_text": big_nimby_text,
        "big_yimby": big_yimby,
        "big_yimby_text": big_yimby_text,
        "reset_button": reset_button,
        "show_circle": show_circle,
        "show_blue_line": show_blue_line,
        #"out": out,
        "status": status,
        "ui": ui
    }
