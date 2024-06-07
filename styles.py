style_parse_button = """QPushButton {
    background-color: #0077FF;
    color: white;
    border: none;
    font-weight: bold;
    padding: 3px;
    margin-top: 3px;
    height: 20px;
    border-radius: 3px;
}

QPushButton:hover {
    background-color: #1a85ff;
}

QPushButton:pressed {
    background-color: #5181b8;
}
"""

style_stop_button = """QPushButton {
    background-color: #ff0000;
    color: white;
    border: none;
    font-weight: bold;
    padding: 3px;
    margin-top: 3px;
    height: 20px;
    border-radius: 3px;
}

QPushButton:hover {
    background-color: #ff5353;
}

QPushButton:pressed {
    background-color: #d10000;
}
"""

style_checkbox = """QCheckBox{ 
    background-color: transparent;
}

QCheckBox::indicator {
    border: 1px solid #d3d9de;
    margin-right: 5px;
    border-radius: 3px;
    width: 15px;
    height: 15px;
}

QCheckBox::indicator:checked {
    border: 1px solid #d3d9de;
    color: white;
    background-color: #5181b8;
    image: url(:/icon/icons/check.png);
}
"""
