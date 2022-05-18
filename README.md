# Coding-Competition-Software-for-Debugging-Challenge
This Software will help you to setup debugging challenge for coding competitions that you setup without much effort

----
> # How to use:
>  - Open the file Debug_Me.py in a Python IDE or Text Editor.
>  - Edit the list 'Q' on line 6 add the error code/question.
>  - Edit the list 'A' on line 38 add the correct solutions for the question in the same index.
>  - Edit the timer variables on line 72 to disable timer replace 'update_time()' with '#update_time()' on line 108.
>  - Run the code

----
> # How it works:
>  - When the start button is pressed the timer is started and the code is displayed on the left Text widgit.
>  - Next and Previous buttons allow you to go to the next and previous question in the list 'Q'.
>  - When pressed Check the input is taken from the right Text widgit and all the spaces and '\n' are removed and then compared with the answers in list 'A'.
>  - If the input is same as the answer after removing all the '\n' and ' ' from both then its correct else wrong.

----
> # Requirenments:
>  - Python
>  - TKinter
>  - Pyperclip
