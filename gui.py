from ipywidgets import FloatSlider, BoundedFloatText, FloatText, Button, VBox, HBox, Output, HTML, Layout, dlink, Checkbox,jslink
def create_gui():
    #layout def
    slider_layout = Layout(width='250px')
    text_layout = Layout(width='80px')
    #direktheit slider und text
    has_to_be_fast = FloatSlider(
        value=1000.0,#usedd to be 20
        min=1,
        max=2000.0,
        step=1.0,
        description='Direktheit:',
        layout=slider_layout,
        readout=False
    )
    has_to_be_fast_text = FloatText(
        value=has_to_be_fast.value,
        layout=text_layout
    )
    #only slider -> text
    dlink((has_to_be_fast, 'value'), (has_to_be_fast_text, 'value'))
    has_to_be_fast_row = HBox([has_to_be_fast, has_to_be_fast_text])

    #hausscheue slider und text
    big_nimby = FloatSlider(
        value=5000.0,
        min=1,
        max=10000.0,
        step=1.0,
        description='Hausscheue:',
        layout=slider_layout,
        readout=False
    )
    big_nimby_text = FloatText(
        value=big_nimby.value,
        layout=text_layout
    )
    
    #only slider -> text 
    dlink((big_nimby, 'value'), (big_nimby_text, 'value'))
    big_nimby_row = HBox([big_nimby, big_nimby_text])

    #anbindung slider und text
    big_yimby = FloatSlider(
        value=1000.0,
        min=0.0,
        max=2000.0,
        step=10.0,
        description='Erschließung:',
        layout=slider_layout,
        readout=False
    )
    big_yimby_text = BoundedFloatText(
        value=big_yimby.value,
        min=big_yimby.min,
        max=big_yimby.max,
        step=big_yimby.step,
        layout=text_layout
    )
    
    #slider <-> text double coupled
    jslink((big_yimby, 'value'), (big_yimby_text, 'value'))
    big_yimby_row = HBox([big_yimby, big_yimby_text])

    #überschrift
    title = HTML("""
    <h3 style="margin:0; color:#2c3e50;">Trassenparameter</h3>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Klicke auf die Karte. 
    </p>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Nach 4 Clicks wird eine Trasse generiert
    </p>
    """)

    #reset
    reset_button = Button(
        description='Reset',
        button_style='warning',
        layout=Layout(width='140px')
    )

    #initial status
    status = HTML("<b>Ready</b>")

    #toggle options for optional map and calculation elements
    show_circle = Checkbox(
        value=False,
        description='Hausradius zeigen',
        indent=False
    )
    show_blue_line = Checkbox(
        value=False,
        description='Winkelkurve zeigen',
        indent=False
    )
    show_temp_line = Checkbox(
        value=True,
        description='Iterationen zeigen',
        indent=False
    )
    make_stations = Checkbox(
        value=True,
        description='Haltepunkte generieren',
        indent=False
    )
    
    #define ui and layout
    ui = VBox(
        [
            title,
            has_to_be_fast_row,
            big_nimby_row,
            big_yimby_row,
            reset_button,
            show_circle,
            show_blue_line,
            show_temp_line,
            make_stations,
            status
        ],
        layout=Layout(
            width='360px',
            padding='12px',
            border='1px solid #d1d5db',
            border_radius='10px',
            background_color='white'
        )
    )
    
    #return ui
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
        "show_temp_line": show_temp_line,
        "make_stations": make_stations,
        "status": status,
        "ui": ui
    }
