from functions.call_function import call_function
from google.genai import types

function_call_part = types.FunctionCall()

function_call_part.name = "get_files_info"
function_call_part.args = {
    "directory": "calculator"
}

call_function(function_call_part, verbose = True)
