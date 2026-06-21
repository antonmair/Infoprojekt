from ipywidgets import FloatSlider, Button, VBox, Output, HTML, Layout

def create_gui():
    # consistent width for all controls
    slider_layout = Layout(width='250px')

    # sliders
    has_to_be_fast = FloatSlider(#if divided over at spawnerhouse valiue really high like 2000000 but if * over there really low like 10
        value=20.0,
        min=0.0,
        max=2000.0,#2000000 was ex
        step=10.0,
        description='Direktheit:',
        layout=slider_layout
    )
    big_nimby = FloatSlider(#20000 #1000
        value=1000.0,
        min=0.0,
        max=2000.0,#50000 was ex 10000 was ex
        step=10.0,
        description='Hausscheue:',
        layout=slider_layout
    )
    big_yimby = FloatSlider(#maybe invert this and change to close to settlement#200 #500
        value=1250.0,#higher value here means lower value over at spawnerhouse 
        min=0.0,
        max=2000.0,#this cannot be changed because of the inverting logic in spawnrehouse.py
        step=10.0,
        description='Anbindungswichtigkeit:',
        layout=slider_layout
    )

    #title
    title = HTML("""
    <h3 style="margin:0; color:#2c3e50;">Trassenparameter</h3>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Clicke auf die Karte. 
    </p>
    <p style="margin:6px 0 2px 0; color:#6b7280;">
        Nach 4 Clicks wird eine Trasse generiert
    </p>
    """)

    #output box
    out = Output(
        layout=Layout(
            width='250px',
            min_height='90px',
            border='1px solid #d1d5db',
            padding='8px'
        )
    )

    #reset button
    reset_button = Button(
        description='Reset',
        button_style='warning',
        layout=Layout(width='140px')
    )
    #status
    status = HTML("<b>Ready</b>")
    
    #complete UI container
    ui = VBox(
        [
            title,
            has_to_be_fast,
            big_nimby,
            big_yimby,
            reset_button,
            status,
            out
        ],
        layout=Layout(
            width='360px',
            padding='12px',
            border='1px solid #d1d5db',
            border_radius='10px',
            background_color='white'
        )
    )
    
    
    return {
        "has_to_be_fast": has_to_be_fast,
        "big_nimby": big_nimby,
        "big_yimby": big_yimby,
        "reset_button": reset_button,
        "out": out,
        "status":status,
        "ui": ui
    }