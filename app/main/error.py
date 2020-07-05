from flask import render_template
from . import main

@main.errorhandler(404)
def four_o_four(error):
    """
    function to render 404 errors
    """
    return render_template('404.html')